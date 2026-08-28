# 墨仔 (Mozai) · 生图提示词速查

> 版本 2.0.0 · 2026-08-28（墨仔形象重大升级：圆润穹顶 + 向上看大眼 + 差异化嘴巴 + 螺旋圈双叶 + 严格四肢）
> 开箱即用：直接复制下方任一块到任意生图工具即可锁定墨仔 v2.0。权威角色规范见 `mozai-character.md`。

---

## 一、中文形象卡（给人看的，不是 prompt）

墨仔是一滴在纸上活过来的墨。**修长泪滴身 + 圆润穹顶（不尖）** + 顶部一根细卷须顶着**螺旋形圈 + 两片绿叶**（签名标记）+ **中等大小圆眼，大白眼珠，黑瞳孔偏上（向上看）** + **差异化小嘴巴（每页根据场景不同）** + **严格两手两腿** + 身上可选一个红橙小墨芯。
它是"系统操作员"：搬运、漏斗、拉线、警示、记录、探头都由它来做。**可爱但优雅**，有表情但不过度卖萌，绝不是贴纸吉祥物。

**颜色锁（死规定）**
- 身体：哑光墨黑 `#1A1A1A`（非死黑 `#000000`，带轻微不均匀墨质）
- 线稿：墨黑 `#1A1A1A`
- 螺旋圈：墨黑 `#1A1A1A`
- 绿叶：鼠尾草绿 `#A3C9A8`（两片）
- 眼白：白色
- 瞳孔：墨黑 `#1A1A1A`（偏上位置）
- 墨芯：暖红橙 `#E07B39`（可选）
- 纸底：暖白 `#FBFAF5`

**形象锁（v2.0 死规定）**
- 头顶：圆润穹顶，**不尖**
- 身体：修长泪滴形，**不圆胖**
- 眼睛：中等大小（占脸 50-55%），大白眼珠，**黑瞳孔偏上（向上看）**
- 嘴巴：**每页差异化**（好奇O / 认真一字 / 坚定抿嘴 / 友好微笑 / 思考歪嘴 / 小点）
- 卷须：细卷须 + **螺旋形圈** + **两片绿叶**
- 四肢：**严格两手两腿**，每次都有

---

## 二、英文生图 Prompt Block（★ 直接复制这一块 ★）

> 每行都是硬约束。粘进 prompt 末尾即可，前面照常写页面构图/文案。

```text
Recurring IP character required: 墨仔 (Mozai), a small soft-ink creature with a SLIM ELONGATED TEARDROP body and ROUNDED DOME TOP (not pointed, not sharp), in matte INK-BLACK (around #1A1A1A, not pure #000000, slightly uneven ink texture) with faint paper grain. One thin curly tendril from the rounded top ending in a SPIRAL-SHAPED COIL LOOP, with TWO SAGE-GREEN LEAVES above the spiral (signature). MEDIUM-SIZED ROUND EYES (each 25-30% body width, two eyes 50-55% face width) with LARGE WHITE EYE WHITES and SMALL BLACK PUPILS POSITIONED IN THE UPPER PART (looking upward, signature upward-gaze). Mouth is SMALL BUT CLEAR and DIFFERENTIATED PER PAGE based on action/emotion (choose from: curious O, serious line, determined press, friendly smile, thoughtful tilt, tiny dot). EXACTLY TWO thin black arms (always present) and EXACTLY TWO thin black legs (always present). One optional tiny warm red-orange core dot on body. 墨仔 must perform the core conceptual action as the actor, not decorate the scene. Cute but elegant, expressive, slightly absurd, refined, not a mascot sticker. Occupies about 12-22% of page height when active. Keep the spiral coil and two green leaves visible in every appearance.

HARD RULE: exactly ONE 墨仔 on this page, never two or more. If the page needs 墨仔 at multiple positions, show 墨仔 once in its main actor pose and rely on linework (arrows, ghost outlines, dotted path) to imply motion or sequence; do not draw a second 墨仔 silhouette.

HARD RULE: 墨仔 body and all linework are INK-BLACK (around #1A1A1A). Do NOT use pure #000000 (flat dead black) — keep a soft uneven ink texture. Never tint blue; the whole deck is ink-black on warm paper.

HARD RULE: rounded dome top (NOT pointed), slim elongated body (NOT chubby/fat), medium eyes with upper pupils (NOT tiny white-dot eyes, NOT centered pupils), differentiated mouth (NOT same shape every page), spiral coil + two leaves (NOT simple loop, NOT one leaf), exactly 2 arms + 2 legs (NOT extra limbs, NOT missing arms).
```

---

## 三、精简版（快速出图用，控得粗一点）

```text
Include 墨仔 (Mozai): a small matte ink-black (#1A1A1A) soft ink creature with SLIM ELONGATED TEARDROP body and ROUNDED DOME TOP (not pointed), thin curly tendril with SPIRAL COIL + TWO SAGE-GREEN LEAVES, MEDIUM ROUND EYES with large white whites and small black pupils in UPPER part (looking up), small CLEAR mouth DIFFERENTIATED per scene, EXACTLY 2 thin arms + EXACTLY 2 thin legs. It performs the main action as the actor. Cute but elegant. Exactly ONE 墨仔, not pure #000000, linework ink-black #1A1A1A.
```

