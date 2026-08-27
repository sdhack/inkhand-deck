# 墨仔 (Mozai) · 生图提示词速查

> 版本 1.1.2 · 2026-08-27（人物卡升级为肢体完整·表情完整版）
> 开箱即用：直接复制下方任一块到任意生图工具即可锁定墨仔。权威角色规范见 `mozai-character.md`。

---

## 一、中文形象卡（给人看的，不是 prompt）

墨仔是一滴在纸上活过来的墨。软墨泪滴身 + 顶部一根细卷须顶着一片小绿芽（签名标记）+ 两个白点眼 + 死鱼脸 + 两条细腿 + 身上一个红橙小墨芯。
它是"系统操作员"：搬运、漏斗、拉线、警示、记录、探头都由它来做。冷静、死板、有点荒诞，绝不可爱、绝不卖萌、绝不是贴纸吉祥物。

**颜色锁（死规定）**
- 身体：哑光墨黑 `#1A1A1A`（非死黑 `#000000`，带轻微不均匀墨质）
- 线稿：墨黑 `#1A1A1A`
- 绿芽：鼠尾草绿 `#A3C9A8`
- 墨芯：暖红橙 `#E07B39`
- 纸底：暖白 `#FBFAF5`

---

## 二、英文生图 Prompt Block（★ 直接复制这一块 ★）

> 每行都是硬约束。粘进 prompt 末尾即可，前面照常写页面构图/文案。

```text
Recurring IP character required: 墨仔 (Mozai), a small soft-ink teardrop creature in matte INK-BLACK (around #1A1A1A, not pure #000000, slightly uneven ink texture) with faint paper grain and a slight ink halo, one thin curly tendril on top ending in one tiny sage-green sprout (its signature), two small white-dot eyes, blank deadpan serious face, two thin legs, occasionally thin arms for the action. One tiny warm red-orange core dot on the body. 墨仔 must perform the core conceptual action as the actor, not decorate the scene. Calm, slightly absurd, refined, not cute, not a mascot. Occupies about 12-22% of page height when active. Keep the sage-green sprout visible in every appearance.

HARD RULE: exactly ONE 墨仔 on this page, never two or more. If the page needs 墨仔 at multiple positions, show 墨仔 once in its main actor pose and rely on linework (arrows, ghost outlines, dotted path) to imply motion or sequence; do not draw a second 墨仔 silhouette.

HARD RULE: 墨仔 body and all linework are INK-BLACK (around #1A1A1A). Do NOT use pure #000000 (flat dead black) — keep a soft uneven ink texture. Never tint blue; the whole deck is ink-black on warm paper.
```

---

## 三、精简版（快速出图用，控得粗一点）

```text
Include 墨仔 (Mozai): a small matte ink-black (#1A1A1A) soft teardrop ink creature with a tiny sage-green sprout on a curly tendril, two white-dot eyes, deadpan face, red-orange core dot, thin legs. It performs the main action as the actor. Exactly ONE 墨仔, not pure #000000, linework ink-black #1A1A1A.
```

---

## 四、配套"墨黑手绘风"全局锁（每页都要一起粘）

```text
Refined commercial Chinese handdrawn technical article illustration. Very light warm white paper near #FBFAF5 with subtle grain. No full-page border. Centered Chinese title with one ink-black handdrawn underline. Fine ink-black (#1A1A1A) ink/pencil linework, slightly uneven ink texture, delicate hatching. Muted pastel labels: pale blue, sage green, peach, lavender. Sparse corner construction marks (faint grid/dots/ruler ticks). Generous negative space, calm premium teaching-note feel. Avoid yellow/beige paper, giant fonts, corporate template, shadows, gradients, neon, gibberish, English filler, cute mascot, pure #000000.
```

---

## 五、避坑清单（写进 prompt 的 Avoid 段）

- 可爱吉祥物 / 大眼闪光 / 咧嘴笑 / chibi 比例
- 给墨仔穿衣服或戴配件（可手持物件，不可穿戴）
- 一页出现多个墨仔（HARD RULE：仅 1 个）
- 墨仔缩在角落当看客（正文页它是演员，不是装饰）
- 死黑 #000000 线稿 / 纯黑身体（HARD RULE：用墨黑 #1A1A1A，非死黑 #000000）
- 用墨仔替代图表结构（墨仔在结构里"操作"，不"变成"结构）

---

## 六、本地 SVG 路线（不走生图模型，无水印）

墨仔是 `<symbol id="mozai">`，源见各 deck 的 `<defs>`（如项目 `胶原蛋白肽科普-墨蓝SVG-deck/01-封面.svg`），7 页全 `<use>` 复用 —— 改一处全联动。
角色参考图：`assets/mozai-character-sheet.png`（肢体完整·表情完整人物卡，母版 image-to-image 版，带云端水印）。本地无水印矢量路线见项目日志（Chrome 无头 `--screenshot` SVG）。

> **云端生图严格锁定墨黑初版**：若用云端 ImageGen 出墨仔，建议用 image-to-image 模式以 `assets/mozai-mother-version.png`（墨黑初版母版）为 reference image，比纯文字 prompt 更稳地锁死墨黑 `#1A1A1A` 非死黑、绿芽 `#A3C9A8`、墨芯 `#E07B39`、暖白纸 `#FBFAF5` 的原始形象。
