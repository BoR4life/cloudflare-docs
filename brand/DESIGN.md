# DESIGN.md — Bundle of Rays Academy

House visual system for anything Bundle of Rays ships to a screen: proposals, pitch decks, landing pages, module interfaces, XR companion UI, grant and HREC attachments.

This file is authoritative. Where it conflicts with a model's defaults, this file wins. Where a brief conflicts with this file, the brief wins and you say so out loud.

---

## 1. Who this is for

Nurse educators, directors of nursing, clinical education leads, deans and course convenors, HREC committees, hospital procurement, and university partnership offices.

They read documents for a living. They are sceptical of vendors. They have sat through hundreds of tick-box compliance modules and can smell a template from the first screen. Credibility is earned by looking like something a clinician built, not like something a growth team shipped.

The design job is **legibility and seriousness**, with enough craft that it does not read as institutional beige.

---

## 2. The colour rule (read this before touching a palette)

In a clinical setting colour is *functional*. Red, amber and green already mean something on an observation chart, an early warning score, a triage category, an alarm state. Borrowing them for decoration is a category error and clinicians notice.

**Therefore:**

- Red, amber and green are never brand colours, never accents, never gradient stops, never section backgrounds. They are reserved exclusively for genuine clinical state, and only where the artefact actually depicts clinical state.
- The palette does its work in neutrals. One accent, locked, used sparingly.
- No gradient washes as decoration. A gradient must encode something (a scale, a progression) or it does not appear.

### Tokens

```css
--ink:        #101619;  /* cold near-black. Body text, display type. */
--paper:      #F2F4F3;  /* cool paper stock, not warm cream. Page ground. */
--surface:    #FFFFFF;  /* raised surfaces, tables, insets. Used sparingly. */
--rule:       #C6CFCD;  /* hairlines, table rules, column dividers. */
--muted:      #56645F;  /* captions, metadata, source lines, axis labels. */
--accent:     #3730C4;  /* THE accent. Indigo. Locked. */
--accent-ink: #FFFFFF;  /* text on accent. */
```

