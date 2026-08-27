---
name: inkhand-deck
version: 1.1.2
description: Create refined Chinese handdrawn technical article/PPT-style page images featuring the recurring original IP 墨仔 (Mozai), a small soft-ink teardrop creature that acts as the absurd worker in each diagram. Fuses ian-handdrawn-ppt's refined commercial handdrawn shell with an original recurring actor IP. Use when the user wants handdrawn article/slides/courseware/课件/演示稿/配图 that needs a consistent mascot character performing the core conceptual action in each page, or wants the 墨仔 IP, or wants a handdrawn deck with a recurring ink-drop character. Default outputs are 21:9 covers and 16:9 body illustrations with 墨仔 embedded as the actor.
---

# Inkhand Deck · 墨仔手绘

Refined Chinese handdrawn technical page decks with **墨仔 (Mozai)**, the original recurring IP, as the absurd worker in each diagram.

## What this skill is

A fusion of two proven visual systems:

- **Base shell** (from `ian-handdrawn-ppt` V6): refined commercial Chinese handdrawn technical illustration on near-white warm paper, fine ink + pencil, pastel labels, semantic archetypes, large negative space.
- **Actor layer** (originated here, inspired by `ian-xiaohei-illustrations`): a recurring small ink-drop IP — **墨仔** — embedded as the action subject of each diagram. Calm, deadpan, slightly absurd, never cute.

墨仔 is **not** a decorative mascot. It is the system's operator: it carries, funnels, pulls, warns, opens, records. Removing 墨仔 should weaken the metaphor.

## Operating Rule

Default production output is complete raster page images from the built-in image generation model. Blog/article covers default to 21:9; body illustrations default to 16:9. Each page contains both the semantic diagram and exact short Chinese text. 墨仔 appears on every body page as the actor (optional on covers).

This skill produces PPT-style **visual page images**, not editable PPTX/PDF. Do not route to presentation/document packaging because the user says PPT/PPTX/PDF.

## Resource Map

Load only the references you need:

- `references/visual-dna-fusion.md` — merged style lock: handdrawn shell + 墨仔 placement rules.
- `references/mozai-character.md` — 墨仔 detailed spec for prompts (look, variants, scale, action library).
- `references/mozai-prompt.md` — copy-paste prompt cheatsheet (full / short / global-lock blocks).
- `references/slide-archetypes.md` — semantic mapping with 墨仔 actor role per archetype.
- `references/prompt-patterns-fusion.md` — complete prompt templates with 墨仔 injection.
- `references/qa-checklist.md` — verification gates before delivery.
- `assets/theme-tokens-fusion.json` — color/spacing tokens (paper, ink, pastels, 墨仔 accent).
- `assets/mozai-character-sheet.png` — 墨仔人物卡（肢体完整·表情完整，母版 image-to-image 版，带云端水印，参考用）。
- `assets/mozai-mother-version.png` — 墨黑初版视觉金标准（原始母版 demo 页，作配色/形象对照；云端生图建议以此为 image-to-image reference 锁定墨黑初版形象）。

## Workflow

1. **Ingest material.** Read the provided content or attached file. Same intake as ian-handdrawn-ppt.
2. **Intake and gap diagnosis.** Topic, audience, scenario, length, source sufficiency. Ask at most 1–3 questions only when missing info materially changes the deck.
3. **Plan narrative.** Teaching / persuasive / report / product explanation / knowledge card. One main point per page.
4. **Map pages to archetypes + 墨仔 actor role.** For each page choose an archetype and decide 墨仔's action (carry / funnel / pull / warn / record / open / transform). Load `references/slide-archetypes.md`.
5. **Lock the fused style.** Paste the merged style lock from `references/visual-dna-fusion.md` into every page prompt verbatim. Load `references/mozai-character.md` and paste the 墨仔 spec block into every page prompt verbatim. Vary the middle composition per page.
6. **Generate pages.** One image generation call per page. Use the complete-prompt template from `references/prompt-patterns-fusion.md`. Keep `Required text only` short and exact.
7. **Verify.** Run the QA checklist. Check: deck shell consistency across pages, 墨仔 presence + actor role on each body page, Chinese text accuracy, 墨仔 not cute/mascot-y, no watermark-related issues you can avoid, semantic accuracy.
8. **Deliver.** Save images, make a contact sheet, report paths.

## Defaults

- Language: Simplified Chinese.
- Audience: Chinese learners with some technical curiosity.
- Deck length: 8–12 pages for an article, 5–8 for a short idea.
- Output: PNG page images + contact sheet + short blueprint.
- Style: refined near-white Chinese handdrawn technical illustration (V6 shell) + 墨仔 actor on every body page.
- 墨仔 accent colors: matte ink-black body (#1A1A1A-ish, not pure #000000), sage-green sprout, one warm red-orange core dot. All linework is ink-black (#1A1A1A-ish), slightly uneven ink texture.
- Cover: 墨仔 may be present but optional; body pages: 墨仔 required as actor.

## Guardrails (must enforce)

- 墨仔 is **the actor**, not a corner decoration.
- At most **one** 墨仔 per page.
- 墨仔 occupies **12–22% of page height** when active; never fills the page.
- 墨仔 body = soft matte **ink-black** (#1A1A1A-ish, not pure #000000, never hard silhouette) with faint paper grain.
- 墨仔 keeps its **sage-green sprout** signature on every page it appears.
- Body language: deadpan, calm, slightly absurd; never cute, never shiny-eyed, never wearing clothes.
- Handdrawn shell constraints (paper tone, no border, page number, title underline, corner marks, pastel labels, large negative space) still apply on every page.
- 墨仔 does **not** replace diagram structure — arrows, groupings, flows still come from linework.

## Final Response

When finished, report:

- Output folder and contact sheet path.
- Page count, deck type, 墨仔's actor role per page.
- Assumptions made.
- Verification performed and any remaining risks (e.g., image-model watermark in lower-right corner that must be cropped at publish time).