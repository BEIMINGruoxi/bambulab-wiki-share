#!/usr/bin/env python3
"""解析缓存的 Wiki 页面 HTML -> 结构化 JSON 记录（含 Markdown 正文）。"""
import base64
import glob
import gzip
import json
import os
import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag

try:  # bs4 >= 4.13 会把 <template> 内的文本标记为 TemplateString
    from bs4.element import TemplateString
    TEXT_TYPES = (NavigableString, TemplateString)
except ImportError:  # 旧版 bs4 无此类型
    TemplateString = NavigableString
    TEXT_TYPES = (NavigableString,)

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = "https://wiki.bambulab.com"


def text_of(el) -> str:
    """取元素文本。bs4>=4.13 中 <template> 内文本为 TemplateString，
    默认 get_text 不收集它，必须显式指定 types，否则整页标题与链接文字为空。"""
    try:
        return el.get_text(" ", strip=True, types=TEXT_TYPES)
    except TypeError:  # 极旧版本不支持 types 参数
        return el.get_text(" ", strip=True)


def text_of_block(el) -> str:
    """块级取文本，段落间用换行分隔。"""
    try:
        return el.get_text("\n", strip=True, types=TEXT_TYPES)
    except TypeError:
        return el.get_text("\n", strip=True)


def clean_inline(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u200b", "")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def abs_url(href: str, page_url: str) -> str:
    if not href:
        return ""
    if href.startswith("http"):
        return href
    return urljoin(page_url, href)


def md_table(tbl: Tag) -> str:
    rows = []
    for tr in tbl.find_all("tr"):
        cells = []
        for c in tr.find_all(["th", "td"]):
            txt = clean_inline(text_of(c)).replace("|", "\\|")
            n_img = len(c.find_all("img"))
            if n_img:
                imgs = [clean_inline(i.get("alt", "")) or "图片" for i in c.find_all("img")]
                tag = "〔" + "、".join(imgs[:2]) + ("…" if len(imgs) > 2 else "") + "〕"
                txt = (txt + " " + tag).strip() if txt else tag
            cells.append(txt)
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * ncol) + " |"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out) + "\n\n"


def to_md(node: Tag, page_url: str, links: list, images: list, level: int = 0) -> str:
    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            txt = clean_inline(str(child))
            if txt:
                out.append(txt + " ")
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()
        cls = " ".join(child.get("class", []))
        if name in ("script", "style", "noscript", "iframe", "comments"):
            continue
        if "toc-anchor" in cls:
            continue
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            lv = int(name[1])
            txt = re.sub(r"^¶\s*", "", clean_inline(text_of(child)))
            if txt:
                out.append("\n\n" + "#" * min(lv + 1, 6) + " " + txt + "\n\n")
        elif name == "p":
            inner = to_md(child, page_url, links, images, level)
            if inner.strip():
                out.append("\n\n" + inner.strip() + "\n\n")
        elif name in ("ul", "ol"):
            out.append("\n\n")
            for i, li in enumerate(child.find_all("li", recursive=False), 1):
                inner = to_md(li, page_url, links, images, level + 1).strip()
                prefix = f"{i}. " if name == "ol" else "- "
                indent = "  " * level
                lines = inner.split("\n")
                out.append(indent + prefix + lines[0] + "\n")
                for ln in lines[1:]:
                    if ln.strip():
                        out.append(indent + "  " + ln.strip() + "\n")
            out.append("\n")
        elif name == "table":
            out.append("\n\n" + md_table(child))
        elif name == "pre":
            code = text_of_block(child).strip("\n")
            out.append("\n\n```\n" + code + "\n```\n\n")
        elif name in ("blockquote", "div", "section", "article", "span", "details", "summary"):
            inner = to_md(child, page_url, links, images, level)
            if name == "blockquote" and inner.strip():
                out.append("\n\n> " + inner.strip().replace("\n", "\n> ") + "\n\n")
            elif inner.strip():
                out.append(("\n\n" if name in ("div", "section", "article", "details") else "") + inner.strip())
                if name in ("div", "section", "article", "details"):
                    out.append("\n\n")
        elif name == "a":
            href = abs_url(child.get("href", ""), page_url)
            txt = clean_inline(text_of(child))
            if href and href.startswith("https://wiki.bambulab.com/"):
                if "/zh/" in href:
                    links.append({"title": txt, "url": href.split("#")[0]})
            if txt and href:
                out.append(f"[{txt}]({href}) ")
            elif txt:
                out.append(txt + " ")
        elif name == "img":
            src = abs_url(child.get("src", ""), page_url)
            alt = clean_inline(child.get("alt", "")) or "图片"
            if src:
                images.append({"alt": alt, "src": src})
            out.append(f"\n\n![{alt}]({src})\n\n")
        elif name in ("oembed", "video", "audio", "source"):
            src = child.get("url") or child.get("src") or ""
            if src:
                out.append(f"\n\n{abs_url(src, page_url)}\n\n")
        elif name == "br":
            out.append("\n")
        elif name == "hr":
            out.append("\n\n---\n\n")
        elif name == "code":
            out.append("`" + text_of(child) + "`")
        else:
            inner = to_md(child, page_url, links, images, level)
            if inner.strip():
                out.append(inner)
    return "".join(out)


