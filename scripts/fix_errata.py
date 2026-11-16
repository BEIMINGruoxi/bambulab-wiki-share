#!/usr/bin/env python3
"""对解析结果应用人工核定的勘误（官网原文自身的字符损坏）。

Bambu Lab 官网个别页面在发布时就带着 U+FFFD 替换符（UTF-8 解码正常，
说明是官方编辑时的输入损坏，不是抓取造成）。这里按上下文与同页对照
做确定性修复，避免把这些坏字符一路带进数据库和检索片段。

用法：python3 parse_zh.py && python3 fix_errata.py && python3 build_db.py
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "pages_raw.jsonl")

# (页面 path, 原文片段, 修正后, 判定依据)
ERRATA = [
    ("h3c/troubleshooting/hmscode/0700_2000_0002_0020",
     "缓冲器附近的料管破损或弯折，\ufffd\ufffd\ufffd致耗材无法顺畅通过",
     "缓冲器附近的料管破损或弯折，导致耗材无法顺畅通过",
     "同段前两条均为「导致耗材卡住」，此处应为「导致」"),
    ("h3c/troubleshooting/hmscode/0700_2000_0002_0020",
     "将断料清除后再重试进料\ufffd\ufffd\ufffd",
     "将断料清除后再重试进料。",
     "句末应为句号，后接下一条操作步骤"),
    ("h3c/troubleshooting/hmscode/0700_2000_0002_0020",
     "说明故障已\ufffd\ufffd除",
     "说明故障已解除",
     "上下文判断为「解除」"),
    ("h3c/troubleshooting/hmscode/0700_2000_0002_0020",
     "AMS C \ufffd\ufffd\ufffd 3 助力电机过载",
     "AMS C 槽 3 助力电机过载",
     "同表其他行写法为「AMS A 槽 1」「AMS B 槽 2」"),
]


def main():
    recs = [json.loads(l) for l in open(SRC, encoding="utf-8") if l.strip()]
    by_path = {r["path"]: r for r in recs}
    applied = 0
    for path, old, new, _ in ERRATA:
        r = by_path.get(path)
        if not r:
            print(f"[skip] 页面不存在：{path}")
            continue
        hit = False
        for key in ("content_md", "content_text"):
            if old in r[key]:
                r[key] = r[key].replace(old, new)
                hit = True
        if hit:
            applied += 1
        else:
            print(f"[miss] 未匹配：{path} | {old[:30]!r}")
    with open(SRC, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    left = sum(r["content_md"].count("\ufffd") + r["content_text"].count("\ufffd") for r in recs)
    print(f"勘误应用 {applied}/{len(ERRATA)} 条，剩余 U+FFFD：{left}")


if __name__ == "__main__":
    main()
