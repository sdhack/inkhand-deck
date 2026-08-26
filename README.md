# inkhand-deck

墨蓝手绘风 · 中文技术图文 / 长文配图技能（WorkBuddy Agent Skill）。

原创 IP **「墨仔（Mozai）」** —— 一滴在纸上活过来的墨。每页作为"演员"操作图表隐喻（搬运 / 漏斗 / 拉线 / 警示 / 记录 / 探头），死板、冷静、有点荒诞，**绝不卖萌、绝不吉祥物化**。

## 特性

- **墨蓝去黑风格锁**：暖白纸 `#FBFAF5` + 深蓝灰线 `#34465E` + 墨蓝身体 `#23386B` + pastel 标签，绝不用纯黑
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
│   ├── visual-dna-fusion.md       # 墨蓝手绘风 DNA 锁
│   ├── slide-archetypes.md        # 7 类页面原型
│   ├── prompt-patterns-fusion.md  # 生图 prompt 模板 + ImageGen 撞名修复经验
│   └── qa-checklist.md            # 出图 QA 清单
└── assets/
    ├── mozai-character-sheet.png  # 墨仔角色参考图（本地 SVG 无水印版）
    └── theme-tokens-fusion.json   # 主题色 token
```

## 墨仔生图提示词

直接复制 `references/mozai-character.md` 末尾的 `Generation Prompt Block` 到任意生图工具即可（含两条 HARD RULE：每页仅 1 个墨仔 / 绝不用纯黑）。

## 许可

MIT © 2026 sdhack
