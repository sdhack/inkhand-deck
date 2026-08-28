---
name: inkhand-deck
version: 2.0.0
description: Create refined Chinese handdrawn technical article/PPT-style page images featuring the recurring original IP 墨仔 (Mozai), a small soft-ink teardrop creature with rounded dome top, upward-gazing expressive eyes, differentiated mouth, spiral coil + two green leaves, and exactly two arms + two legs. Fuses ian-handdrawn-ppt's refined commercial handdrawn shell with an original recurring actor IP. Use when the user wants handdrawn article/slides/courseware/课件/演示稿/配图 that needs a consistent mascot character performing the core conceptual action in each page, or wants the 墨仔 IP, or wants a handdrawn deck with a recurring ink-drop character. Supports 21:9 covers, 16:9 body illustrations, and 3:4 Douyin/Xiaohongshu vertical formats with handwritten Chinese fonts.
---

# Inkhand Deck · 墨仔手绘

Refined Chinese handdrawn technical page decks with **墨仔 (Mozai)**, the original recurring IP, as the absurd worker in each diagram.

## What this skill is

A fusion of two proven visual systems:

- **Base shell** (from `ian-handdrawn-ppt` V6): refined commercial Chinese handdrawn technical illustration on near-white warm paper, fine ink + pencil, pastel labels, semantic archetypes, large negative space. **v2.0 update**: all text in Chinese handwritten style (bold brush/marker hand-lettering for titles, casual pencil handwriting for subtitles/labels), rich hand-drawn detail (cross-hatching, stippling), wavy title underlines.
- **Actor layer** (originated here, inspired by `ian-xiaohei-illustrations`): a recurring small ink-drop IP — **墨仔** — embedded as the action subject of each diagram. **v2.0 update**: cute but elegant, with rounded dome top (not pointed), slim elongated teardrop body (not chubby), medium-sized expressive eyes with large white whites and upper-positioned black pupils (looking upward), differentiated mouth per page (not the same shape every page), thin curly tendril with spiral-shaped coil loop + two green leaves (not simple loop + one sprout), exactly two arms + two legs always present.

墨仔 is **not** a decorative mascot. It is the system's operator: it carries, funnels, pulls, warns, opens, records. Removing 墨仔 should weaken the metaphor.

## Operating Rule

Default production output is complete raster page images from the built-in image generation model. Blog/article covers default to 21:9; body illustrations default to 16:9; **Douyin/Xiaohongshu/social vertical default to 3:4 (1080x1440) with thin double-line border + decorative corner flourishes**. Each page contains both the semantic diagram and exact short Chinese text. 墨仔 appears on every body page as the actor (optional on covers).

This skill produces PPT-style **visual page images**, not editable PPTX/PDF. Do not route to presentation/document packaging because the user says PPT/PPTX/PDF.

## Resource Map

Load only the references you need:

- `references/visual-dna-fusion.md` — merged style lock: handdrawn shell + 墨仔 placement rules (v2.0: handwritten fonts, social vertical, detailed hand-drawn style).
- `references/mozai-character.md` — 墨仔 detailed spec for prompts (v2.0: rounded dome, upward-gazing eyes, differentiated mouth, spiral+two leaves, strict limbs) — **authoritative source**.
- `references/mozai-prompt.md` — copy-paste prompt cheatsheet (full / short / global-lock blocks + mouth differentiation library + Douyin vertical lock).
- `references/slide-archetypes.md` — semantic mapping with 墨仔 actor role per archetype.
- `references/prompt-patterns-fusion.md` — complete prompt templates with 墨仔 injection (v2.0: includes 3:4 Douyin vertical template + mouth shape field).
- `references/qa-checklist.md` — verification gates before delivery (v2.0: includes v2.0 character checks + handwritten font checks).
- `assets/theme-tokens-fusion.json` — color/spacing tokens (paper, ink, pastels, 墨仔 accent).
- `assets/mozai-character-sheet.png` — 墨仔人物卡（v1.0 版，v2.0 升级后待更新；参考用）。
- `assets/mozai-mother-version.png` — 墨黑初版视觉金标准（v1.0 原始母版 demo 页，作配色/形象对照；云端生图建议以此为 image-to-image reference 锁定墨黑初版形象，v2.0 建议叠加用户确认的 v2.0 参考图）。

## Workflow

