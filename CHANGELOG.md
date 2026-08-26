# Changelog · inkhand-deck

## v1.0.0 (2026-08-27)

首个公开发布版本。

- **融合来源**：`ian-handdrawn-ppt` V6 手绘外壳 + 原创 IP 墨仔（灵感来自 `ian-xiaohei-illustrations`）。
- **墨蓝去黑风格锁**：暖白纸 `#FBFAF5` + 深蓝灰线 `#34465E` + 墨蓝身体 `#23386B` + pastel 标签，绝不用纯黑。
- **7 类页面原型**：封面 / 左右对比 / 主隐喻 / 机制环 / 矩阵表 / 警示 / 落点，每页映射墨仔演员角色（搬运 / 漏斗 / 拉线 / 警示 / 记录 / 探头）。
- **两种生产模式**：
  - ☁️ 云端生图（ImageGen / nanobanana pro / Gemini）：用 `mozai-character.md` 或 `mozai-prompt.md` 的 prompt block。
  - 🖥️ 本地 SVG 矢量（无水印、不花 credits）：墨仔 `<symbol>` + 无头 Chrome 渲染。
- **文档资产**：
  - `SKILL.md` — 技能入口、触发词、工作流、Guardrails。
  - `references/mozai-character.md` — 墨仔角色规范 + 生图 prompt block（权威源）。
  - `references/mozai-prompt.md` — 开箱即用提示词速查（完整版 / 精简版 / 全局锁 / 避坑）。
  - `references/visual-dna-fusion.md` — 墨蓝手绘风 DNA 锁。
  - `references/slide-archetypes.md` — 页面原型 + 墨仔演员角色表。
  - `references/prompt-patterns-fusion.md` — 生图 prompt 模板 + ImageGen 并发撞名修复经验。
  - `references/qa-checklist.md` — 出图前 QA 清单。
  - `assets/mozai-character-sheet.png` — 墨仔角色参考图（本地 SVG 无水印版）。
  - `assets/theme-tokens-fusion.json` — 主题色 token。
- **修复**：`qa-checklist.md` 中墨仔身体配色描述由误写的 `ink-black` 统一为 `deep ink-blue (#23386B)`，与全局去黑风格锁一致。
- **许可**：MIT。