def tidy_md(s: str) -> str:
    s = s.replace("\u00a0", " ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"^\s*¶\s*", "", s, flags=re.M)
    return s.strip()


def parse_file(fp: str) -> dict | None:
    with gzip.open(fp, "rb") as f:
        html = f.read().decode("utf-8", "replace")
    soup = BeautifulSoup(html, "lxml")
    pg = soup.find("page")
    if pg is None:
        return None
    path = pg.get("path", "").strip("/")
    title = clean_inline(pg.get("title", "")) or path
    desc = clean_inline(pg.get("description", ""))
    created = pg.get("created-at", "")
    updated = pg.get("updated-at", "")
    author = clean_inline(pg.get("author-name", ""))
    page_id = pg.get(":page-id", "")
    filename = pg.get("filename", "")
    tags = []
    raw_tags = pg.get(":tags")
    if raw_tags:
        try:
            tags = json.loads(raw_tags.replace("&quot;", '"'))
        except Exception:
            tags = []

    tpl = pg.find("template", slot="contents") or pg.find("template")
    if tpl is None:
        return None
    links, images = [], []
    md = tidy_md(to_md(tpl, f"{ROOT}/zh/{path}", links, images))
    text = tidy_md(text_of_block(tpl))
    text = re.sub(r"^\s*¶\s*", "", text, flags=re.M)
    # 去掉纯分隔符行（如 “| | |”），压缩多余空行
    text = "\n".join(ln for ln in text.split("\n") if not re.fullmatch(r"[\s|·•]+", ln))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    # 去重链接
    seen = set()
    uniq_links = []
    for l in links:
        key = l["url"]
        if key in seen:
            continue
        seen.add(key)
        uniq_links.append(l)

    headings = []
    for h in tpl.find_all(re.compile(r"h[1-4]")):
        txt = re.sub(r"^¶\s*", "", clean_inline(text_of(h)))
        if txt:
            headings.append({"level": int(h.name[1]), "text": txt})

    cn = len(re.findall(r"[\u4e00-\u9fff]", text))
    en = len(re.findall(r"[A-Za-z]+", text))
    return {
        "page_id": page_id,
        "path": path,
        "url": f"{ROOT}/zh/{path}",
        "title": title,
        "description": desc,
        "filename": filename,
        "author": author,
        "created_at": created,
        "updated_at": updated,
        "tags": tags,
        "headings": headings,
        "char_count": cn,
        "word_count": en,
        "content_md": md,
        "content_text": text,
        "images": images,
        "links": uniq_links,
    }


def main():
    files = sorted(glob.glob(os.path.join(BASE, "cache", "*.html.gz")))
    recs = []
    for i, fp in enumerate(files):
        try:
            r = parse_file(fp)
            if r:
                recs.append(r)
        except Exception as e:
            print("ERR", fp, e)
    out = os.path.join(BASE, "pages_raw.jsonl")
    with open(out, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("parsed", len(recs), "->", out)


if __name__ == "__main__":
    main()
