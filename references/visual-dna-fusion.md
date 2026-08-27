# 融合视觉 DNA · Handdrawn Shell + 墨仔

> 版本 1.1.0 · 2026-08-27（revert 回初版墨黑）

This is the merged style lock for the fused skill. Use it verbatim in every page prompt.

## Positioning

Refined commercial Chinese handdrawn technical illustration with the recurring IP **墨仔 (Mozai)** embedded as the absurd worker in each diagram.

墨仔 is part of the diagram's meaning — not a sticker pasted on top.

## Canvas

- Final output is a complete raster image.
- Role-specific canvases:
  - Blog/article cover image: 21:9, preferably 2520x1080.
  - Body illustration: 16:9, preferably 1920x1080.
  - Standard deck page: 16:9 unless user specifies.
- Very light warm white paper, near `#FBFAF5`, with extremely subtle grain.
- No full-page border by default.
- Only sparse corner construction marks: faint grey grid / dots / ruler ticks.
- Generous negative space.

## Master Consistency (locked across a multi-page deck)

- Same warm white paper tone and grain.
- Same no-border shell.
- Same small page number convention `NN / TT` in the upper-left.
- Same title treatment: centered medium Chinese title + one short ink-black underline.
- Same subtitle position and scale.
- Same title optical size across body pages (no enlarging short titles).
- Same diagram line weight and hatching style.
- Same pastel family: pale blue, sage green, peach, lavender.
- Same 墨仔 look (see `mozai-character.md`) on every page it appears.
- Same corner construction mark density.

If two pages feel like different illustrators made them, revise prompts before regenerating.

## Deck Shell + Variation

Fixed shell: paper, no border, page number, title block, underline, corner marks, negative space.
Variable middle: object diagram + 墨仔's action + labels + arrows.
Vary layouts by semantic archetype and 墨仔's role — not by changing shell.

## 墨仔 Placement Rules (the fusion)

- Body pages: 墨仔 **required**, embedded in the semantic diagram as the actor.
- Cover pages: 墨仔 optional; can be a small presence or absent.
- One 墨仔 per page max.
- Scale: 墨仔 occupies **12–22% of page height** when active. Never fills the page. Never a tiny corner decoration unless the page is a takeaway / signature.
- Position is determined by the action: pulling a line (墨仔 on the pulling end), funnelling (墨仔 is the funnel or sits at the funnel mouth), warning (墨仔 holds the sign), carrying (墨仔 on the carrying end), etc.
- The diagram's structural lines (arrows, groupings, flows) come from linework, not from 墨仔. 墨仔 operates within the structure.

## Typography

- Heading: clear handdrawn hard-pen Chinese title.
- Body labels: small readable hard-pen Chinese.
- Avoid calligraphic brush, dramatic flyaway strokes, childish doodle fonts, heavy advertising type.
- Scale: body title medium restrained, cover title medium-large but elegant.
- Short-title trap: 4–6 character titles must keep the same optical size as other body pages.

## Text Budget

- Title: 5–12 Chinese characters.
- Subtitle: 3–12 characters or three short terms separated by `·`.
- Main labels: 2–5 per page.
- Captions: 0–6 short items.
- Always provide a `Required text only` list.

## Color

- Paper: near `#FBFAF5`.
- Lines: **ink-black** (#1A1A1A-ish), fine handdrawn with slightly uneven ink texture. The whole deck reads as soft ink on warm paper, not flat black.
- Pastel labels: pale blue, sage green, peach, lavender.
- 墨仔 body: matte **ink-black** (#1A1A1A-ish, not pure #000000, never hard silhouette) with faint paper grain.
- 墨仔 sprout: sage-green (signature).
- 墨仔 core dot: one tiny warm red-orange dot (signature).
- Avoid large saturated blocks, shadows, gradients, neon, product-card styling.

## Line and Shape

- Fine handdrawn lines, stable but slightly irregular.
- Use careful line-art objects: cards, documents, funnels, sieves, shelves, clocks, devices, magnifying glasses.
- Containers paper-filled with thin outlines; pastel fills sparingly.
- Slim quiet arrows.

## Slide Density

- 2–4 main structure groups.
- 4–12 micro modules.
- 0–3 annotations.
- 1 main idea per page.

## Watermark (known platform constraint)

The built-in image generation model stamps a small `AI生成 / WORKBUDDY` watermark in the lower-right corner of every output. This cannot be removed via prompt. Inform the user and crop in post when needed.

## Final Look

A premium Chinese article/teaching-note feeling where 墨仔 quietly does the absurd system work that makes the diagram true.