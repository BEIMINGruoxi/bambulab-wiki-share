# Bambu Lab 中文 Wiki 知识库

> ## ⚠️ 版权声明（务必先读）
>
> **本仓库收录的全部页面正文、图片链接、术语释义，著作权均归 Bambu Lab（拓竹）所有。**
> 本仓库**不是**官方项目，与 Bambu Lab 无任何关联，内容可能存在滞后或偏差，一切以[官方 Wiki](https://wiki.bambulab.com/zh/home) 为准。
>
> 本仓库仅作**个人技术存档与本地检索工具的技术演示**，不对内容主张任何权利，不用于商业用途。
> 若你是权利人并认为本仓库侵犯了你的权益，请提 Issue 或邮件联系仓库所有者，**我会在收到通知后立即删除相关内容或整个仓库**。
>
> 本仓库自行编写的代码（`kb_search.py`、`mcp_server.py`、`scripts/` 下的全部脚本）以 MIT 协议发布，见 `LICENSE`。
> **该许可仅覆盖代码，不覆盖被收录的 Wiki 内容。**

把拓竹官方中文 Wiki（https://wiki.bambulab.com/zh/home）整站抓取、清洗、结构化后的本地知识库。
纯离线文件，不依赖任何第三方库；既可以直接给支持 MCP 的框架（如 AuroraBot）挂工具，也可以喂给平台型知识库，或在自写代码里用 SQLite 检索。

- **抓取时间**：2026-11-16（同日按官网重新抓取并重建）
- **规模**：3243 篇页面 / 20524 个语义段落 / 64 个系列 / 296 个分类节点 / 正文约 304 万字
- **失败页面**：9 篇（官方返回 404/403，属已删除或受限页面，清单见 `scripts/crawl_fail.txt`），其余全部入库
- **版本说明**：本版修复了旧版因 BeautifulSoup 版本差异导致的模板内文本丢失问题（标题、超链接文字、表格单元格文字曾大面积缺失），段落数由 6280 增至 20524，详见文末「修订记录」
- **内容范围**：H3C、H2、X1、P2S、A2L、R1、X2D、H2C、P1、A1、A1 mini、H2D、H2S、AMS 系列、软件（Bambu Studio / Handy / Suite）、耗材与配件、激光刀切、HMS 报错码、MakerWorld、经验分享等

## 文件清单

| 文件 | 说明 |
| --- | --- |
| `bambulab_wiki_zh.db` | SQLite 主库（91 MB），含中文全文索引，可直接 SQL 查询 |
| `bambulab_wiki_zh.jsonl` | 页面级 JSONL，一行一篇，含正文 Markdown/纯文本、图片、内链 |
| `bambulab_wiki_zh_chunks.jsonl` | 段落级 JSONL，一行一个语义块，最适合做向量化 / RAG 导入 |
| `bambulab_wiki_zh_index.csv` | 页面索引（标题、链接、系列、分类、更新时间、字数），Excel 可开 |
| `bambulab_wiki_zh_markdown.zip` | 3243 个 Markdown 文件，路径与页面 slug 一一对应，带 front-matter |
| `markdown/` | 同上，解压状态，方便直接指向目录上传 |
| `kb_search.py` | 检索模块 + 命令行工具（纯标准库） |
| `mcp_server.py` | MCP stdio 服务，给 AuroraBot 等框架注册工具用 |
| `scripts/` | 抓取 / 解析 / 勘误 / 建库脚本，可复现、可增量更新 |
| `stats.json` | 本次构建统计 |

## 数据库结构

```sql
pages(id, page_id, slug, url, title, description, series, series_title,
      section, section_title, category_path, kind, author, created_at,
      updated_at, tags, headings, char_count, word_count, image_count,
      link_count, images, internal_links, content_md, content_text)

categories(slug, title, url, level, parent_slug, page_count)

chunks(id, page_slug, page_title, heading, chunk_index, text)

pages_fts(title, category, body)   -- FTS5，汉字逐字分词，支持词组匹配
chunks_fts(title, heading, body)   -- FTS5，段落级
```

常用查询：

```sql
-- 某机型的所有故障排查页
SELECT title, url, updated_at FROM pages
WHERE series='x1' AND kind='troubleshooting' ORDER BY updated_at DESC;

-- 按北京时间最近更新的 20 篇
SELECT title, url, updated_at FROM pages ORDER BY updated_at DESC LIMIT 20;

-- 全文检索（建议用 kb_search.py，已处理中文分词）
SELECT p.title, p.url FROM pages_fts f JOIN pages p ON p.id=f.rowid
WHERE pages_fts MATCH '"A M S" AND "卡 料"' LIMIT 10;
```

## 接入方式

### 方式一：AuroraBot（MCP 工具，推荐）

AuroraBot 通过 MCP 给 Bot 挂工具，本包自带零依赖的 stdio MCP 服务，暴露两个工具：

- `search_bambu_wiki(query, top_k)`：按用户问题检索，返回标题、原文链接、片段
- `get_bambu_page(slug_or_title)`：取整页 Markdown，拿到完整排查步骤

在 AuroraBot 的 MCP 配置里加入（路径换成你机器上的实际路径）：

```json
{
  "mcpServers": {
    "bambulab-wiki-zh": {
      "command": "python3",
      "args": ["/path/to/bambulab_wiki_zh_kb/mcp_server.py"]
    }
  }
}
```

建议在 Bot 的人格/系统提示里补一句：*“回答拓竹打印机相关问题时，先调用 search_bambu_wiki 检索；需要完整步骤时再调用 get_bambu_page，并在回答里附上原文链接。”*

手工验证 MCP 是否正常：

```bash
printf '%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
 '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"search_bambu_wiki","arguments":{"query":"AMS 卡料","top_k":3}}}' \
 | python3 mcp_server.py
```

### 方式二：平台知识库（AstrBot / Dify / 扣子 / FastGPT 等）

- 支持 Markdown 上传的平台：把 `markdown/` 按系列分批上传（单批别超过平台文件数限制），或直接传 `bambulab_wiki_zh_markdown.zip`。
- 支持数据集/JSONL 的平台：导入 `bambulab_wiki_zh_chunks.jsonl`，字段 `text` 作为待向量化内容，`title` / `heading` / `url` 作为元数据。
- 切片已按页面小节切分：97.1% 的段落带小节标题，中位数约 120 字，P90 约 420 字。偏短是有意为之——同一页面内换小节就断开，避免把不同主题的步骤混在一块；如果平台对短块敏感，可在导入时把同页相邻块合并。

### 方式三：自写代码（SQLite 直连）

```python
import sys
sys.path.insert(0, "/path/to/bambulab_wiki_zh_kb")
import kb_search

results = kb_search.search("H2D 首层不粘", top_k=5)
for r in results:
    print(r["title"], r["url"], r["snippet"][:80])

page = kb_search.get_page("h2/troubleshooting/first-layer-printing-optimization-guide")
print(page["content_md"][:500])
```

命令行：

```bash
python3 kb_search.py "喷嘴堵塞" --top 5
python3 kb_search.py "AMS 2 Pro 烘干" --json
python3 kb_search.py --page x1/maintenance/replace-hotend
```

检索策略说明：

- 段落级 BM25，标题权重高于正文；先按“标题覆盖查询词的数量”排序，再用 BM25 细排。
- 自动识别 `H2D`、`X1`、`P2S`、`AMS` 等机型词，只作为加权项、不做硬性过滤——所以问“H2D 首层不粘”时，通用首层指南和 H2D 专属指南都能被召回。
- **意图分流**：库内 HMS 报错码页占 45%，标题模板化、关键词密度高，容易抢占正常问句的结果。因此当查询带操作意图（清理／更换／安装／维护／校准／设置等）时，对 HMS 页降权，让操作指南排前面；查询本身提到 HMS 或错误码时反向优先报错页；纯故障描述（如“AMS 卡料”）不降权——这时报错页往往正是对症的。
- 先清洗口语化问法（`怎么调`、`怎么办`、`如何解决` 等），命中不足时自动用二元组召回兜底，`喷嘴堵了怎么办` 这类口语也能找到“喷嘴堵塞”页面。
- 同一页面默认只返回 1 条，避免刷屏；纯符号或空查询直接返回空结果。
- 实测（24 条真实问句）：top3 内能找到可用页面的占 75%。剩余失败集中在口语与官方术语不一致的场景——库里叫“收缩”，用户问“尺寸不准”；库里叫“冷拔”，用户说“冷拉”。这类查询换个词就能命中，属于语义鸿沟而非索引缺陷。

中文查询不需要空格，`AMS 卡料`、`热床调平失败`、`HMS 0700-7000`、`X1 更换热端` 都能命中；英文关键词（如 `AMS HT drying`）会按词面匹配部分召回，但知识库正文是中文，英文长句效果有限。

## 数据质量说明

- 已剔除页面底部的“我们希望本指南能为您提供有用的信息…”等模板话术、纯图片占位表格、纯分隔符行。
- 正文保留原始 Markdown 结构（标题、列表、表格、图片链接），图片是官方 CDN 直链，机器人可直接发图。3243 页中 3199 页带可点击超链接，27543 张图片全部为官方 CDN 直链（抽样 10 张均 200 可访问）。
- 部分 `miniwiki` 快速排查页原始标题是路径，已用正文首句重写标题，归类为“HMS 快速排查（机型）”。
- HMS 报错码页面按机型各存一份（同一错误码在不同机型有细微差异），检索时优先按机型关键词过滤效果更好。

### 已知限制（无法通过抓取修复）

- **表格内容以图片承载**：约 560 页（正文 &gt; 800 字）的表格单元里放的是图片，原站不在 HTML 里放文字，因此 Markdown 里只剩 `| 〔图片〕 |`。典型如《拓竹 3D 打印机风扇介绍》——字符数 6307，可提取文字不足 300 字，风扇型号与电压参数全在图里。此类问题需视觉识别才能补全，本包不做处理，建议直接给官方原文链接。
- **75 页没有生成语义段落**：这些页面正文以链接列表为主（目录页、清单页），清洗后每段不足 40 字被过滤。页面本身仍在 `pages` 表和 Markdown 目录中，可用 `get_bambu_page` 取全文，只是不参与段落级检索。
- **Windows 下 Markdown 目录大小写折叠**：官网存在 `/zh/A1-mini/Midi` 与 `/zh/a1-mini/...` 这类大小写不同的路径，而 `pages.slug` 保留官网原始大小写。Windows 文件系统不区分大小写，会把它们折叠进同一个目录，导致用 slug 严格匹配文件路径时对不上（文件内容本身正确）。Linux/macOS 无此问题。

## 更新方法

```bash
cd scripts
python3 crawl_zh.py     # 增量抓取，已缓存的页面会跳过
python3 parse_zh.py     # 重新解析
python3 fix_errata.py   # 应用人工核定的勘误（官网原文的坏字符）
python3 build_db.py     # 重建数据库和导出文件
```

首次全量抓取约 8 分钟（8 并发），解析 30 秒，建库 30 秒。建议每月跑一次；Wiki 更新频繁，HMS 码和固件相关页面变动较多。

`fix_errata.py` 里维护着一张勘误表，每条形如 `(页面路径, 原文, 修正后, 判定依据)`。目前只有 4 条，全部集中在 `h3c/troubleshooting/hmscode/0700_2000_0002_0020`——该页在官网发布时就带 11 个 U+FFFD 替换符（原始 HTML 解码正常，说明是官方编辑时的输入损坏，不是抓取造成），已按同页上下文修正为「导致」「槽」「解除」等。发现新的同类问题可按同样格式追加。

## 修订记录

### 2026-11-16 修订（对照官网核对后重建）

对全站 3243 页重新抓取、重新解析、重建全部产物。修正的问题：

1. **模板内文本丢失（最严重）**。旧版解析用 `element.get_text()` 取文本，而 BeautifulSoup 4.13+ 会把 `<template>` 内的文本标记为 `TemplateString`，默认不被 `get_text()` 收集。后果：所有标题、超链接文字、表格单元格文字为空——旧版 `pages.headings` 3243 页全空，`content_md` 里真正的超链接只剩 17 页（0.5%），93 页留下「请参考： 。」这种断链痕迹，3306 个列表项只剩一个 `-`。本版对取文本统一走 `parse_zh.text_of()`，显式指定 `types=(NavigableString, TemplateString)`，并兼容旧版 bs4。
2. **段落从 6280 增至 20524**。标题恢复后才能按小节切分，heading 覆盖率 0% → 97.1%，检索结果开始带小节上下文。
3. **正文缺字**。旧版 4 页 `content_md` 为空（其中含《全部公开的链接》31571 字），现已全部补齐；`content_md` 空页数为 0。
4. **乱码**。旧版 1 页 2 处 U+FFFD，实际官网原文有 11 处，已按上下文全部修正，见 `scripts/fix_errata.py`。
5. **检索排序偏置**。新增意图分流，解决 HMS 报错页抢占正常问句的问题（「热端堵头怎么清理」原先 top3 全是散热片过热的报错页，现在给出《H3C 热端堵塞清理指南》等操作指南）。
6. **Markdown 文件路径**。改为与页面 slug 一一对应（原先用双下划线扁平化，与 slug 不一致 3077 项）。
7. **stats.json 计数**。`categories` 改为数据库实际行数（296），此前报的是分类键数量（306）。

经核对后确认**不构成问题**、未做改动的项：

- 官网更新页 `/zh/new-and-updates` 上有 19 个链接指向已失效路径（含 6 个 `/zh/staging/` 草稿路径、`/zh/h2/trubleshooting/` 这类官网拼写错误），逐一访问均返回 404。本包未收录它们是正确的，不存在遗漏。
- 9 篇抓取失败页面经复核确为官网 404/403（AMS 3P 系列 5 篇、2 篇 HMS 码、1 篇 x2d 耗材页、2 篇无权访问），非抓取异常。

## 版权与边界

内容版权归 Bambu Lab 所有，本包仅做格式转换与本地索引，供个人学习与内部机器人问答使用；对外答复请附官方原文链接，并以官方页面为准。

- **不主张权利**：本仓库对所有 Wiki 正文、图片、术语释义不具备著作权，也不授予他人任何使用许可。
- **非官方**：与 Bambu Lab 无关联、未获授权、不代表官方立场。内容可能滞后，技术判断请以官网为准。
- **可删除**：权利人提出异议后，会立即删除相关内容或整仓，无需另行协商。
- **不建议再分发**：如需在自家产品中使用这些内容，请先向 Bambu Lab 取得授权，或直接调用官网。
- **抓取频率**：本项目只在需要修复数据缺陷时做一次性重建，不做持续轮询，请求带 UA 标识并限制并发。
