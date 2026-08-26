# Prompt Patterns · Fused (Handdrawn Shell + 墨仔)

> 版本 1.0.0 · 2026-08-27

Use these templates for every page. Paste the merged style lock and the 墨仔 spec block verbatim.

## 1. Merged Style Lock (paste once per prompt)

```text
Refined commercial Chinese handdrawn technical article/PPT illustration.
Complete raster image on very light warm white paper, near #FBFAF5, with extremely subtle grain.
No full-page border and no rectangular frame unless explicitly requested.
Upper-left small page number in handwritten style.
Centered medium Chinese title with one pale blue handdrawn underline.
Small subtitle under title when needed.
For body pages, keep title size optically consistent across pages; do not enlarge short titles.
Fine DEEP BLUE-GREY ink and pencil linework (NOT pure black, soft dark slate-blue around #34465E), delicate hatching, stable but slightly irregular.
Muted pastel marker labels: pale blue, sage green, peach, lavender.
Sparse corner construction marks only: faint pale grey grid, dots, ruler ticks, measurement lines.
Generous negative space, calm premium teaching-note feeling.
Recurring IP character 墨仔 embedded as the actor (see 墨仔 spec block).
Props should be blank or contain only simple line marks unless their text appears in Required text only.
Avoid full-page border, yellow paper, beige paper, giant fonts, cheap poster look, childish doodles, many characters, thick marker strokes, dense bullets, corporate template style, shadows, gradients, neon, gibberish text, English filler, cute mascot look.
```

## 2. 墨仔 Spec Block (paste once per prompt that includes 墨仔)

```text
墨仔 (Mozai): a small soft-ink teardrop creature in matte DEEP INK-BLUE (dark navy, around #23386B, never pure black) with faint paper grain and a slight ink halo, one thin curly tendril on top ending in one tiny sage-green sprout (its signature), two small white-dot eyes, blank deadpan serious face, two thin legs, occasionally thin arms for the action. One tiny warm red-orange core dot on the body.
墨仔 must perform the core conceptual action as the actor, not decorate. Calm, slightly absurd,
refined, not cute, not a mascot. Occupies about 12-22% of page height when active.
Keep the sage-green sprout visible in every appearance.
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
墨仔 actor role on this page: <one short sentence describing 墨仔's action, e.g. "墨仔 sits at the funnel mouth, sorting items into two bins">
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
corporate template look, cute mascot, shiny eyes, multiple 墨仔s on one page, two 墨仔s,
a second 墨仔 silhouette. EXACTLY ONE 墨仔 per page.
pure black, pure black linework, near-black ink — the entire deck must stay in deep blue-grey + deep ink-blue + pastels only.
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
extra text, invented micro-labels, English, gibberish, watermark.
```

## 5. Multi-page consistency pass

Before generating, check:

- Every page shares the same page number position, paper tone, title underline, line weight, pastel family.
- 墨仔 looks identical across pages (soft deep ink-blue, sprout visible, white-dot eyes, deadpan face, tiny red-orange core dot).
- 墨仔's action varies by archetype and main point.
- 墨仔 scale stays within 12–22% on active pages.
- Every active page pastes the 墨仔 spec block.
- No page has 墨仔 as a tiny corner decoration unless it's a takeaway.
- Required text only lists are short enough for clean Chinese rendering.

## 6. Text fidelity fallback

If image-generated Chinese text is wrong after acceptance: regenerate with fewer words, or reserve blank label spaces and overlay exact text with deterministic post-processing.

## 7. Watermark note

The image model stamps `AI生成 / WORKBUDDY` in the lower-right corner of every output. This cannot be removed via prompt. Crop in post if needed.

## 8. Filename collision workaround (multi-page parallel generation)

The built-in image model auto-generates filenames from the prompt's opening slug + a second-resolution timestamp. **When generating multiple pages in parallel, prompts with identical opening text produce the same slug, and timestamps can collide on the same second — one page silently overwrites another on disk.**

Observed in deck production: 7 parallel calls → only 5 files landed; P3/P5 and P4/P6 collided and the later writer overwrote the earlier.

**Fix: prefix every parallel-call prompt with a unique short tag** so the auto-generated slug differs. Examples:

- Cover: `P1-cover: Use case: ...`
- Body P3: `P3-myth-page: Use case: ...`
- Body P6: `P6-warn-page: Use case: ...`

The tag must be at the very start of the prompt (the model uses the first ~60 chars to form the filename). It is not rendered into the image because the model only treats it as prompt text; verify by checking the generated filename contains the tag. After generation, rename files to semantic names (e.g. `01-封面-墨仔天平.png`) and verify file count == requested page count before assuming success.

**Always verify page count on disk before reporting success.** A 7-page deck should land 7 files.