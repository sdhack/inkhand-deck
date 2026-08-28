# Changelog · inkhand-deck

## v2.0.0 (2026-08-28)

墨仔形象**重大升级**（v2.0）：基于多轮用户迭代确认，从 v1.x 的"死鱼脸白点眼+一片绿芽"升级为"圆润穹顶+向上看大眼+差异化嘴巴+螺旋圈双叶+严格四肢"的可爱但优雅形象。同步新增手写字体锁、抖音竖版 3:4 模板、细节手绘风格。

### 墨仔形象升级（核心变更）

- **头顶**：从 v1.x 的泪滴尖顶 → **圆润穹顶（rounded dome top, not pointed）**。用户明确要求"头顶不应该是尖的"。
- **身体**：从 v1.x 的 rounded teardrop → **修长泪滴形（slim elongated teardrop, not chubby/fat/spherical）**。用户反馈"体型显着很胖"。
- **眼睛**：从 v1.x 的 "two small white-dot eyes" → **中等大小圆眼（medium-sized round eyes, 50-55% face width）+ 大白眼珠（large white eye whites）+ 黑瞳孔偏上（small black pupils in upper part, looking upward）**。用户迭代确认"大萌眼睛"、"眼睛向上看"。
- **嘴巴**：从 v1.x 的 "occasionally a thin curved-line mouth" → **每页差异化（differentiated per page based on action/emotion）**。用户明确要求"嘴巴不应该都是一个形状"。新增 6 种嘴型库：好奇 O 形 / 认真一字 / 坚定抿嘴 / 友好微笑 / 思考歪嘴 / 小点嘴。多页 deck 至少使用 3 种。
- **头顶卷须**：从 v1.x 的 "one thin curly tendril ending in one tiny sage-green sprout" → **细卷须 + 螺旋形圈（spiral-shaped coil loop）+ 两片绿叶（two green leaves）**。用户迭代确认"头顶到叶子之间打个圈"、"两片绿叶"。
- **四肢**：从 v1.x 的 "two thin legs at rest, arms appear only when action requires" → **严格两手两腿（exactly two arms + exactly two legs, always present）**。用户明确要求"锁定四肢不要多手多脚"。
- **性格**：从 v1.x 的 "Deadpan, calm, slightly absurd. Never cute." → **可爱但优雅（cute but elegant, expressive, slightly absurd, not a mascot sticker）**。用户迭代中要求"整体还不够可爱"，最终定位为可爱但优雅，不是过度Q版。
- **墨芯红点**：保留为可选（optional），v2.0 迭代中用户未强调，生成图中不明显。

### 视觉风格升级

- **字体**：新增 **全中文手写字体锁（ALL TEXT IS CHINESE HANDWRITTEN STYLE）**。标题用 bold brush/marker hand-lettering + 波浪下划线；副标题/标签用 casual pencil handwriting。禁止正式印刷字体和英文。用户要求"字体不要这么正式的，要有手绘风格的"。
- **细节手绘**：新增 cross-hatching / stippling / subtle ink bleed / delicate hatching 等细节手绘风格要求。用户要求"配图采用细节丰富的手绘风格"。
- **波浪下划线**：标题下划线从 straight 改为 wavy handdrawn underline。

### 新增抖音竖版 3:4 支持

- 新增 **3:4 竖版（1080x1440）** 作为抖音/小红书配图默认尺寸。
- 竖版加 thin double-line border + decorative corner flourishes。
- 新增封面钩子要求："封面设计应该有钩子，紧贴新闻热点"。
- 新增文字信息量要求：竖版增加 key data points / pastel tags / quote boxes / contrast cards。
- `prompt-patterns-fusion.md` 新增完整的 "Complete Douyin Vertical Prompt (3:4)" 模板。

### 文档同步更新

- `SKILL.md`：版本 1.1.2 → 2.0.0，description/Guardrails/Workflow/Defaults 全面更新为 v2.0。
- `references/mozai-character.md`：权威角色规范全面重写，新增 Mouth Expression Library、v2.0 HARD RULE、完整 Generation Prompt Block。
- `references/mozai-prompt.md`：提示词速查全面更新，新增嘴巴差异化速查表、抖音竖版专用锁、v2.0 形象锁/避坑清单。
- `references/visual-dna-fusion.md`：视觉 DNA 锁更新，新增 Typography (v2.0 handwritten font lock)、Text Budget (v2.0 increased density)、Line and Shape (v2.0 detailed hand-drawn)、抖音竖版尺寸。
- `references/prompt-patterns-fusion.md`：提示词模板全面更新，新增 3:4 抖音竖版模板、嘴巴形状字段、封面钩子字段、热点关联字段。
- `references/qa-checklist.md`：QA 清单全面更新，新增 v2.0 墨仔 16 项检查（圆润穹顶/修长身/螺旋圈双叶/中上瞳孔/嘴巴差异化/严格四肢等）、手写字体检查、细节手绘检查、抖音竖版检查。

### 已知待办

- `assets/mozai-character-sheet.png` 仍为 v1.0 版，待更新为 v2.0 人物卡。
- `assets/mozai-mother-version.png` 仍为 v1.0 墨黑初版母版，v2.0 建议叠加用户确认的 v2.0 参考图做 image-to-image。

---

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
