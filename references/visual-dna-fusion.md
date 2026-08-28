# 融合视觉 DNA · Handdrawn Shell + 墨仔

> 版本 2.0.0 · 2026-08-28（墨仔 v2.0 形象升级 + 手写字体锁 + 抖音竖版 + 细节手绘风格）

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
  - **Douyin / Xiaohongshu / social vertical: 3:4, preferably 1080x1440.** Add thin double-line border + decorative corner flourishes for social framing.
- Very light warm white paper, near `#FBFAF5`, with extremely subtle grain.
- No full-page border by default (add thin double-line border for social vertical formats).
- Only sparse corner construction marks: faint grey grid / dots / ruler ticks.
- Generous negative space.

## Master Consistency (locked across a multi-page deck)

- Same warm white paper tone and grain.
- Same border convention (none for PPT, thin double-line for social vertical).
- Same small page number convention `NN / TT` in the upper-left.
- Same title treatment: centered medium Chinese title + one short ink-black handdrawn wavy underline.
- Same subtitle position and scale.
- Same title optical size across body pages (no enlarging short titles).
- Same diagram line weight and hatching style.
- Same pastel family: pale blue, sage green, peach, lavender.
- Same 墨仔 look (see `mozai-character.md`) on every page it appears.
- Same corner construction mark density.
- Same handwritten font style across all text.

If two pages feel like different illustrators made them, revise prompts before regenerating.

## Deck Shell + Variation

Fixed shell: paper, border convention, page number, title block, wavy underline, corner marks, negative space.
Variable middle: object diagram + 墨仔's action + labels + arrows.
Vary layouts by semantic archetype and 墨仔's role — not by changing shell.

## 墨仔 Placement Rules (the fusion)

- Body pages: 墨仔 **required**, embedded in the semantic diagram as the actor.
- Cover pages: 墨仔 optional; can be a small presence or absent.
- One 墨仔 per page max.
- Scale: 墨仔 occupies **12–22% of page height** when active. Never fills the page. Never a tiny corner decoration unless the page is a takeaway / signature.
- Position is determined by the action: pulling a line (墨仔 on the pulling end), funnelling (墨仔 is the funnel or sits at the funnel mouth), warning (墨仔 holds the sign), carrying (墨仔 on the carrying end), etc.
- The diagram's structural lines (arrows, groupings, flows) come from linework, not from 墨仔. 墨仔 operates within the structure.

## Typography (v2.0 handwritten font lock)

- **ALL TEXT IS CHINESE HANDWRITTEN STYLE.** No formal printed fonts, no English text.
- **Title**: bold brush/marker hand-lettering, with a wavy handdrawn underline.
- **Subtitle**: casual pencil handwriting, smaller than title.
- **Labels / tags / card text**: casual pencil handwriting or natural handwritten Chinese.
- **Page number**: small handwritten style, upper-left.
- **Quote boxes / speech bubbles**: natural handwritten Chinese inside.
- Avoid: calligraphic brush with dramatic flyaway strokes, childish doodle fonts, heavy advertising type, formal serif/sans-serif printed fonts, any English/Latin text.
- Scale: body title medium restrained, cover title medium-large but elegant.
- Short-title trap: 4–6 character titles must keep the same optical size as other body pages.

## Text Budget (v2.0 increased information density)

- Title: 5–12 Chinese characters.
- Subtitle: 3–12 characters or three short terms separated by `·`.
- Main labels: 2–5 per page.
- Captions: 0–6 short items.
- **For social vertical (Douyin/Xiaohongshu)**: increase text information density — include key data points, pastel tags, quote boxes, and contrast cards where appropriate. Cover must have a strong hook title tied to current news hotspot.
- Always provide a `Required text only` list.

## Color

- Paper: near `#FBFAF5`.
- Lines: **ink-black** (#1A1A1A-ish), fine handdrawn with slightly uneven ink texture. The whole deck reads as soft ink on warm paper, not flat black.
- Pastel labels: pale blue, sage green, peach, lavender.
- 墨仔 body: matte **ink-black** (#1A1A1A-ish, not pure #000000, never hard silhouette) with faint paper grain.
- 墨仔 spiral coil: ink-black.
- 墨仔 leaves: sage-green (two leaves, signature).
- 墨仔 eyes: white eye whites + ink-black pupils in upper part.
- 墨仔 core dot: one tiny warm red-orange dot (optional).
- Avoid large saturated blocks, shadows, gradients, neon, product-card styling.

## Line and Shape (v2.0 detailed hand-drawn style)

- Fine handdrawn lines, stable but slightly irregular.
- **Rich detail**: cross-hatching, stippling, subtle ink bleed, delicate hatching for shading and texture.
- Use careful line-art objects: cards, documents, funnels, sieves, shelves, clocks, devices, magnifying glasses, hands, balance scales, price tags.
- Containers paper-filled with thin outlines; pastel fills sparingly.
- Slim quiet arrows.
- Decorative corner flourishes (for social vertical formats).
- Wavy underlines for titles.

## Slide Density

- 2–4 main structure groups.
- 4–12 micro modules.
- 0–3 annotations.
- 1 main idea per page.

## Watermark (known platform constraint)

The built-in image generation model may stamp a small watermark in the lower-right corner of every output. This cannot be fully removed via prompt. **Strategies**: (1) crop in post when needed; (2) use image-to-image with user reference images to reduce watermark visibility; (3) for critical deliverables, use local SVG route (no watermark). Inform the user and crop in post when needed.

## Final Look

A premium Chinese article/teaching-note feeling where 墨仔 (cute but elegant, expressive, with upward-gazing eyes and differentiated mouth) quietly does the absurd system work that makes the diagram true. Rich hand-drawn detail, warm paper, handwritten fonts, and consistent character across all pages.
