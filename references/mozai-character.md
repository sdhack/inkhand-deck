# 墨仔 (Mozai) · 角色规范

> 版本 1.1.0 · 2026-08-27（revert 回初版墨黑；v1.0.0 曾改墨蓝，现恢复原始墨黑设计）

Paste this spec block verbatim into every page prompt that includes 墨仔.

## Identity

墨仔 is a small soft-ink teardrop creature — a drop of ink that came alive on the page. It is the system's operator: it carries, funnels, pulls, warns, opens, records. Deadpan, calm, slightly absurd. Never cute. Never a mascot sticker.

## Look (fixed across all pages)

- Body shape: **rounded teardrop / ink-drop**, soft matte **ink-black** (#1A1A1A-ish, slightly uneven ink texture, not pure #000000, never a hard silhouette) with faint paper grain and a slight ink halo.
- Top of body: **one thin curly tendril** ending in **one tiny sage-green sprout** (signature mark — keep it visible).
- Face: **two small white-dot eyes**, mostly blank/deadpan; occasionally a thin curved-line mouth; never large, never shiny, never emotive-cartoon.
- Legs: **two thin legs** at rest.
- Arms: thin arms appear only when the action requires them.
- Body accent: **one tiny warm red-orange dot** on the body (the "墨芯").
- The whole creature should read as **soft ink**, not a graphic icon.

## Variants (how the body changes)

墨仔's body is ink — it can morph while keeping the soft-ink feel and signature sprout:

- **Rest**: teardrop body, two thin legs, sprout up.
- **Carry**: same body, two thin arms holding a small hand-drawn object.
- **Funnel**: body becomes a small **ink-black** funnel shape; sprout still visible at the top when possible (note: at funnel scale the sprout may be tiny but must not disappear in body/carry/warn states).
- **Pull**: body leaning back, one thin arm pulling a line or rope.
- **Warn**: body upright, one thin arm holding a small sign or pointing at a warning dot.
- **Record**: body seated with a small notebook/page in lap, one thin arm writing.
- **Open / peek**: body half out of a small opening (hole, drawer, machine) with the other half hidden; sprout visible.
- **Transform**: body morphing into a small machine-part (gear, lever, bar) — still soft ink, sprout still visible.
- **Tiny corner presence**: only when the page is a takeaway or signature slide; otherwise 墨仔 is the actor, not the decoration.

## Personality (must read in the drawing)

- Serious, deadpan, focused on the job.
- A bit clumsy but never stupid.
- Slightly absurd — the job it does is the metaphor.
- Cold humor — never sell cuteness.

## Scale Lock

- Active 墨仔: **12–22% of page height**.
- Tiny corner 墨仔: ≤8% of page height (only for takeaways / signatures).
- 墨仔 never overlaps the title or the page number.
- 墨仔 never touches the corner construction marks.

## Color (墨仔 only)

- Body: soft matte **ink-black** (#1A1A1A-ish, not pure #000000) with faint paper grain.
- Sprout: sage-green.
- Core dot: warm red-orange (small, single).
- No other colors on 墨仔. Information labels stay in pastels.

## Avoid (墨仔)

- Cute mascot, kawaii face, shiny eyes, big smile.
- Children's cartoon proportions, chunky body, chibi style.
- Clothing, accessories, props on its body (it can hold objects, not wear them).
- Multiple 墨仔s on one page.
- 墨仔 as a tiny bystander in the corner of a busy page (it's the actor).
- Replacing diagram structure with 墨仔 — 墨仔 operates within the structure, it does not become the structure.

## Generation Prompt Block (paste verbatim)

```text
Recurring IP character required: 墨仔 (Mozai), a small soft-ink teardrop creature in matte INK-BLACK (around #1A1A1A, not pure #000000, slightly uneven ink texture) with faint paper grain and a slight ink halo, one thin curly tendril on top ending in one tiny sage-green sprout (its signature), two small white-dot eyes, blank deadpan serious face, two thin legs, occasionally thin arms for the action. One tiny warm red-orange core dot on the body. 墨仔 must perform the core conceptual action as the actor, not decorate the scene. Calm, slightly absurd, refined, not cute, not a mascot. Occupies about 12-22% of page height when active. Keep the sage-green sprout visible in every appearance.

HARD RULE: exactly ONE 墨仔 on this page, never two or more. If the page needs 墨仔 at multiple positions, show 墨仔 once in its main actor pose and rely on linework (arrows, ghost outlines, dotted path) to imply motion or sequence; do not draw a second 墨仔 silhouette.

HARD RULE: 墨仔 body and all linework are INK-BLACK (around #1A1A1A). Do NOT use pure #000000 (flat dead black) — keep a soft uneven ink texture. Never tint blue; the whole deck is ink-black on warm paper.
```