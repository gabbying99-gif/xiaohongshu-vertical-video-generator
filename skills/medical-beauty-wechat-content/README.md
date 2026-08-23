# Medical Beauty WeChat Content Skill

这个仓库用于保存 `medical-beauty-wechat-content` skill。

## 这个 skill 是做什么的

`medical-beauty-wechat-content` 是一个医美公众号内容工作流 skill，用来帮助医美渠道类公众号做：

- 公众号选题判断
- 小红书 / 视频号 / 公众号搜索趋势复盘
- 医美产品文章草稿
- 产品区别、适合人群、使用思路、注意事项整理
- 水光、刷酸、术后修复、填充、再生材料类内容
- 私域引流窗口和免责声明
- 文章发布后数据复盘
- 下一篇选题建议

它适合的账号类型：

- 医美渠道产品公众号
- 水光 / 刷酸 / 院线护肤品内容号
- 服务个人自用、小代理、美容院、工作室、机构工作人员的私域引流号

## 文件结构

```text
medical-beauty-wechat-content/
  SKILL.md
  agents/
    openai.yaml
  references/
    style-and-components.md
    topic-system.md
    workspace-workflow.md
```

## 给 WorkBuddy 的调用方式

如果 WorkBuddy 支持读取本地 skill，请把 `medical-beauty-wechat-content` 整个文件夹放进 WorkBuddy 的 skills 目录。

之后可以这样下达指令：

```text
用 medical-beauty-wechat-content，帮我判断【产品名/选题】最近值不值得写。
请按：小红书/视频号/公众号搜索、机构端是否在推、用户是否有拿货需求、风险和转化价值分析。
```

```text
用 medical-beauty-wechat-content，根据我发的素材，写一篇公众号草稿。
要求：精简、有实质内容、符合我之前风格，包含产品详情、区别、使用思路、注意事项、引流窗口和免责声明。
```

```text
用 medical-beauty-wechat-content，帮我复盘这篇公众号。
数据：阅读量、搜一搜占比、分享、加微信人数、问价人数、成交人数。
请判断为什么有/没有流量，下一篇应该追什么选题。
```

```text
用 medical-beauty-wechat-content，帮我做本周公众号选题。
重点：水光、刷酸、术后修复、再生材料、拿货前先看、真假防伪、产品对比。
```

## 最常用任务模板

### 1. 判断选题值不值得写

```text
用 medical-beauty-wechat-content，帮我判断【产品名】最近值不值得写。
请按：
1. 小红书/视频号/公众号搜索
2. 机构端是否在推
3. 用户是否有拿货需求
4. 风险和合规注意
5. 转化价值
6. 下一篇建议标题
```

### 2. 写公众号文章

```text
用 medical-beauty-wechat-content，帮我写一篇公众号：
主题：【主题】
素材：【粘贴资料/链接/图片说明】
要求：
- 不要太长
- 不要只写适合人群
- 要写产品详情、区别、使用思路、搭配、注意事项
- 结尾加引流窗口和免责声明
- 风格要像我之前的公众号，大白话、实用、渠道视角
```

### 3. 复盘公众号

```text
用 medical-beauty-wechat-content，帮我复盘这篇公众号。
文章：【标题/链接/文件】
数据：
- 阅读量：
- 搜一搜占比：
- 分享：
- 加微信人数：
- 问价人数：
- 成交人数：
请判断：
1. 为什么有/没有流量
2. 流量有没有商业价值
3. 为什么转化弱/强
4. 下一篇应该追什么选题
5. 引流窗口怎么改
```

## 注意

医美内容涉及较高合规风险。使用这个 skill 时，公开文章里不要写具体注射层次、剂量、复溶配比、自我操作教程，也不要承诺绝对效果或零风险。涉及医疗美容操作的内容，应统一引导到正规医疗机构和专业医生判断。

