#!/usr/bin/env python3
"""Bambu Lab 中文 Wiki 知识库检索模块（可被机器人直接 import，也可命令行使用）。

用法：
    python3 kb_search.py "AMS 卡料"           # 命令行检索
    python3 kb_search.py --page x1/maintenance/replace-hotend   # 取整页
"""
import argparse
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "bambulab_wiki_zh.db")
BASE_URL = "https://wiki.bambulab.com/zh/"


def _is_cjk(ch: str) -> bool:
    return "\u3400" <= ch <= "\u9fff" or "\uf900" <= ch <= "\ufaff"


def cjk_space(text: str) -> str:
    out = []
    for ch in text:
        out.append(" " + ch + " " if _is_cjk(ch) else ch)
    return re.sub(r" +", " ", "".join(out))


NOISE = (
    "怎么调", "如何调", "怎样调", "怎么解决", "如何解决", "怎样解决", "怎么处理", "如何处理",
    "怎么办", "咋办", "怎么回事", "怎么弄", "如何弄", "怎么设置", "如何设置", "怎么用", "如何使用",
    "请问", "一下", "帮我", "我想", "我要", "想问", "求助", "有没有", "能不能", "可不可以",
)


def normalize_query(q: str) -> str:
    q = (q or "").strip()
    for w in NOISE:
        q = q.replace(w, " ")
    q = re.sub(r"[？?！!。，,、]+$", "", q)
    return re.sub(r"\s+", " ", q).strip()


def fts_query(q: str) -> str:
    q = normalize_query(q)
    q = re.sub(r"[^\w\u4e00-\u9fff\s\-\.]+", " ", q or "")
    terms = []
    for part in re.split(r"\s+", q.strip()):
        for run in re.findall(r"[\u3400-\u9fff\uf900-\ufaff]+|[A-Za-z0-9][A-Za-z0-9\-\.]*", part):
            if _is_cjk(run[0]):
                terms.append('"' + " ".join(run) + '"')
            else:
                terms.append('"' + run + '"')
    return " AND ".join(terms)


def fts_query_or(q: str) -> str:
    q = normalize_query(q)
    q = re.sub(r"[^\w\u4e00-\u9fff\s\-\.]+", " ", q or "")
    terms = []
    for part in re.split(r"\s+", q.strip()):
        for run in re.findall(r"[\u3400-\u9fff\uf900-\ufaff]+|[A-Za-z0-9][A-Za-z0-9\-\.]*", part):
            if _is_cjk(run[0]):
                terms.append('"' + " ".join(run) + '"')
            else:
                terms.append('"' + run + '"')
    return " OR ".join(terms)


def connect():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"数据库不存在：{DB_PATH}")
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def _key_terms(q: str) -> set:
    out = set()
    for part in q.split():
        for run in re.findall(r"[\u3400-\u9fff\uf900-\ufaff]+|[A-Za-z0-9][A-Za-z0-9\-\.]*", part):
            if _is_cjk(run[0]):
                if len(run) <= 2:
                    out.add(run)
                else:
                    for i in range(len(run) - 1):
                        out.add(run[i:i + 2])
            else:
                out.add(run.lower())
    return out


HMS_RE = re.compile(r"(?i)\bHMS\b|HMS[_-]|\d{4}[-_]\d{4}|错误码|报错码|故障码")
# 用户问的是"怎么做"而不是"这是什么错"时，操作指南应优先于报错码页
ACTION_RE = re.compile(r"清理|清除|疏通|更换|拆|安装|组装|维护|保养|润滑|校准|标定|调平|设置|调节|配置|参数|升级|教程|步骤|指南|怎么调|怎么设")


def _is_hms_row(r) -> bool:
    """判断一条结果是否属于 HMS 报错码页（含 miniwiki 快速排查页）。"""
    try:
        slug = r["slug"] or ""
        series = r["series"] or ""
        title = r["title"] or ""
    except (IndexError, KeyError):
        return False
    return "/hmscode/" in slug or series == "miniwiki" or title.startswith(("HMS_", "HMS-"))


