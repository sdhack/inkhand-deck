# Changelog · inkhand-deck

## v1.1.2 (2026-08-27)

人物卡升级为「肢体完整·表情完整」版本。

- 替换 `assets/mozai-character-sheet.png`：新人物卡由母版 image-to-image 生成，墨仔从绿芽到两条细腿全可见、无裁切，两白点眼死板表情清晰，四肢完整。
- 同步新增 `墨仔-云端图/Generate_a_clean_character_exp_2026-08-27T12-46-51.png`：8 格 deadpan 表情卡（平静/困惑/专注/惊/累/傲/疑/微喜），展示墨仔情绪范围。
- `SKILL.md` / `README.md` / `references/mozai-character.md` / `references/mozai-prompt.md` 文档描述同步为「肢体完整·表情完整人物卡」。
- 版本号 1.1.1 → 1.1.2。

## v1.1.1 (2026-08-27)

同步**墨黑初版视觉金标准母版**（并入 `assets/mozai-mother-version.png`）。

- 新增 `assets/mozai-mother-version.png`：墨黑初版原始母版 demo 页（含 2 墨仔的搬运示意），作为墨仔墨黑初版的"视觉金标准"对照图。
- `SKILL.md` / `README.md` / `references/mozai-character.md` / `references/mozai-prompt.md` 增加母版引用与"云端生图建议以母版为 image-to-image reference 锁定墨黑初版形象"说明。
- 版本号 1.1.0 → 1.1.1。

## v1.1.0 (2026-08-27)

恢复墨仔**初版墨黑设计**（revert v1.0.0 的墨蓝去黑）。

- **墨黑风格锁（初版）**：暖白纸 `#FBFAF5` + 墨黑线/身体 `#1A1A1A`（非死黑 `#000000`，带轻微不均匀墨质）+ pastel 标签。
- 全部 references（mozai-character / mozai-prompt / visual-dna-fusion / prompt-patterns-fusion / qa-checklist）+ SKILL.md + README 配色描述 revert 回墨黑。
- HARD RULE 由「绝不用纯黑」改为「用墨黑 #1A1A1A，非死黑 #000000，绝不偏蓝」。
- 角色参考图重出墨黑版（替换 assets/mozai-character-sheet.png）。
- 绿芽 `#A3C9A8` / 红橙墨芯 `#E07B39` / 白点眼 / 暖白纸 等签名件保留不变。

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
