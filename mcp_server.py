#!/usr/bin/env python3
"""Bambu Lab 中文 Wiki 知识库 MCP 服务（stdio，纯标准库，无第三方依赖）。

注册到 AuroraBot / 其它支持 MCP 的客户端即可，暴露两个工具：
  - search_bambu_wiki : 语义关键词检索（返回标题/链接/片段）
  - get_bambu_page    : 按 slug 或标题读取整页 Markdown

日志一律写 stderr，stdout 只输出 MCP JSON-RPC 报文。
"""
import json
import sys

import kb_search

SERVER_INFO = {"name": "bambulab-wiki-zh", "version": "1.0.0"}
PROTOCOL = "2024-11-05"

TOOLS = [
    {
        "name": "search_bambu_wiki",
        "description": "检索拓竹（Bambu Lab）官方中文 Wiki。适用于打印机安装/使用、故障排查、维护保养、AMS、耗材、Bambu Studio/Handy 软件、HMS 报错码等问题。返回最相关的知识条目片段与原文链接。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "用户问题或关键词，例如“AMS 卡料怎么办”“H2D 喷嘴堵塞”"},
                "top_k": {"type": "integer", "description": "返回条数，默认 5", "default": 5},
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_bambu_page",
        "description": "按页面 slug 或标题读取 BamBu Lab 中文 Wiki 的整页 Markdown 原文，用于在检索到相关页面后获取完整步骤。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "slug_or_title": {"type": "string", "description": "页面 slug（如 x1/maintenance/replace-hotend）或页面标题"},
            },
            "required": ["slug_or_title"],
        },
    },
]


def handle(req: dict):
    method = req.get("method")
    rid = req.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": PROTOCOL, "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": SERVER_INFO}}
    if method in ("notifications/initialized", "notifications/cancelled"):
        return None
    if method == "ping":
        return {"jsonrpc": "2.0", "id": rid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        try:
            if name == "search_bambu_wiki":
                q = args.get("query", "")
                k = int(args.get("top_k") or 5)
                res = kb_search.search(q, top_k=max(1, min(k, 20)))
                text = json.dumps({"query": q, "count": len(res), "results": res}, ensure_ascii=False, indent=2)
                if not res:
                    text = json.dumps({"query": q, "count": 0, "results": [],
                                       "hint": "未命中，可换更通用的关键词（如机型名、部件名、报错码）"}, ensure_ascii=False)
            elif name == "get_bambu_page":
                page = kb_search.get_page(args.get("slug_or_title", ""))
                if not page:
                    return {"jsonrpc": "2.0", "id": rid, "result": {
                        "content": [{"type": "text", "text": "未找到该页面，请先用 search_bambu_wiki 检索。"}],
                        "isError": True}}
                if page.get("error"):
                    return {"jsonrpc": "2.0", "id": rid, "result": {
                        "content": [{"type": "text", "text": json.dumps(page, ensure_ascii=False)}], "isError": True}}
                md = f"# {page['title']}\n\n来源：{page['url']}\n分类：{page.get('category_path','')}\n更新：{page.get('updated_at','')[:10]}\n\n{page['content_md']}"
                text = md
            else:
                return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"unknown tool: {name}"}}
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": text}], "isError": False}}
        except Exception as e:  # noqa
            return {"jsonrpc": "2.0", "id": rid, "result": {
                "content": [{"type": "text", "text": f"工具执行失败：{e}"}], "isError": True}}
    if method in ("resources/list", "prompts/list"):
        return {"jsonrpc": "2.0", "id": rid, "result": {"resources": []} if method == "resources/list" else {"prompts": []}}
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"method not found: {method}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            print("invalid json line", file=sys.stderr)
            continue
        resp = handle(req)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