1. **Ingest material.** Read the provided content or attached file. Same intake as ian-handdrawn-ppt.
2. **Intake and gap diagnosis.** Topic, audience, scenario, length, source sufficiency. Ask at most 1–3 questions only when missing info materially changes the deck.
3. **Plan narrative.** Teaching / persuasive / report / product explanation / knowledge card. One main point per page.
4. **Map pages to archetypes + 墨仔 actor role + mouth shape.** For each page choose an archetype, decide 墨仔's action (carry / funnel / pull / warn / record / open / transform), and assign a mouth shape from the differentiation library (curious O / serious line / determined press / friendly smile / thoughtful tilt / tiny dot). Ensure at least 3 different mouth shapes across a multi-page deck. Load `references/slide-archetypes.md`.
5. **Lock the fused style.** Paste the merged style lock from `references/visual-dna-fusion.md` into every page prompt verbatim. Load `references/mozai-character.md` and paste the 墨仔 spec block into every page prompt verbatim. Vary the middle composition per page.
6. **Generate pages.** One image generation call per page. Use the complete-prompt template from `references/prompt-patterns-fusion.md` (16:9 for PPT, 3:4 for Douyin/social vertical). Keep `Required text only` short and exact. Prefix each parallel prompt with a unique tag to avoid filename collisions.
7. **Verify.** Run the QA checklist from `references/qa-checklist.md`. Check: deck shell consistency across pages, 墨仔 v2.0 presence + actor role + mouth differentiation on each body page, Chinese handwritten text accuracy, 墨仔 not cute-mascot-overload, no watermark-related issues you can avoid, semantic accuracy.
8. **Deliver.** Save images, make a contact sheet, report paths.

## Defaults

- Language: Simplified Chinese.
- Audience: Chinese learners with some technical curiosity.
- Deck length: 8–12 pages for an article, 5–8 for a short idea.
- Output: PNG page images + contact sheet + short blueprint.
- Style: refined near-white Chinese handdrawn technical illustration (V6 shell, v2.0 handwritten fonts + detailed hand-drawn style) + 墨仔 actor on every body page.
- 墨仔 accent colors: matte ink-black body (#1A1A1A-ish, not pure #000000), spiral coil ink-black, two sage-green leaves, white eye whites, ink-black upper-positioned pupils, optional warm red-orange core dot. All linework is ink-black (#1A1A1A-ish), slightly uneven ink texture.
- Cover: 墨仔 may be present but optional; body pages: 墨仔 required as actor.
- Canvas: 21:9 cover / 16:9 body / **3:4 Douyin vertical (1080x1440)**.

## Guardrails (must enforce)

- 墨仔 is **the actor**, not a corner decoration.
- At most **one** 墨仔 per page.
- 墨仔 occupies **12–22% of page height** when active; never fills the page.
- 墨仔 body = soft matte **ink-black** (#1A1A1A-ish, not pure #000000, never hard silhouette) with faint paper grain.
- 墨仔 **rounded dome top** (NOT pointed/sharp).
- 墨仔 **slim elongated teardrop body** (NOT chubby/round/spherical/fat).
- 墨仔 **medium-sized eyes with large white whites + upper-positioned black pupils** (looking upward; NOT tiny white-dot eyes, NOT centered pupils, NOT extremely large chibi eyes).
- 墨仔 **differentiated mouth per page** (NOT the same shape on every page; choose from mouth expression library).
- 墨仔 **spiral-shaped coil loop + exactly two green leaves** (NOT simple loop, NOT one leaf, NOT three leaves).
- 墨仔 **exactly two arms + exactly two legs, always present** (NOT extra limbs, NOT missing arms).
- 墨仔 keeps its **spiral coil + two green leaves** signature on every page it appears.
- Body language: cute but elegant, expressive, slightly absurd; never cute-mascot-overload, never shiny-eyed, never wearing clothes.
- **ALL text is Chinese handwritten style** — no formal printed fonts, no English text.
- Handdrawn shell constraints (paper tone, border convention, page number, title wavy underline, corner marks, pastel labels, large negative space) still apply on every page.
- 墨仔 does **not** replace diagram structure — arrows, groupings, flows still come from linework.
- For Douyin/social vertical: cover must have a strong hook tied to current news hotspot; increase text information density.

## Final Response

When finished, report:

- Output folder and contact sheet path.
- Page count, deck type, canvas ratio, 墨仔's actor role and mouth shape per page.
- Assumptions made.
- Verification performed and any remaining risks (e.g., image-model watermark in lower-right corner that must be cropped at publish time; v1.0 character sheet assets pending v2.0 update).
