# Prompt Patterns · Fused (Handdrawn Shell + 墨仔)

> 版本 2.0.0 · 2026-08-28（墨仔 v2.0 形象升级 + 手写字体锁 + 抖音竖版模板 + 嘴巴差异化）

Use these templates for every page. Paste the merged style lock and the 墨仔 spec block verbatim.

## 1. Merged Style Lock (paste once per prompt)

```text
Refined commercial Chinese handdrawn technical article/PPT illustration.
Complete raster image on very light warm white paper, near #FBFAF5, with extremely subtle grain.
No full-page border by default (add thin double-line border + decorative corner flourishes for Douyin/social vertical formats).
Upper-left small page number in handwritten style.
Centered medium Chinese title with one ink-black handdrawn wavy underline.
Small subtitle under title when needed.
ALL TEXT IS CHINESE HANDWRITTEN STYLE: bold brush/marker hand-lettering for titles, casual pencil handwriting for subtitles and labels. NO formal printed fonts, NO English text.
For body pages, keep title size optically consistent across pages; do not enlarge short titles.
Fine INK-BLACK ink and pencil linework (NOT pure #000000, slightly uneven ink texture, around #1A1A1A), delicate hatching, cross-hatching, stippling, stable but slightly irregular.
Muted pastel marker labels: pale blue, sage green, peach, lavender.
Sparse corner construction marks only: faint pale grey grid, dots, ruler ticks, measurement lines.
Generous negative space, calm premium teaching-note feeling.
Recurring IP character 墨仔 embedded as the actor (see 墨仔 spec block).
Props should be blank or contain only simple line marks unless their text appears in Required text only.
Avoid full-page border (unless social vertical), yellow paper, beige paper, giant fonts, cheap poster look, childish doodles, many characters, thick marker strokes, dense bullets, corporate template style, shadows, gradients, neon, gibberish text, English filler, formal printed fonts, cute mascot overload.
```

## 2. 墨仔 Spec Block (paste once per prompt that includes 墨仔)

```text
墨仔 (Mozai): a small soft-ink creature with a SLIM ELONGATED TEARDROP body and ROUNDED DOME TOP (not pointed, not sharp), in matte INK-BLACK (around #1A1A1A, not pure #000000, slightly uneven ink texture) with faint paper grain. One thin curly tendril from the rounded top ending in a SPIRAL-SHAPED COIL LOOP, with TWO SAGE-GREEN LEAVES above the spiral (signature). MEDIUM-SIZED ROUND EYES (each 25-30% body width, two eyes 50-55% face width) with LARGE WHITE EYE WHITES and SMALL BLACK PUPILS POSITIONED IN THE UPPER PART (looking upward, signature upward-gaze). Mouth is SMALL BUT CLEAR and DIFFERENTIATED PER PAGE based on action/emotion (choose from: curious O, serious line, determined press, friendly smile, thoughtful tilt, tiny dot). EXACTLY TWO thin black arms (always present) and EXACTLY TWO thin black legs (always present). One optional tiny warm red-orange core dot on body.
墨仔 must perform the core conceptual action as the actor, not decorate. Cute but elegant, expressive, slightly absurd, refined, not a mascot sticker. Occupies about 12-22% of page height when active.
Keep the spiral coil and two green leaves visible in every appearance.
```

## 3. Complete Page Prompt (16:9 body)

```text
Use case: Chinese article/slide body illustration with recurring IP.
Asset type: one complete 16:9 Chinese handdrawn technical body illustration, final raster page.
Preferred final size: 1920x1080 if supported; otherwise keep native ratio and report actual size.

Page role: body illustration.
Create page <NN>/<TT> of a coherent deck.
Page number text exactly: <NN / TT>
Title exactly: <short Chinese title>
Subtitle exactly: <optional short Chinese subtitle>
Archetype: <left-right contrast | horizontal process | circular mechanism | branching map | classification map | matrix table | main metaphor | takeaway>
墨仔 actor role on this page: <one short sentence describing 墨仔's action>
墨仔 mouth shape for this page: <choose one: curious O | serious line | determined press | friendly smile | thoughtful tilt | tiny dot>
Main point: <one sentence>

Apply the merged style lock:
<paste the merged style lock from section 1 verbatim>

Apply the 墨仔 spec block:
<paste the 墨仔 spec block from section 2 verbatim>

Composition:
<specific layout based on semantics. Describe object-based handdrawn diagram AND where 墨仔 is + what it is doing.>
Scale lock:
central diagram 50-60% page width, 35-45% page height; title optically same as other body pages; 墨仔 at 12-22% page height.

Required text only:
<list every visible Chinese text item exactly. Keep this list short.>

Avoid:
full-page border, yellow paper, beige paper, oversized central objects, oversized body-page title,
heavy bottom boxes, extra text, invented micro-labels, gibberish, English, watermark,
crowded composition, many characters, childish cartoons, thick outlines, saturated colors,
corporate template look, cute mascot overload, shiny eyes, formal printed fonts,
multiple 墨仔s on one page, two 墨仔s, a second 墨仔 silhouette. EXACTLY ONE 墨仔 per page.
pure #000000 (flat dead black) — the entire deck must stay in ink-black #1A1A1A + pastels only, never tint blue.
Mozai pointed top, Mozai chubby body, Mozai tiny white-dot eyes, Mozai centered pupils, Mozai same mouth every page, Mozai simple loop, Mozai one leaf, Mozai extra limbs, Mozai missing arms.
```

