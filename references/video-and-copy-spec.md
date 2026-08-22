# Video and Publish-Copy Specification

Read this file before rendering the MP4 or drafting its matching TXT.

## Visual layout

- Canvas: `1080x1920`, `9:16`, 30 fps.
- Use a stable hierarchy: header, source-video area, subtitle area, then optional compact vocabulary area.
- Keep the header warm and clean. Use a dark bold Chinese title and a high-contrast episode label.
- Scale a horizontal source proportionally. Crop only when the subject remains safe; otherwise use fit-with-background composition.
- Keep essential text within approximate safe margins: 80 px left, 180 px right, 120 px top, and 260 px bottom. Adjust after previewing because platform UI may vary.
- Use no more than two subtitle lines per language at once when possible.

## Subtitle treatment

- Include every subtitle cue overlapping the final clip.
- Keep source-language spelling, accents, and punctuation faithful.
- Translate for natural learner comprehension rather than literal word order.
- Remove punctuation from Chinese video-overlay text by default, replacing punctuation with spaces and collapsing whitespace.
- Keep normal punctuation in the TXT when it improves readability.

## Learning content

- Use 6-8 vocabulary items by default for a 60-120 second learning clip.
- Include only words, chunks, grammar, or cultural notes demonstrably supported by the selected clip.
- Prefer useful chunks over isolated rare words.
- Keep cards short enough to read on a phone without crowding subtitles.

## File naming

- Default output root: `D:\双语\<source-video-id>_小红书竖屏视频\`.
- MP4: `第XX期_<主题>_<系列名>_小红书竖屏短视频.mp4`
- TXT: `第XX期_<主题>_<系列名>_小红书发布文案.txt`
- Preview: `previews/第XX期_<主题>_opening.png` and `previews/第XX期_<主题>_midpoint.png`
- Temporary render assets may use technical names, but final deliverables must use readable names.

## TXT template

```text
本期内容有个非常地道、也非常生活化的表达，你听出来了吗？

对！就是 <核心表达> 这个西语表达～

在西语里，<解释核心词或表达的意思>。如果你<列出真实生活场景>，就可以直接说：

<核心表达>
<自然中文释义>

视频里博主<交代真实语境>，所以她/他说：

<视频中的完整西语例句>
<自然中文翻译>

📌重点词汇：
🔸<核心表达> <中文释义>
🔸<词汇或词块 2> <中文释义>
🔸<词汇或词块 3> <中文释义>
🔸<词汇或词块 4> <中文释义>
🔸<词汇或词块 5> <中文释义>

📌 点赞+收藏，让表达一点点积累，别让好内容从手里溜走～

#vlog #西班牙语 #西语 #西班牙语学习 #西语学习 #西语口语 #西班牙语入门 #西班牙语口语 #西语入门 #油管博主 #西语听力 #西语日常表达 #<主题标签>
```

## Copy quality bar

- Make the copy understandable without production context.
- Match title, body, hashtags, language, learner level, and episode topic to the finished MP4.
- Keep the tone conversational and lightly enthusiastic. Use `对！就是……～` and emoji section markers naturally, not mechanically more than needed.
- Choose one central expression that genuinely appears in the clip. Do not force every episode into a grammar explanation when a concrete noun contrast or scene phrase is stronger.
- Preserve the speaker's actual context. Do not invent a purchase, trip, decision, reason, or quotation.
- Avoid clickbait, medical/financial promises, unverifiable superlatives, and fabricated personal experience.
- Do not expose source paths, commands, render settings, manifest data, or workflow notes.
- End with tags on a single line unless the user requests another format.