def _bigram_query(q: str) -> str:
    terms = []
    for part in re.split(r"\s+", q.strip()):
        for run in re.findall(r"[\u3400-\u9fff\uf900-\ufaff]+|[A-Za-z0-9][A-Za-z0-9\-\.]*", part):
            if _is_cjk(run[0]):
                if len(run) == 1:
                    terms.append('"' + run + '"')
                else:
                    terms += ['"' + " ".join(run[i:i + 2]) + '"' for i in range(len(run) - 1)]
            else:
                terms.append('"' + run + '"')
    return " OR ".join(terms)


MODEL_FAMILY = {
    "h2": ["h2"], "h2d": ["h2", "h2d", "h2d-pro"], "h2c": ["h2", "h2c"], "h2s": ["h2", "h2s"],
    "h3c": ["h3c", "h3"], "x1": ["x1", "x1c", "x1e"], "x1c": ["x1", "x1c"], "x1e": ["x1", "x1e"],
    "x2d": ["x2d", "x2"], "p1": ["p1", "p1p", "p1s"], "p1p": ["p1", "p1p"], "p1s": ["p1", "p1s"],
    "p2s": ["p2s"], "p3c": ["p3c"], "a1": ["a1", "a1mini", "a1-mini"],
    "a1mini": ["a1", "a1mini", "a1-mini"], "ams": ["ams"], "r1": ["r1"], "e1": ["e1"],
}

MODEL_WORDS = {
    "h2", "h2d", "h2c", "h2s", "h3c", "x1", "x1c", "x1e", "x2d", "p1", "p1p", "p1s",
    "p2s", "p3c", "a1", "a1mini", "a1-mini", "ams", "ams2", "ams3", "ams-ht", "r1", "e1",
}


def split_model_terms(q: str):
    toks = re.findall(r"[A-Za-z0-9][A-Za-z0-9\-\.]*|[\u3400-\u9fff]+", q)
    model = [t for t in toks if t.lower() in MODEL_WORDS]
    rest = " ".join(t for t in toks if t.lower() not in MODEL_WORDS)
    return model, rest


SQL = """
SELECT chunks_fts.rowid AS rid, p.title, p.url, c.heading, c.text, p.updated_at, p.series, p.slug,
       bm25(chunks_fts, 15.0, 6.0, 1.0) AS score
FROM chunks_fts
JOIN chunks c ON c.id = chunks_fts.rowid
JOIN pages p ON p.slug = c.page_slug
WHERE chunks_fts MATCH ?
ORDER BY score
LIMIT ?
"""


