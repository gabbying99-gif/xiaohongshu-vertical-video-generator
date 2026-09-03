---
name: xiaohongshu-vertical-video-generator
description: Create a 9:16 Xiaohongshu vertical short video and a matching Xiaohongshu publish-copy TXT file from a source video, selected clip, subtitles, transcript, or language-learning episode. Use when the user asks to 制作小红书竖屏短视频、生成小红书视频成片、把横屏素材改成小红书视频、同步生成小红书发布文案、生成配套标题正文话题标签 TXT, or package an existing learning clip for Xiaohongshu. Supports Spanish and other languages; does not publish to Xiaohongshu unless the user explicitly asks and a publishing tool is available.
---

# 小红书竖屏视频生成 Skill

Turn one source into two synchronized deliverables: a mobile-ready vertical MP4 and a UTF-8 Xiaohongshu publish-copy TXT.

## Inputs and defaults

- Accept a local source video, a YouTube/video URL, or an existing clip plus timed subtitles/transcript.
- Reuse an existing episode number, topic, clip range, translations, and vocabulary when supplied.
- When given a long source, select a coherent 60-120 second segment by default. Prefer clear speech, a complete micro-topic, and strong opening value.
- When one source contains multiple strong, non-overlapping micro-topics, create 2-3 independent episodes. Give each episode its own clip range, title, subtitles, vocabulary, MP4, and publish-copy TXT; do not split merely to reach a target count.
- For language-learning content, preserve the complete subtitle sequence within the selected range and use 6-8 clip-supported vocabulary items.
- When the original video shows the protagonist speaking on camera or keeps the source spoken audio, subtitles must follow the original SRT verbatim for the spoken language, then add a natural Chinese translation. Do not replace spoken subtitles with rewritten, condensed, or teaching-summary sentences.
- Hard rule for talking-head/original-audio clips: the selected video source start and the selected subtitle source start must be the same source timestamp. Never shift subtitles by guessing from the rendered clip alone. If the clip starts at source 0:00, include the SRT cues from source 0:00; if the clip starts at source 12.06, include the SRT cues from source 12.06.
- Save deliverables under `D:\双语\<source-video-id>_小红书竖屏视频\` by default. For example, source `nZ72qntioZI` uses `D:\双语\nZ72qntioZI_小红书竖屏视频\`. Use another location only when the user explicitly requests it.
- Ask only for information that cannot be inferred safely. Do not require Feishu documents or knowledge-base configuration.

## Workflow

1. Inspect the source and resolve title, duration, dimensions, audio, language, subtitle tracks, and existing episode metadata.
2. Acquire or align timestamped subtitles. Prefer human subtitles, then automatic captions, then ASR. Translate naturally when bilingual subtitles are needed.
3. Select or reuse the clip. Record exact start and end times and include every subtitle row that overlaps the range.
4. Before rendering, run an alignment check for talking-head/original-audio clips:
   - Compare the first visible/sounded sentence in the clip with the first subtitle cue.
   - Compare at least one midpoint cue and one ending cue against the original SRT timing.
   - Confirm the target-language text is copied cue by cue from the original SRT, not rewritten.
   - If any check fails, adjust the clip start/end or subtitle source start/end before rendering.
5. Read [references/video-and-copy-spec.md](references/video-and-copy-spec.md) before composing or rendering.
6. Render the 9:16 MP4 with readable mobile typography, bilingual subtitles when applicable, and compact learning points or vocabulary.
7. Generate the matching publish copy from the actual finished clip; do not draft from unrelated source-video content.
8. Save the MP4 and TXT side by side with the same basename.
9. Validate both deliverables and fix blocking issues before reporting completion.

## Required deliverables

Use a readable Chinese basename:

```text
第XX期_<主题>_<系列名>_小红书竖屏短视频.mp4
第XX期_<主题>_<系列名>_小红书发布文案.txt
```

Use two-digit episode numbers. Keep the topic concise, Chinese-readable, and punctuation-free. If no series name exists, use a short content category such as `西语学习` or omit that component consistently.

The TXT must be UTF-8 plain text and contain paste-ready copy in this order:

```text
<用提问制造互动感，并提示本期有一个地道生活表达>

<直接揭晓核心西语表达，并用“就是……这个西语表达～”建立口语感>

<解释表达的含义和适用生活场景>

<引用视频里的完整西语例句>
<自然中文翻译>

📌重点词汇：
🔸<表达> <中文释义>
...