## 4. Complete Cover Prompt (21:9)

```text
Use case: Chinese article cover image with optional 墨仔 presence.
Asset type: one complete 21:9 ultra-wide Chinese handdrawn technical cover image, final raster page.
Preferred final size: 2520x1080 if supported.

Page role: cover image.
Title exactly: <title>
Subtitle exactly: <subtitle>
Archetype: cover metaphor
Cover hook: <one sentence describing the hook — must tie to current news hotspot or striking contrast>
墨仔 presence: <optional — if present, describe action and mouth shape>
Main point: <one sentence>

Apply the merged style lock (without the 墨仔-mandatory line):
<paste the merged style lock; include the 墨仔 spec block ONLY if 墨仔 appears on this cover>

Composition:
<one small refined central metaphor, occupying about 50-55% page width, with wide empty margins.
If 墨仔 is on this cover, it is a small presence at 10-14% page height near the metaphor.>

Required text only:
<short exact visible Chinese text list>

Avoid:
full-page border, yellow paper, beige paper, large poster composition, giant title, heavy boxes,
extra text, invented micro-labels, English, gibberish, watermark, formal printed fonts, cute mascot overload.
```

## 5. Complete Douyin Vertical Prompt (3:4) — NEW in v2.0

```text
Use case: Chinese Douyin/Xiaohongshu vertical article illustration with recurring IP.
Asset type: one complete 3:4 vertical Chinese handdrawn technical illustration, final raster page.
Preferred final size: 1080x1440.

Page role: <cover | body illustration | takeaway>
Create page <NN>/<TT> of a coherent vertical deck.
Page number text exactly: <NN / TT> (upper-left, body pages only)
Title exactly: <short Chinese title with strong hook>
Subtitle exactly: <optional short Chinese subtitle>
Archetype: <cover metaphor | left-right contrast | main metaphor | takeaway>
墨仔 actor role on this page: <one short sentence describing 墨仔's action>
墨仔 mouth shape for this page: <choose one: curious O | serious line | determined press | friendly smile | thoughtful tilt | tiny dot>
Main point: <one sentence>
Hotspot tie-in: <one sentence — how this page ties to current news/hotspot>

Apply the merged style lock (with social vertical border):
<paste the merged style lock from section 1 verbatim; ensure thin double-line border + decorative corner flourishes>

Apply the 墨仔 spec block:
<paste the 墨仔 spec block from section 2 verbatim>

Composition:
<vertical 3:4 layout. Top: title block + hotspot tags. Middle: detailed hand-drawn diagram + 墨仔 actor. Bottom: pastel tags / quote box / CTA. Increase text information density: include key data, contrast cards, labels.>
Scale lock:
title 15-20% page height; central diagram 35-45% page height; 墨仔 at 12-22% page height; bottom info 15-20% page height.

Required text only:
<list every visible Chinese text item exactly.>

Avoid:
yellow paper, beige paper, oversized objects, heavy boxes, extra text, invented micro-labels,
gibberish, English, watermark, crowded composition, childish cartoons, thick outlines,
saturated colors, corporate template look, cute mascot overload, shiny eyes, formal printed fonts,
multiple 墨仔s, pure #000000, Mozai pointed top, Mozai chubby body, Mozai tiny white-dot eyes,
Mozai centered pupils, Mozai same mouth every page, Mozai simple loop, Mozai one leaf,
Mozai extra limbs, Mozai missing arms.
```

## 6. Multi-page consistency pass

Before generating, check:

- Every page shares the same page number position, paper tone, title wavy underline, line weight, pastel family, handwritten font style.
- 墨仔 looks identical across pages (slim elongated teardrop, rounded dome top, spiral coil + two leaves, medium eyes with upper pupils, differentiated mouth per page, exactly 2 arms + 2 legs).
- 墨仔's mouth shape varies across the deck (at least 3 different mouth shapes in a multi-page deck).
- 墨仔's action varies by archetype and main point.
- 墨仔 scale stays within 12–22% on active pages.
- Every active page pastes the 墨仔 spec block.
- No page has 墨仔 as a tiny corner decoration unless it's a takeaway.
- Required text only lists are short enough for clean Chinese rendering.
- ALL text is Chinese handwritten style, no formal fonts, no English.

## 7. Text fidelity fallback

If image-generated Chinese text is wrong after acceptance: regenerate with fewer words, or reserve blank label spaces and overlay exact text with deterministic post-processing.

## 8. Watermark note

The image model may stamp a watermark in the lower-right corner of every output. This cannot be fully removed via prompt. Strategies: (1) crop in post; (2) use image-to-image with user reference images; (3) use local SVG route for critical deliverables.

## 9. Filename collision workaround (multi-page parallel generation)

The built-in image model auto-generates filenames from the prompt's opening slug + a second-resolution timestamp. **When generating multiple pages in parallel, prompts with identical opening text produce the same slug, and timestamps can collide on the same second — one page silently overwrites another on disk.**

**Fix: prefix every parallel-call prompt with a unique short tag** so the auto-generated slug differs. Examples:

- Cover: `P1-cover: Use case: ...`
- Body P3: `P3-myth-page: Use case: ...`
- Body P6: `P6-warn-page: Use case: ...`

The tag must be at the very start of the prompt. After generation, rename files to semantic names and verify file count == requested page count before assuming success.

**Always verify page count on disk before reporting success.**