def search(query: str, top_k: int = 5, max_per_page: int = 1) -> list:
    """段落级检索，返回 [{title,url,heading,snippet,score}]"""
    query = normalize_query(query) or query
    if not re.search(r"[\w\u4e00-\u9fff]", query):
        return []
    results = []
    con = connect()
    rows = []
    model, content_q = split_model_terms(query)
    and_q = fts_query(query)
    content_and = fts_query(content_q) if content_q else ""
    try:
        if and_q:
            rows = list(con.execute(SQL, (and_q, max(top_k * 10, 40))).fetchall())
        if content_and and content_and != and_q:
            extra = con.execute(SQL, (content_and, max(top_k * 10, 40))).fetchall()
            seen = {r["rid"] for r in rows}
            rows += [r for r in extra if r["rid"] not in seen]
        extra = con.execute(SQL, (_bigram_query(content_q or query), max(top_k * 10, 40))).fetchall()
        seen = {r["rid"] for r in rows}
        rows += [r for r in extra if r["rid"] not in seen]
    except sqlite3.OperationalError:
        rows = []
    if not rows:
        rows_like = con.execute(
            "SELECT title,url,'' AS heading,content_text AS text,updated_at,series,slug,0 AS score,id AS rid FROM pages "
            "WHERE content_text LIKE ? OR title LIKE ? LIMIT ?",
            (f"%{query}%", f"%{query}%", max(top_k * 4, 12)),
        ).fetchall()
        rows = rows_like

    terms = _key_terms(content_q or query)
    fam = sorted({f for m in model for f in MODEL_FAMILY.get(m.lower(), [m.lower()])})
    want_hms = bool(HMS_RE.search(query))

    def intent_bonus(r) -> int:
        """意图分流：问报错码时优先报错页；问操作步骤时压低报错页，避免其抢占操作指南。
        纯故障描述（如"AMS 卡料"）不降权——此时报错页往往正是对症的。"""
        h = _is_hms_row(r)
        if want_hms:
            return 2 if h else -1
        if h and ACTION_RE.search(query):
            return -2
        return 0

    def coverage(title: str) -> int:
        t = (title or "").lower()
        return sum(1 for k in terms if k in t)

    def model_hit(r) -> int:
        try:
            series = r["series"] or ""
            slug = r["slug"] or ""
        except (IndexError, KeyError):
            series, slug = "", ""
        hay = ((r["title"] or "") + " " + series + " " + slug).lower()
        return 1 if any(m in hay for m in fam) else 0

    rows = sorted(rows, key=lambda r: (-(coverage(r["title"]) + 2 * model_hit(r) + intent_bonus(r)), float(r["score"] or 0)))

    per_page = {}
    for r in rows:
        url = r["url"]
        if per_page.get(url, 0) >= max_per_page:
            continue
        per_page[url] = per_page.get(url, 0) + 1
        text = (r["text"] or "").strip().replace("\n", " ")
        snippet = text[:260] + ("…" if len(text) > 260 else "")
        results.append({
            "title": r["title"], "url": url, "heading": r["heading"] or "",
            "snippet": snippet, "score": round(float(r["score"] or 0), 3),
            "updated_at": (r["updated_at"] or "")[:10],
        })
        if len(results) >= top_k:
            break
    con.close()
    return results


def get_page(slug_or_url: str) -> dict | None:
    slug = slug_or_url.replace("https://wiki.bambulab.com/zh/", "").replace("https://wiki.bambulab.com/en/", "").strip("/")
    con = connect()
    row = con.execute(
        "SELECT id,slug,url,title,description,series_title,section_title,category_path,"
        "author,created_at,updated_at,char_count,content_md FROM pages WHERE slug = ? OR title = ?",
        (slug, slug_or_url),
    ).fetchone()
    if not row:
        rows = con.execute("SELECT slug,title FROM pages WHERE title LIKE ? LIMIT 5", (f"%{slug_or_url}%",)).fetchall()
        con.close()
        return {"error": "not_found", "candidates": [dict(r) for r in rows]} if rows else None
    d = dict(row)
    con.close()
    return d


def categories() -> list:
    con = connect()
    rows = con.execute("SELECT slug,title,level,page_count FROM categories ORDER BY level, page_count DESC").fetchall()
    con.close()
    return [dict(r) for r in rows]


def main():
    ap = argparse.ArgumentParser(description="Bambu Lab 中文 Wiki 知识库检索")
    ap.add_argument("query", nargs="?", help="检索关键词，如 “AMS 卡料”")
    ap.add_argument("--page", help="按 slug 取整页，如 x1/maintenance/replace-hotend")
    ap.add_argument("--top", type=int, default=5, help="返回条数，默认 5")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    if args.page:
        page = get_page(args.page)
        if not page:
            print("未找到该页面")
            sys.exit(1)
        print(json.dumps(page, ensure_ascii=False, indent=2) if args.json else page["content_md"])
        return
    if not args.query:
        ap.print_help()
        return
    results = search(args.query, top_k=args.top)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    if not results:
        print("没有找到相关内容")
        return
    for i, r in enumerate(results, 1):
        print(f"\n[{i}] {r['title']}" + (f" · {r['heading']}" if r["heading"] else ""))
        print(f"    {r['url']}  （更新 {r['updated_at']}）")
        print(f"    {r['snippet']}")


if __name__ == "__main__":
    main()
