#!/usr/bin/env python3
"""构建 SQLite 知识库（中文全文索引）+ JSONL / CSV / Markdown 导出。"""
import csv
import json
import os
import re
import shutil
import sqlite3
import zipfile
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(OUT, "bambulab_wiki_zh.db")

SERIES_FALLBACK = {
    "h2": "H2 系列", "h2d": "H2D", "h2c": "H2C", "h2s": "H2S", "h2d-pro": "H2D Pro",
    "h3c": "H3C", "h-series": "H 系列", "x1": "X1 系列", "x1e": "X1E",
    "x2d": "X2D", "x-series": "X 系列", "p1": "P1 系列", "p1s": "P1S", "p2s": "P2S",
    "p3c": "P3C", "p-series": "P 系列", "a1": "A1 系列", "a1-mini": "A1 mini",
    "a1mini": "A1 mini", "a-series": "A 系列", "e1": "E1", "r1": "R1 激光雕刻机",
    "ams": "AMS", "ams3": "AMS 3", "ams3h": "AMS 3H", "ams3p": "AMS 3 Pro",
    "ams-2-pro": "AMS 2 Pro", "ams-ht": "AMS HT", "amsht": "AMS HT",
    "ams-lite": "AMS lite", "ams-series": "AMS 系列",
    "software": "软件 & APP", "bambu-studio": "Bambu Studio", "bambu-handy": "Bambu Handy",
    "bambu-suite": "Bambu Suite", "studio-handy": "Bambu Studio & Handy",
    "filament-acc": "耗材指南", "filament": "耗材", "parts-acc": "配件 & 工具",
    "part-acc": "配件 & 工具", "acc": "配件 & 工具", "laser": "激光 & 刀切",
    "laser-cutting-module": "激光切割模块", "makerworld": "MakerWorld",
    "knowledge-sharing": "经验分享", "general": "通用知识", "hms": "HMS 报错码",
    "cyberbrick": "CyberBrick", "home": "主页", "glossary": "术语表", "faq": "常见问题",
}
SECTION_FALLBACK = {
    "manual": "使用手册", "maintenance": "维护保养", "troubleshooting": "故障排除",
    "faq": "常见问题", "software": "软件", "hms": "HMS 报错码", "knowledge-sharing": "经验分享",
    "filament-acc": "耗材与配件", "makerworld": "MakerWorld", "general": "通用知识",
    "ams": "AMS", "slicer": "切片软件", "wiki": "Wiki", "guides": "指南", "guide": "指南",
}
KIND_WORDS = set(SECTION_FALLBACK)


def is_cjk(ch: str) -> bool:
    return "\u3400" <= ch <= "\u9fff" or "\uf900" <= ch <= "\ufaff"


def cjk_space(text: str) -> str:
    out = [" " + ch + " " if is_cjk(ch) else ch for ch in text]
    return re.sub(r" +", " ", "".join(out))


IMG_RE = re.compile(r"!\[[^\]]*\]\((?:[^()]|\([^()]*\))*\)")
LINK_RE = re.compile(r"\[([^\]]*)\]\((?:[^()]|\([^()]*\))*\)")


BOILER = (
    "我们希望本指南能为您提供有用的信息",
    "如果您对本指南未解决您的问题",
    "我们随时准备为您解答疑问并提供帮助",
    "如果您对本篇 Wiki 有任何建议或反馈",
    "欢迎在评论区留言",
    "感谢您的支持与关注",
    "我们希望这份指南为您提供了有效的信息",
    "如果您对本文中描述的过程有任何疑虑",
    "您可以在开始操作前联系我们的客户服务团队",
    "我们随时准备为您提供帮助并回答您的任何问题",
    "如果本指南未解决您的问题",
)


def clean_for_chunk(text: str) -> str:
    text = IMG_RE.sub("", text)
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"〔[^〕]{0,40}〕", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines = []
    for ln in text.split("\n"):
        if re.fullmatch(r"[\s|·•\-—:]+", ln):
            continue
        if any(b in ln for b in BOILER):
            continue
        lines.append(ln)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(ln for ln in text.split("\n") if not re.fullmatch(r"[\s|·•]+", ln))
    return text.strip()