---

## 四、配套"墨黑手绘风"全局锁（每页都要一起粘）

```text
Refined commercial Chinese handdrawn technical article illustration. Very light warm white paper near #FBFAF5 with subtle grain. No full-page border by default (add thin double-line border for Douyin/social vertical formats). Centered Chinese title with one ink-black handdrawn underline. ALL TEXT IS CHINESE HANDWRITTEN STYLE: bold brush/marker hand-lettering for titles, casual pencil handwriting for subtitles and labels. NO formal printed fonts, NO English text. Fine ink-black (#1A1A1A) ink/pencil linework, slightly uneven ink texture, delicate hatching, cross-hatching, stippling. Muted pastel labels: pale blue, sage green, peach, lavender. Sparse corner construction marks (faint grid/dots/ruler ticks). Generous negative space, calm premium teaching-note feeling. Avoid yellow/beige paper, giant fonts, corporate template, shadows, gradients, neon, gibberish, English filler, formal fonts, pure #000000.
```

---

## 五、嘴巴差异化速查（写进每页 prompt 的 Mouth 段）

在多页 deck 中，至少使用 3 种不同嘴型，不要每页都一样。

| 嘴型 | 英文 prompt 写法 | 适用场景 |
|---|---|---|
| 好奇 O 形 | `small curious O-shaped open mouth` | 封面仰望、发现、惊讶 |
| 认真一字 | `small serious straight-line mouth` | 对比页、持天平、专注 |
| 坚定抿嘴 | `small firm pressed determined mouth (slightly downturned corners)` | 推开、拒绝、立场 |
| 友好微笑 | `small friendly curved smiling mouth (upward arc)` | 落点页、举牌、互动 |
| 思考歪嘴 | `small thoughtful tilted mouth (one corner up)` | 疑问、权衡、思考 |
| 小点嘴 | `very small dot mouth (minimal)` | 中性观察、安静存在 |

---

## 六、避坑清单（写进 prompt 的 Avoid 段）

- 尖头顶 /  sharp pointed top（必须圆润穹顶）
- 圆胖身体 / chubby spherical fat body（必须修长泪滴）
- 极大眼睛 / extremely large chibi eyes（必须中等 50-55% 脸宽）
- 小白点眼 / tiny white-dot eyes（v1.0 旧款，v2.0 是大眼白+上瞳孔）
- 瞳孔居中 / centered pupils（必须偏上，向上看）
- 每页嘴型一样 / same mouth every page（必须差异化）
- 无嘴 / 看不见嘴 / no mouth invisible mouth（必须小但清晰）
- 简单圈 / simple loop on tendril（必须螺旋形圈）
- 一片叶或三片叶 / one leaf or three leaves（必须恰好两片）
- 多手多脚 / extra limbs（必须恰好 2 手 2 脚）
- 缺手 / missing arms（手每次都要有，不是动作需要时才有）
- 可爱吉祥物过载 / cute mascot kawaii overload shiny eyes big grin
- 给墨仔穿衣服或戴配件（可手持物件，不可穿戴）
- 一页出现多个墨仔（HARD RULE：仅 1 个）
- 墨仔缩在角落当看客（正文页它是演员，不是装饰）
- 死黑 #000000 线稿 / 纯黑身体（HARD RULE：用墨黑 #1A1A1A，非死黑 #000000）
- 正式印刷字体 / formal printed fonts（必须手写风格字体）
- 英文文字 / English text（必须全中文）
- 用墨仔替代图表结构（墨仔在结构里"操作"，不"变成"结构）

---

## 七、抖音竖版配图专用锁（3:4）

当用户要求抖音配图 / 竖版 / 小红书配图时，使用 3:4 竖版（1080x1440），并加以下锁：

```text
Canvas: 3:4 vertical, 1080x1440. Thin double-line border around the page (for social media framing). Decorative corner flourishes at all four corners. ALL TEXT IS CHINESE HANDWRITTEN STYLE. Cover page must have a strong hook title tied to current news hotspot. Increase text information density: include subtitle, key data points, pastel tags, and quote boxes where appropriate.
```

---

## 八、本地 SVG 路线（不走生图模型，无水印）

墨仔是 `<symbol id="mozai">`，源见各 deck 的 `<defs>`（如项目 `胶原蛋白肽科普-墨蓝SVG-deck/01-封面.svg`），7 页全 `<use>` 复用 —— 改一处全联动。
角色参考图：`assets/mozai-character-sheet.png`（v1.0 人物卡，v2.0 升级后待更新）。本地无水印矢量路线见项目日志（Chrome 无头 `--screenshot` SVG）。

> **云端生图严格锁定 v2.0**：若用云端 ImageGen 出墨仔，建议用 image-to-image 模式以用户确认的 v2.0 参考图为 reference image，比纯文字 prompt 更稳地锁死圆润穹顶、向上看大眼、差异化嘴巴、螺旋圈双叶、修长泪滴身、两手两腿的 v2.0 形象。