Why indigo: health-tech has standardised on cyan-blue (#0066CC and its neighbours) and AI-generated design has standardised on warm clay (#D97757). Indigo sits outside both, and outside the clinical triage spectrum, so it can carry brand meaning without carrying clinical meaning.

Accent budget: **one accent element per viewport**. A link colour, or a filled button, or a chart series, or a rule — not all four. If two things are competing to be the accent, one of them becomes `--ink`.

Clinical-state colours, only when depicting real clinical state:

```css
--state-critical: #B3261E;
--state-caution:  #A26400;
--state-stable:   #1F6B3A;
```

---

## 3. Typography

Two families, deliberately inverted from the AI default of serif display over sans body.

- **Display and UI: Archivo.** Weights 500–700. Tight tracking at large sizes (−0.02em at 40px and above). Width is a tool — Archivo's expanded and condensed cuts are permitted for a single hero moment, nowhere else. Tabular numerals for all data.
- **Body and long-form: Source Serif 4.** 400/600. This is the credibility move: a serif body reads as document, not as marketing page. Line-height 1.6. Measure 62–68 characters, never past 75.

Scale (1.25 ratio, clamp for fluid):

```
display   clamp(2.5rem, 5vw, 4rem)   Archivo 600
h1        2.0rem                     Archivo 600
h2        1.5rem                     Archivo 600
h3        1.25rem                    Archivo 500
body      1.0625rem                  Source Serif 4 400
small     0.875rem                   Archivo 400  (metadata, labels)
```

Forbidden typographic moves:

- ALL-CAPS tracked-out eyebrow labels above headings.
- Colouring or italicising one word in a headline for emphasis.
- Meta strings joined with middle dots (`A · B · C`).
- `WORD — fragment` label constructions with a spaced em dash.
- An arrow appended to button or link text.
- Monospace for small data labels. Use Archivo tabular figures instead.
- A label above content that the content already makes obvious.

Sentence case everywhere, including buttons and headings.

---

## 4. Layout

**The chart-margin grid.** Asymmetric, echoing an observation chart: a narrow fixed left column carrying structure and provenance, a wide right column carrying content.

```
┌──────────┬────────────────────────────────────────────┐
│          │                                            │
│  margin  │  content                                   │
│  200px   │  max 68ch                                  │
│          │                                            │
│ section  │  Headline sits here, flush left,           │
│ ref      │  never centred.                            │
│          │                                            │
│ source   │  Body copy. Serif. Generous leading.       │
│ status   │                                            │
│ date     │                                            │
│          │                                            │
├──────────┼────────────────────────────────────────────┤
│          │  hairline rule spans content only          │
└──────────┴────────────────────────────────────────────┘
```

The left margin column carries real information — section reference, evidence source, review status, revision date — or it is empty. It is never filled with decorative numbering. Below 768px it collapses above the content as a single metadata line.

Structure rules:

- Content is left-aligned. Centred body text does not appear. A centred hero is permitted once per site if the hero is a single line.
- Numbered markers (01 / 02 / 03) only where the content is genuinely sequential — a protocol, a timeline, a staged rollout. Not on feature lists.
- Hierarchy comes from space and type size, not from wrapping everything in cards. If more than three identically-shaped rounded cards appear in a row, redesign the section.
- Border radius: 2px on inputs and buttons, 0 on containers and tables. Not one radius on everything.
- One shadow value exists, `0 1px 2px rgba(16,22,25,.08)`, and it is used only on genuinely floating elements — dropdowns, modals. Never on static cards.
- Tables are first-class. Clinical audiences read tables. Hairline rules, no zebra striping, tabular figures, right-aligned numerics.

---

## 5. Motion

One orchestrated moment per page, maximum — a single reveal or load sequence, if it earns its place.

Banned: fade-and-slide-up entrances on every section, hover lifts on every card, scroll-triggered counters, parallax.

Motion that answers a user action — a panel opening, a state confirming, a value updating — is always welcome, because it shows what changed. Durations 120–200ms, ease-out. `prefers-reduced-motion` is respected without exception.

---

## 6. Copy

- Plain verbs, sentence case, no filler. Australian English: organise, recognise, colour, programme (for a course of study), practise (verb).
- Name things as a clinician would name them. "Handover simulation", not "knowledge transfer module". "Scenario", not "learning experience".
- Buttons say what happens. "Start the scenario", not "Get started". "Download the evidence summary", not "Submit".
- No hype adjectives: revolutionary, cutting-edge, seamless, powerful, game-changing, transformative. If a claim is worth making, make it with a number and a source.
- Every efficacy or outcome claim carries its source in the margin column. This is the single biggest credibility lever with academic and HREC readers, and it is non-negotiable.
- Errors state what happened and what to do. Empty states are an invitation to act.

---

## 7. Quality floor

Responsive to 360px. Visible keyboard focus (2px `--accent` outline, 2px offset). Contrast: body text ≥ 7:1, large text and UI ≥ 4.5:1. Semantic headings in order. Real `<table>` markup for tabular data. Alt text that describes clinical content, not "image of chart".

---

## 8. Self-check before shipping

Run this list. Any yes is a rewrite.

1. Could this be any health-tech company's page with the logo swapped?
2. Is there a warm cream background, a serif display headline, and a terracotta accent?
3. Is there more than one accent colour doing brand work?
4. Are red, amber or green used decoratively?
5. Are there identical rounded cards with identical shadows standing in for hierarchy?
6. Is there an ALL-CAPS eyebrow label anywhere?
7. Does any section animate in on scroll for no reason?
8. Does an outcome claim appear without a source?
9. Is the boldness spread across three elements instead of concentrated in one?

Then remove one thing.

---

## 9. Using this file

**Claude Code:** keep `DESIGN.md` at the repo root. Reference it from `CLAUDE.md` with a line such as `Follow DESIGN.md for all visual and copy decisions.`

**Claude app:** attach this file to the project, or paste it at the top of a build request.

**Amendments:** change this file rather than overriding it in a prompt. A one-off override that works twice belongs in here.