def pack_paragraphs(body: str, target: int = 700, hard: int = 1200):
    body = clean_for_chunk(body)
    paras = [p.strip() for p in re.split(r"\n{2,}", body) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(p) > hard:
            if cur:
                chunks.append(cur)
                cur = ""
            sents = re.split(r"(?<=[。！？；!?])", p)
            buf = ""
            for s in sents:
                if len(buf) + len(s) > target and buf:
                    chunks.append(buf.strip())
                    buf = s
                else:
                    buf += s
            if buf.strip():
                chunks.append(buf.strip())
            continue
        if not cur:
            cur = p
        elif len(cur) + len(p) + 2 <= target:
            cur += "\n\n" + p
        else:
            chunks.append(cur)
            cur = p
    if cur.strip():
        chunks.append(cur.strip())
    return [c for c in chunks if keep_chunk(c)]


def keep_chunk(c: str) -> bool:
    if len(c) < 40:
        return False
    cjk = sum(1 for ch in c if is_cjk(ch))
    if len(c) < 120 and cjk / max(len(c), 1) < 0.15:
        return False
    return True


def split_sections(md: str):
    for p in re.split(r"\n(?=#{2,4} )", md):
        p = p.strip()
        if not p:
            continue
        m = re.match(r"(#{2,4}) (.+)", p)
        heading = m.group(2).strip() if m else ""
        body = p[m.end():].strip() if m else p
        yield heading, body


def main():
    recs = [json.loads(l) for l in open(os.path.join(BASE, "pages_raw.jsonl"), encoding="utf-8")]
    os.makedirs(OUT, exist_ok=True)
    tmp_db = os.path.join(BASE, "kb_build.db")
    for suffix in ("", "-wal", "-shm"):
        p = tmp_db + suffix
        if os.path.exists(p):
            os.remove(p)
    con = sqlite3.connect(tmp_db)
    con.executescript("""
    PRAGMA journal_mode=WAL;
    CREATE TABLE categories (
        slug TEXT PRIMARY KEY, title TEXT, url TEXT, level INTEGER, parent_slug TEXT, page_count INTEGER
    );
    CREATE TABLE pages (
        id INTEGER PRIMARY KEY, page_id TEXT, slug TEXT UNIQUE, url TEXT, title TEXT,
        description TEXT, series TEXT, series_title TEXT, section TEXT, section_title TEXT,
        category_path TEXT, kind TEXT, author TEXT, created_at TEXT, updated_at TEXT,
        tags TEXT, headings TEXT, char_count INTEGER, word_count INTEGER,
        image_count INTEGER, link_count INTEGER, images TEXT, internal_links TEXT,
        content_md TEXT, content_text TEXT
    );
    CREATE TABLE chunks (
        id INTEGER PRIMARY KEY, page_slug TEXT, page_title TEXT, heading TEXT, chunk_index INTEGER, text TEXT
    );
    CREATE VIRTUAL TABLE pages_fts USING fts5(title, category, body, tokenize='unicode61');
    CREATE VIRTUAL TABLE chunks_fts USING fts5(title, heading, body, tokenize='unicode61');
    """)

    def nice_title(r):
        t = r["title"].strip()
        if "/" in t or t == r["path"]:
            for ln in (r.get("content_text") or "").split("\n")[:6]:
                ln = re.sub(r"^\s*标签\s*", "", ln).strip()
                if len(ln) >= 8:
                    return ln[:56]
            return t
        return t

    for r in recs:
        r["display_title"] = nice_title(r)
    slug_title = {r["path"]: r["display_title"] for r in recs}
    rows, chunk_rows = [], []
    for i, r in enumerate(sorted(recs, key=lambda x: x["path"]), 1):
        parts = r["path"].split("/")
        series = parts[0] if parts else ""
        series_title = slug_title.get(series) or SERIES_FALLBACK.get(series, series)
        section = section_title = None
        if series == "miniwiki":
            real = parts[2] if len(parts) > 2 else ""
            series_title = "HMS 快速排查（" + SERIES_FALLBACK.get(real, real) + "）"
            parts = [series] + parts[1:]
            section = section_title = None
            category_path = series_title
            kind = "hms"
            rows.append((
                i, r.get("page_id", ""), r["path"], r["url"], r["display_title"], r.get("description", ""),
                series, series_title, "", "", category_path, kind,
                r.get("author", ""), r.get("created_at", ""), r.get("updated_at", ""),
                json.dumps(r.get("tags", []), ensure_ascii=False),
                json.dumps(r.get("headings", []), ensure_ascii=False),
                r.get("char_count", 0), r.get("word_count", 0),
                len(r.get("images", [])), len(r.get("links", [])),
                json.dumps(r.get("images", []), ensure_ascii=False),
                json.dumps(r.get("links", []), ensure_ascii=False),
                r.get("content_md", ""), r.get("content_text", ""),
            ))
            cidx = 0
            for heading, body in split_sections(r.get("content_md", "")):
                for piece in pack_paragraphs(body):
                    chunk_rows.append((r["path"], r["display_title"], heading, cidx, piece))
                    cidx += 1
            continue
        if len(parts) >= 2:
            cand = parts[1]
            sec_slug = f"{series}/{cand}"
            if sec_slug in slug_title:
                section, section_title = cand, slug_title[sec_slug]
            elif cand in SECTION_FALLBACK:
                section, section_title = cand, SECTION_FALLBACK[cand]
        category_path = " > ".join([x for x in [series_title, section_title] if x])
        kind = section or ""

        rows.append((
            i, r.get("page_id", ""), r["path"], r["url"], r["display_title"], r.get("description", ""),
            series, series_title, section or "", section_title or "", category_path, kind,
            r.get("author", ""), r.get("created_at", ""), r.get("updated_at", ""),
            json.dumps(r.get("tags", []), ensure_ascii=False),
            json.dumps(r.get("headings", []), ensure_ascii=False),
            r.get("char_count", 0), r.get("word_count", 0),
            len(r.get("images", [])), len(r.get("links", [])),
            json.dumps(r.get("images", []), ensure_ascii=False),
            json.dumps(r.get("links", []), ensure_ascii=False),
            r.get("content_md", ""), r.get("content_text", ""),
        ))

        cidx = 0
        sections = list(split_sections(r.get("content_md", "")))
        if len(sections) == 1 and not sections[0][0]:
            for piece in pack_paragraphs(sections[0][1]):
                chunk_rows.append((r["path"], r["display_title"], "", cidx, piece))
                cidx += 1
        else:
            for heading, body in sections:
                for piece in pack_paragraphs(body):
                    chunk_rows.append((r["path"], r["display_title"], heading, cidx, piece))
                    cidx += 1

    con.executemany("INSERT INTO pages VALUES (" + ",".join(["?"] * 25) + ")", rows)
    con.executemany("INSERT INTO chunks(page_slug,page_title,heading,chunk_index,text) VALUES (?,?,?,?,?)", chunk_rows)
    for row in rows:
        con.execute("INSERT INTO pages_fts(rowid,title,category,body) VALUES (?,?,?,?)",
                    (row[0], cjk_space(row[4]), cjk_space(row[10]), cjk_space(row[24])))
    for cid, (slug, ptitle, heading, idx, text) in enumerate(chunk_rows, 1):
        con.execute("INSERT INTO chunks_fts(rowid,title,heading,body) VALUES (?,?,?,?)",
                    (cid, cjk_space(ptitle), cjk_space(heading), cjk_space(text)))
    con.execute("UPDATE chunks SET id = rowid")

    cat_counts = Counter()
    for row in rows:
        series, series_title, section, section_title = row[6], row[7], row[8], row[9]
        cat_counts[(series, series_title, 1)] += 1
        if section:
            cat_counts[(f"{series}/{section}", section_title, 2)] += 1
    for (slug, title, level), n in cat_counts.items():
        parent = slug.rsplit("/", 1)[0] if "/" in slug else ""
        con.execute("INSERT OR REPLACE INTO categories VALUES (?,?,?,?,?,?)",
                    (slug, title, f"https://wiki.bambulab.com/zh/{slug}", level, parent, n))
    con.commit()
    con.execute("VACUUM")
    con.close()
    shutil.move(tmp_db, DB)

    def page_obj(row):
        return {
            "id": row[0], "slug": row[2], "url": row[3], "title": row[4], "description": row[5],
            "series": row[7], "section": row[9], "category_path": row[10], "kind": row[11],
            "author": row[12], "created_at": row[13], "updated_at": row[14],
            "tags": json.loads(row[15]), "headings": json.loads(row[16]),
            "char_count": row[17], "image_count": row[19],
            "images": json.loads(row[21]), "links": json.loads(row[22]),
            "content_md": row[23], "content_text": row[24],
        }

    with open(os.path.join(OUT, "bambulab_wiki_zh.jsonl"), "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(page_obj(row), ensure_ascii=False) + "\n")

    with open(os.path.join(OUT, "bambulab_wiki_zh_chunks.jsonl"), "w", encoding="utf-8") as f:
        for cid, (slug, ptitle, heading, idx, text) in enumerate(chunk_rows, 1):
            f.write(json.dumps({
                "chunk_id": cid, "slug": slug, "title": ptitle, "heading": heading,
                "url": f"https://wiki.bambulab.com/zh/{slug}",
                "text": (f"{ptitle} / {heading}\n{text}" if heading else f"{ptitle}\n{text}"),
            }, ensure_ascii=False) + "\n")

    with open(os.path.join(OUT, "bambulab_wiki_zh_index.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "url", "series", "section", "kind", "category_path",
                    "updated_at", "char_count", "image_count"])
        for row in rows:
            w.writerow([row[0], row[4], row[3], row[7], row[9], row[11], row[10], row[14], row[17], row[19]])

    md_dir = os.path.join(OUT, "markdown")
    # 直接就地覆盖写，不做整目录删除：避免误删且便于增量重建
    os.makedirs(md_dir, exist_ok=True)
    for r in rows:
        # 文件路径与 slug 一一对应，便于按 slug 直接定位原文
        fn = os.path.join(md_dir, *r[2].split("/")) + ".md"
        os.makedirs(os.path.dirname(fn) or md_dir, exist_ok=True)
        fm = (f"---\ntitle: {r[4]}\nurl: {r[3]}\ncategory: {r[10]}\nupdated: {r[14]}\n---\n\n")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(fm + r[23] + "\n")

    zip_path = os.path.join(OUT, "bambulab_wiki_zh_markdown.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for root, _, files in os.walk(md_dir):
            for name in files:
                full = os.path.join(root, name)
                z.write(full, os.path.relpath(full, md_dir))

    cat_n = sqlite3.connect(DB).execute("SELECT COUNT(*) FROM categories").fetchone()[0]
    stats = {
        "pages": len(rows), "chunks": len(chunk_rows), "categories": cat_n,
        "char_total": sum(r[17] for r in rows),
        "db_bytes": os.path.getsize(DB),
        "md_files": sum(len(fs) for _, _, fs in os.walk(md_dir)),
    }
    with open(os.path.join(OUT, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
