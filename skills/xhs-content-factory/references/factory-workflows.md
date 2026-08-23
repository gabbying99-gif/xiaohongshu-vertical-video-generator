# Xiaohongshu Content Factory Workflows

## Table Roles

Use these table names, resolving exact IDs from the live Base before writing:

- `00｜生命力素材池`: personal source material from movies and travel only.
- `01｜对标视频库`: external benchmark videos/posts from Xiaohongshu or Douyin.
- `02｜对标拉片`: shot-by-shot breakdown of benchmark content.
- `03｜口播稿生产`: original production project hub.
- `04｜拍摄与素材准备`: shot-level recording, B-roll, screen recording, prompt, and material preparation.
- `05｜最终剪辑执行`: editing timeline, subtitles, ChatCut instructions, and delivery tasks.

Do not mix personal material and external benchmarks.

## User Command Patterns

### Personal life material

Use when the user says:

- `把这段电影/旅行素材入00：...`
- `把00里《素材标题》扩写成小红书图文`
- `把00里《素材标题》流转到03，做成一条口播/图文选题`

Write to `00｜生命力素材池`:

- `素材标题`
- `来源`: `电影` or `旅行`
- `发生/观看日期` when known
- `原始碎片`
- `当时的情绪`
- `核心主题`
- `适合形式`
- `内容状态`
- `初稿/原文`, `我建议的标题`, `成稿正文`, `封面文案`, `发布标签` when produced
- `关联生产项目` only after creating a `03` project

### Benchmark archive

Use when the user says:

- `帮我入库这个对标视频：链接。目标：只入01`
- `帮我入库这个对标视频：链接。目标：入01并拉片`
- `帮我入库这个对标视频：链接。目标：生成我的仿写稿`
- `这是一个素材/对标，帮我判断放哪张表，并写入飞书`

For `只入01`, write only to `01｜对标视频库`.

Before writing a benchmark link, try to resolve the source page and download available assets:

- Fetch the shared page with a browser-like user agent and a referer from the source platform.
- Before downloading other assets, first determine whether the page exposes a real transcript/subtitle source, such as `.srt`, `subtitles`, or an equivalent platform subtitle field. Report `可抓取逐字稿：是/否` in the working summary.
- For Xiaohongshu, inspect meta tags, JSON-LD, and embedded state payloads for `og:video`, `contentUrl`, `mediaV2`, `master_url`, `subtitles`, `tagList`, `desc`, `interactInfo`, `duration`, `time`, and cover image URLs.
- Save downloaded files under `D:\Codex\xhs-content-assets\downloads\xhs_<work_id>\` or `D:\Codex\xhs-content-assets\downloads\douyin_<work_id>\` by default.
- If D: is unavailable, save under the current workspace `downloads/` folder and explicitly report the fallback path.
- Prefer stable filenames: `video.mp4`, `cover.jpg` or `cover.png`, `audio_16k.wav`, `subtitle_zh-CN.srt`, `subtitle_en-US.srt`, `transcript.txt`, and `transcript_segments.json`.
- Upload downloaded videos to the `视频` attachment field when present.
- Convert subtitle files into plain readable text and save `transcript.txt`; upload `transcript.txt` to the `逐字稿文件` attachment field when present. Keep `.srt` files locally as source files, but do not rely on `.srt` as the only Base attachment because Feishu may not preview it.
- Upload cover images to the `封面` attachment field when present.
- Convert subtitle files into plain readable text and write it into `逐字稿`.
- If no real subtitle/transcript source is exposed but `video.mp4` is available, use a local ASR fallback: extract `audio_16k.wav` with ffmpeg, transcribe the audio with Whisper/faster-whisper or another available ASR tool, save `transcript.txt` and `transcript_segments.json`, upload `transcript.txt` to `逐字稿文件`, and write the transcript into `逐字稿` with an `ASR逐字稿` marker. Prefer this skill's `scripts/xhs_asr_transcribe.py <asset-dir> [model-size]` helper when available. If ASR tooling is missing, install or create it under `D:\Codex\tools\xhs-asr` when the user has allowed tool setup.
- If neither platform subtitles nor ASR are available, leave `逐字稿` and `逐字稿文件` blank; do not infer a transcript from title, description, comments, or visual guesses.
- Keep original platform hashtags in `正文`. Write `标签` as useful content-factory retrieval tags, such as topic, emotion, format, use case, and account-fit tags. Do not use irrelevant platform tags like `英文` as the only tagging strategy unless they are genuinely useful for later creation.
- Write real metrics, duration, publish time, description, and interaction collection time only when found in the page/source data.

Useful `01` fields:

- `标题`
- `平台`: `小红书` or `抖音`
- `对标账号`
- `原始链接`
- `作品ID`
- `发布时间`
- `标签`
- `正文`
- `逐字稿`
- `时长（秒）`
- `点赞数`, `收藏数`, `分享数`, `评论数`
- `互动数据采集时间`
- `已创建口播记录`: usually `false`

Leave unknown fields blank. Never invent metrics.

If the source page exposes only partial data, write the partial data and report what was not captured. If a download fails after retrying, keep the record and tell the user exactly what file is missing.

### Benchmark shot breakdown

For `入01并拉片`, create `02｜对标拉片` records after the `01` record exists.

Useful `02` fields:

- `来源对标视频`
- `镜号`
- `时间码`
- `时长（秒）`
- `画面类型`
- `素材形态`
- `画面描述`
- `运镜与操作`
- `对标口播`
- `一比一复刻要求`
- `状态`

### Original production project

For `流转到03` or `生成我的仿写稿`, create/update `03｜口播稿生产`.

Useful `03` fields:

- `项目名称`
- `视频主题`
- `目标平台`
- `选题Brief`
- `对标逐字稿`
- `改编的口播稿`
- `人工修改稿`
- `发布标题`
- `发布正文`
- `发布标签`
- `生产状态`
- `当前模块`
- Link to `关联对标视频` or `生命力素材来源`

### Shooting and editing

For `拆成拍摄清单`, create `04｜拍摄与素材准备` records linked to `03`.

For `拆成剪辑清单`, create `05｜最终剪辑执行` records linked to `03` and/or `04`.

Keep each row as one actionable shot. Prefer compact, operational text over essay-like notes.

## Minimum Ingestion Rules

When a Xiaohongshu link cannot be accessed directly, still archive the benchmark if the user provided enough metadata:

- Title from the share text
- Creator from the share text
- Platform inferred from URL
- Raw link
- Work ID parsed from the URL path
- Share code or raw share text stored in `正文`

Tell the user that transcript, metrics, cover, and video assets were not captured only after attempting source-link extraction/download. Do not skip the download attempt for video benchmarks unless the user explicitly says not to download.

## Response Template

After a write:

```text
已写入到 `<table name>`。

- 记录 ID：`<record_id>`
- 写入字段：...
- 未处理：...
- 后续如果要继续，可以说：...
```
