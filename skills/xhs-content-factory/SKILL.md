---
name: xhs-content-factory
description: "Use this skill when the user wants Codex to operate their Xiaohongshu/short-video content factory in Feishu Base: ingest movie or travel life-material into 00, archive Xiaohongshu/Douyin benchmark videos into 01, download video/subtitle/cover assets from shared links when available, analyze and split benchmark videos into 02, generate original scripts in 03, create shooting/material prep in 04, create editing execution tasks in 05, or review published performance. Trigger on Chinese requests such as 入库这个对标视频, 下载这个小红书视频, 补逐字稿和标签, 只入01, 入01并拉片, 生成仿写稿, 流转到03, 拆成拍摄清单, 更新复盘, 小红书内容工厂, or 生命力素材池."
---

# XHS Content Factory

## Overview

Use the user's Feishu Base as a Xiaohongshu/short-video content operating system. Keep two sources separate:

- Personal life material goes to `00｜生命力素材池`; currently only movie and travel material belong here.
- External benchmark content from Xiaohongshu or Douyin goes to `01｜对标视频库`, then optionally to downstream production tables.

Do not hard-code private Base URLs or tokens in public artifacts. If no Base URL/token is available in the task context, ask the user for the Feishu Base link before writing.

## Required Base Handling

Use the `lark-base` workflow for all Feishu Base operations:

1. Resolve a user-provided Base URL with `lark-cli.cmd base +url-resolve --url "<url>" --as user`, or use a known `base_token` from the current conversation.
2. Read real table and field structures before writing: `+table-list`, then `+field-list`.
3. Write only writable storage fields. Do not write attachment, auto-number, formula, lookup, created/updated system fields as normal cell values.
4. Use `--as user` by default.
5. For complex JSON on Windows, write a temporary JSON file and pass `--json @file.json`; delete the temporary file after success.
6. Verify writes by reading the created/updated record back.

Read `references/factory-workflows.md` when deciding where content should go or how to map fields.

## Link Asset Handling

When the user provides a Xiaohongshu or Douyin benchmark link, attempt to resolve and download available source assets before treating transcript, tags, cover, duration, or metrics as missing.

Use `D:\Codex\xhs-content-assets` as the default local asset root on this user's Windows machine. For Xiaohongshu web links, first fetch the shared page with a browser-like user agent and check whether a real subtitle/transcript source is exposed (`.srt`, `subtitles`, or equivalent). Report transcript availability before relying on the transcript field. Then parse available metadata from HTML/JSON-LD/state payloads: title, author, description, tags, interaction counts, duration, video URL, cover URL, and subtitle URLs. Download available video/subtitle/cover files into `D:\Codex\xhs-content-assets\downloads\<platform>_<work_id>\`, then upload those files to matching Base attachment fields when the table has them. If D: is unavailable, fall back to the workspace `downloads/` folder and report that fallback. If parsing or downloading fails because of login, anti-bot, expired links, or network limits, archive the benchmark with known fields and ask the user for the video file, screenshots, transcript, or a fresh link.

## Routing

Route user requests by intent:

- `只入01`: create one record in `01｜对标视频库`; do not create `02`, `03`, `04`, or `05` records.
- `入01并拉片`: create/update `01`, then split shots into `02｜对标拉片`.
- `生成我的仿写稿`: create/update `01`; optionally use `02`; write adapted title/body/tags into `01` and/or create a `03｜口播稿生产` project if the user asks to move into production.
- `入00` or movie/travel life material: create one record in `00｜生命力素材池`.
- `流转到03`: create an original project in `03｜口播稿生产`, linked to either `00` or `01`.
- `拆成拍摄清单`: create shot/material tasks in `04｜拍摄与素材准备`.
- `拆成剪辑清单` or `ChatCut`: create editing execution tasks in `05｜最终剪辑执行`.
- `复盘`: update `03` with publish data and conclusion; do not invent missing metrics.

If a request is ambiguous, choose the safest minimal action and state what was not done.

## Content Principles

- Preserve raw user material. Put polishing, analysis, and adapted drafts into separate fields.
- Do not invent platform metrics, transcript text, screenshots, or video duration. First try to extract/download them from the source link; if the link is inaccessible, ask for the video file, screenshots, transcript, or data screenshot.
- Keep the user's account positioning in mind: a lively, high-empathy creator account. Do not force every life-material item into a technical tutorial.
- For `00`, keep the source limited to movie and travel unless the user explicitly expands the system.
- For `01`, treat content as external benchmark material only; it is not the user's own life material.

## Output Back To User

After writing to Base, report:

- Target table name
- Record ID
- Key fields written
- What was intentionally not done
- Missing source material that would improve later analysis
