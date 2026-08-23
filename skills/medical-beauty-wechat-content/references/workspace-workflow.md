# Workspace Workflow

Use this local workspace convention for the user's WeChat Official Account work.

Base directory:

```text
D:\AI自媒体\内容工厂\公众号
```

## Folder Rules

### 公众号选题01

Save co-planned topics, weekly plans, keyword pools, competitor analysis, viral-post reviews, and product-worth-writing judgments.

Typical files:

- Weekly topic plans
- Xiaohongshu/Weibo/WeChat trend summaries
- Product priority scoring
- Competitor title/content breakdowns
- Post-performance reviews

### 公众号素材02

Save user-provided raw materials and organized material notes.

Typical materials:

- Product photos
- Customer feedback screenshots
- Order screenshots
- Comparison charts
- Brand/product documents
- Reference article text
- Weibo/Xiaohongshu/WeChat screenshots

When images are provided as file paths, keep the original file path in the material note. Do not move user source images unless the user explicitly asks. Create a same-topic markdown note describing what each image is useful for.

### 公众号草稿03

Save article drafts, shortened drafts, revised drafts, confirmed final drafts, and post-publication review notes.

Recommended naming:

```text
YYYY-MM-DD_产品名_标题简写.md
YYYY-MM-DD_产品名_标题简写_终稿.md
```

Example:

```text
2026-07-23_科邦达水杨酸_夏天油皮刷酸怎么选.md
```

## User Command Patterns

Topic planning:

```text
用公众号工作流，帮我做本周选题。
重点：水光、刷酸、术后修复。
目标：个人自用 + 小代理 + 美容院。
请保存到公众号/公众号选题01。
```

Material organization:

```text
这些是科邦达水杨酸的素材，帮我整理到公众号/公众号素材02。
用途：准备写一篇夏天油皮刷酸文章。
```

Draft writing:

```text
用公众号工作流，根据公众号素材02里的科邦达素材，写一篇公众号草稿。
标题：夏天油皮刷酸怎么选？科邦达水杨酸面膜适合人群和使用方法
要求：精简、有实质内容、结尾放联系方式和声明。
写好保存到公众号/公众号草稿03。
```

Draft revision:

```text
帮我把公众号草稿03里的科邦达这篇再精简一点。
要求：减少铺垫，保留适合人群、用法、搭配、注意事项。
```

Final confirmation:

```text
这篇没问题，保存为终稿。
后面我自己复制到公众号后台。
```

## Save Behavior

- Create folders if missing.
- Do not overwrite existing drafts unless the user explicitly says to overwrite.
- When revising, save a new version or final version.
- Every draft must include title, body, image placement notes, lead/contact window, keyword, and disclaimer.
- Public drafts should not expose wholesale price tiers or dropshipping rules. Use need-based screening first.