📌 点赞+收藏，让表达一点点积累，别让好内容从手里溜走～

#vlog #西班牙语 ...
```

Do not add internal production notes, local paths, timestamps, or unsupported claims to the publish copy.

## Rendering rules

- Default canvas: 1080x1920, 9:16, 30 fps.
- Preserve source aspect ratio. Never stretch faces or scenery.
- Put the series title and episode label in a stable header zone.
- Keep the source video visually dominant. For 16:9 sources, fit or crop deliberately; use a designed background rather than distortion.
- Put subtitles in a high-contrast band or safe overlay region. Keep target-language text above natural Chinese translation.
- For talking-head/original-audio clips, keep the target-language subtitle text and timing from the original SRT cue by cue. The Chinese line may be translated naturally, but the target-language line cannot be paraphrased or merged.
- For talking-head/original-audio clips, do not compress subtitle timing to make text appear faster, and do not stretch timing to make text appear slower. Preserve original SRT cue timing relative to the selected source start. If a cue is too long or visually awkward, split it only when the split still follows the spoken rhythm and preserves all original words in order.
- If a rendered preview shows the protagonist saying one sentence while the subtitle shows another sentence, treat it as a blocking failure. Do not report completion until the MP4 has been regenerated.
- For Chinese subtitle overlays, remove punctuation by default and collapse repeated whitespace.
- Keep vocabulary/learning cards compact and supported by the clip.
- Respect mobile safe areas; keep essential text away from the top, bottom, and right-side interaction controls.
- Preserve audio, avoid clipping, and keep output duration aligned to the selected clip within normal encoding tolerance.

Prefer deterministic local rendering with `ffmpeg`. Use ASS subtitles when supported; otherwise render transparent text overlays and compose them with `ffmpeg`.

## Publish-copy rules

- Follow the reference copy pattern in `references/video-and-copy-spec.md`; mirror its rhythm and section order without copying topic-specific wording.
- Open with `本期内容有个非常地道、也非常生活化的表达，你听出来了吗？` or a close topic-specific variation.
- Reveal one central expression conversationally, explain its meaning, and name realistic situations where it is useful.
- Quote a complete Spanish example actually spoken in the clip, followed by a natural Chinese translation.
- Add a `📌重点词汇：` block with 5-7 `🔸` items drawn from the clip.
- End with the preferred `📌 点赞+收藏...` call to action, then place hashtags on one final line.
- For language learning, preserve accents and inverted punctuation in examples; ensure every example appears in the clip.
- Default to the user's stable Spanish-learning tag set, then add up to 2 topic-specific tags. Keep `#vlog #西班牙语 #西语 #西班牙语学习 #西语学习 #西语口语 #西班牙语入门 #西班牙语口语 #西语入门 #油管博主 #西语听力 #西语日常表达` unless a tag is clearly inappropriate.
- Do not include `#小红书` merely as filler.

## Validation

- Use `ffprobe` to confirm 1080x1920, duration, frame rate, and an audio stream.
- Extract at least three preview frames: near the opening, near the midpoint, and near the ending.
- Inspect previews for stretching, cropping errors, unreadable text, collisions, subtitle cutoff, and vocabulary overlap.
- For talking-head/original-audio clips, inspect those preview frames for mouth/audio/subtitle agreement: the opening must match the first spoken sentence, the midpoint must match the active cue, and the ending must match the final spoken sentence.
- Confirm all overlapping subtitle rows appear and all teaching points are supported by the clip.
- Confirm the first SRT cue included in ASS equals the first cue that overlaps the selected source timestamp. A missing opening cue, such as dropping an intro/welcome sentence, is a blocking failure.
- Confirm MP4 and TXT share the intended episode/topic identity.
- Confirm the TXT opens as UTF-8, follows the hook/explanation/example/vocabulary/CTA/hashtags order, and is ready to paste without cleanup.
- Treat missing audio, subtitle omissions, visual overlap, unsupported vocabulary, mismatched copy, or a missing TXT as blocking failures.

## Scope boundary

Create local deliverables only by default. Do not create Feishu documents, Wiki/Base records, covers, or study documents unless separately requested. Do not post to Xiaohongshu without explicit user authorization.

## GitHub sync boundary

- Only update or push the GitHub repository when the user explicitly asks to update/save/upload a skill.
- Routine video generation, subtitle repair, article drafting, or local cleanup must not push to GitHub.
- When a skill is updated and the user asks to sync it, push only the skill-related files that were intentionally changed.
