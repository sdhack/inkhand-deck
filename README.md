# inkhand-deck

> 当前版本：**1.1.2**（2026-08-27）· MIT · [sdhack/inkhand-deck](https://github.com/sdhack/inkhand-deck)

墨黑手绘风（初版）· 中文技术图文 / 长文配图技能（WorkBuddy Agent Skill）。

原创 IP **「墨仔（Mozai）」** —— 一滴在纸上活过来的墨。每页作为"演员"操作图表隐喻（搬运 / 漏斗 / 拉线 / 警示 / 记录 / 探头），死板、冷静、有点荒诞，**绝不卖萌、绝不吉祥物化**。

## 特性

- **墨黑风格锁（初版）**：暖白纸 `#FBFAF5` + 墨黑线 `#1A1A1A` + 墨黑身体 `#1A1A1A` + pastel 标签，非死黑 `#000000`
- **墨仔每页恰好 1 个**（HARD RULE），顶部绿芽签名标记始终可见
- **7 类页面原型**：封面 / 左右对比 / 主隐喻 / 机制环 / 矩阵表 / 警示 / 落点
- **两种生产模式**：
  - ☁️ 云端生图（ImageGen / nanobanana pro / Gemini）：用 `references/mozai-character.md` 的 prompt block
  - 🖥️ 本地矢量（无水印、不花 credits）：墨仔 `<symbol>` + 无头 Chrome 渲染 SVG，配色 100% 锁死

## 安装

```bash
# 方式一：克隆到 WorkBuddy 用户技能目录
git clone https://github.com/sdhack/inkhand-deck.git \
  "$HOME/.workbuddy/skills/inkhand-deck"

# 方式二：WorkBuddy 对话内用 /skill 引用本地路径，或用 @-zip 安装
```

## 文件结构

```
inkhand-deck/
├── SKILL.md                       # 技能入口与触发词
├── references/
│   ├── mozai-character.md         # 墨仔角色规范 + 生图 prompt block ★
│   ├── mozai-prompt.md            # 生图提示词速查（完整版/精简版/全局锁）★
│   ├── visual-dna-fusion.md       # 墨黑手绘风 DNA 锁
│   ├── slide-archetypes.md        # 7 类页面原型
│   ├── prompt-patterns-fusion.md  # 生图 prompt 模板 + ImageGen 撞名修复经验
│   └── qa-checklist.md            # 出图 QA 清单
├── CHANGELOG.md                   # 版本变更记录
└── assets/
    ├── mozai-character-sheet.png  # 墨仔角色参考图（肢体完整·表情完整人物卡，母版 image-to-image 版，带云端水印）
    ├── mozai-mother-version.png    # 墨黑初版视觉金标准（母版 demo 页，对照用）
    └── theme-tokens-fusion.json   # 主题色 token
```

## 墨仔生图提示词

直接复制 `references/mozai-prompt.md` 的「完整版 Prompt Block」（开箱即用，含两条 HARD RULE），或 `references/mozai-character.md` 末尾的 `Generation Prompt Block` 到任意生图工具即可（每页仅 1 个墨仔 / 非死黑 #000000，墨黑 #1A1A1A）。

## 许可

MIT © 2026 sdhack
