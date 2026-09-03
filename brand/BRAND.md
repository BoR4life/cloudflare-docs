# Bundle of Rays — brand kit

Version 1.0. 03 Sep 2026.

This file covers the brand: the mark, colour, typography, texture, the generated layer, and how
the brand is applied. [`DESIGN.md`](./DESIGN.md) governs the house visual system. Where the two
disagree, DESIGN.md wins and this file is wrong. Everything below has been reconciled against it.

## Licence status — read this before applying anything

**The mark is not owned by Bundle of Rays, and the permission on record does not cover using it as
a company logo.**

The artwork is *Us* by Jean Jullien. It was not commissioned. The record:

- **01 Jun 2025** — permission requested to use *Us* for *The Just Us Show*, a monthly VR gathering
  for nurses and teachers, in promotional material and virtual set design, with credit.
- **02 Jun 2025** — Studio Jean Jullien: *"Jean is happy to let you use US, It would have to be
  limited to this project only, ie not used again over consecutive conferences etc. If you're ok
  with that, no fee for you."*
- **02 Jun 2025** — the studio asks how long the show will run. The reply proposes a year, or an
  initial six months, and raises use *"potentially as an implied logo for the show"*.
- **No further reply on record.** Neither the term nor the logo use was agreed.

Company use differs on every axis: a different entity, indefinite term, trademark use, and a
derivative work, since a wordmark has been added beneath the artwork.

**Required before application.** A written licence from Studio Jean Jullien covering company
identity: scope, territory, term, permitted media (print, digital, garments, XR textures), and
whether the wordmark lockup is permitted as a derivative. Expect a fee. If declined, commission a
new mark — the system below survives that, because only the shape vocabulary is mark-specific.

## 1. What the brand is for

Bundle of Rays sells XR and AI education to hospitals and universities. The people who decide are
nurse educators, directors of nursing, clinical education leads, deans, HREC committees and
procurement. They read documents for a living and can identify a template from the first screen.

The brand has one job: **look like something a clinician built, not something a growth team
shipped.** Credibility first, and enough craft that it does not read as institutional beige.

Tagline in use: *Interactive education where learning is reality.*

## 2. The mark

Two brush-ink forms that read as lungs and as a pair of faces in profile, with almond eyes and a
hand-lettered wordmark. Warm, human, faintly funny, deliberately un-clinical — which is the point:
it is the one part of the brand that is not sober, and it earns the sobriety of everything else.

### Lockups

| Lockup | Use |
| --- | --- |
| Vertical | Default. Wordmark above, forms centre, "of rays" below. The production lockup. |
| Horizontal | Where vertical space is short — footers, email signatures, document headers. |
| Forms only | Only where the brand is already named on the same surface. Never as a standalone identifier. |

### Rules

Clear space on all four sides equals the cap height of the wordmark. Minimum reproduction is 24 mm
wide in print and 96 px on screen; below that the eyes fill in and the forms go muddy.

Reproduce in ink on paper, or reversed paper on ink. It may sit on the accent. It may not sit on
any clinical-state colour. Never recolour the mark itself, never outline it, never add a strapline
inside the lockup, never set it in a white box on a dark ground — reverse it properly.

Credit Jean Jullien wherever the mark appears. This was a condition of the original permission and
is right regardless.

**Asset status.** The only artwork available is a 225 × 224 px raster with a baked white
background. Transparent ink and paper versions have been derived from it and live in `logo/`, but
they are upsampled from a thumbnail and are not master artwork. Vector art must come from Studio
Jean Jullien — the same conversation as the licence, so make one request for both.

## 3. Colour

Governed entirely by DESIGN.md. Two things carry the brand: ink and paper. One accent does brand
work. Red, amber and green are never brand colours.

**Why that rule matters more here than in most brands.** In a clinical setting colour is
functional. Red, amber and green already encode early warning scores, triage categories and alarm
states. Borrowing them for decoration is a category error, and the audience is exactly the group
that notices. This retired the entire v0.1 palette, which was built from Jean Jullien's flat poster
colour — right for an illustrator's practice, wrong for this audience.

### Core

| Token | Value | On paper | Use |
| --- | --- | --- | --- |
| Ink | `#101619` | 16.52 | Body text, display type, the mark |
| Paper | `#F2F4F3` | — | Page ground |
| Surface | `#FFFFFF` | 1.10 | Raised surfaces, tables, insets. Sparingly |
| Rule | `#C6CFCD` | 1.44 | Hairlines and dividers. Non-text only |
| Muted | `#56645F` | 5.62 | Large text and UI only — see amendment |
| Accent | `#3730C4` | 7.98 | One accent element per viewport |

### Clinical state

Only where the artefact depicts genuine clinical state.

| Token | Value | On paper | Level |
| --- | --- | --- | --- |
| Critical | `#B3261E` | 5.92 | Large and UI only |
| Caution | `#A26400` | 4.36 | **Fails the 4.5 floor. Do not set type in it** |
| Stable | `#1F6B3A` | 5.90 | Large and UI only |

### Amendments proposed to DESIGN.md

DESIGN.md sets a 7:1 body-text floor. Five of its own values do not meet it in the roles it assigns
them. These are proposed, not adopted — amendments belong in DESIGN.md, so they need sign-off there.

| Token | Value | On paper | Why |
| --- | --- | --- | --- |
| Muted text | `#454F4B` | 7.69 | `--muted` is assigned to captions and source lines, which are text, at 5.62 |
| Accent dark | `#8B87E8` | 5.85 *on ink* | `--accent` is 2.07 on ink and cannot appear on an ink ground at all |
| Critical text | `#9C2019` | 7.22 | State rendered as words rather than fills |
| Caution text | `#6E4400` | 7.63 | As above, and the base value fails every floor |
| Stable text | `#1A5C32` | 7.25 | As above |

## 4. Typography

Archivo for display and UI, Source Serif 4 for body and long-form. Deliberately inverted from the
AI default of serif display over sans body: a serif body reads as document, not as marketing page,
which is the credibility move with this audience.

Both are SIL OFL 1.1, and that is load-bearing rather than incidental: **they can be embedded in
Unity and Unreal builds without a licence problem.** Commercial foundry licences routinely exclude
embedding in an application binary, which is exactly what an XR module is. Do not substitute a paid
face without reading the EULA's embedding clause.

Scale, weights, measure and the forbidden typographic moves are in DESIGN.md §3 and are not
restated here.

**Do not chase the hand-lettering.** Never set type in a marker or faux-handwritten face. The
wordmark is genuine hand-lettering by a serious illustrator; an imitation beside it does not borrow
its credibility, it lends the wordmark its own cheapness. This is not hypothetical — see §7.

## 5. Texture and the ink field

Texture is print-derived, because the mark is ink.

**The ink field** is the brand's strongest device and its primary layout for anything whose job is
recognition rather than information: covers, opening slides, back pages, merchandise. A single
full-bleed field of ink with a torn brush edge, the eyes knocked out to paper, and the wordmark
beneath. No photograph, no accent, no explanation.

Rules: the field bleeds off at least three edges; the edge is torn or brushed, never a straight cut
or a rounded rectangle; the eyes knock out to paper, never to the accent; it carries the wordmark
or a headline, never both plus body copy. If it needs body copy, it is the wrong layout.

**Paper grain** may sit over a full-bleed ground at 0.045 opacity and nowhere else. Drop it
entirely in-headset — at foveated resolutions it becomes shimmer.

Prohibited: gradients as decoration (a gradient must encode a scale or a progression), drop shadows
other than the single DESIGN.md value on genuinely floating elements, glassmorphism, glow, bevel,
and stock imagery with circuit-board or neural-network overlays.

## 6. The generated layer

Influence: [someform](https://someform.studio/) — Matthias Winckelmann and Helge Kiehl, Berlin.
Their practice is identity built from logic, with tooling handed to the client so assets are
produced in-house. Their rendered surface is simulated-photographic and would fight a brush-ink
mark; what is borrowed is the method, not the surface.

`generate-cover.mjs` produces module artwork from a seed, deterministically: `BOR-114` resolves to
the same cover permanently, so the decision is never stored, briefed or remembered. No dependencies.

```
node brand/generate-cover.mjs BOR-114
node brand/generate-cover.mjs BOR-114 --ratio social --out build/
```

Ratios: `cover` 1200×1600, `social` 1200×630, `square` 1200×1200, `scene` 1920×1080.

Shape vocabulary is the mark's own and nothing else: the arch, the ray bundle, the pair of eyes.
Five archetypes keep output composed rather than random — `arch-and-rays`, `the-pair`,
`corner-rays`, `horizon`, `crew`. **Adding to or reordering that list reshuffles every existing
seed, because the archetype is the first draw. Lock it before covers go into production.**

The seed also picks a reversed ink ground about a quarter of the time, which uses the amended
dark-ground accent. Colour is ink, paper and the one accent — nothing else.

### Characters

The mark's forms already read as figures, so the cast is the mark at small scale. A crew is three
to five figures at varying heights, most wearing a headset visor, one keeping the mark's own eyes
so the family resemblance stays visible. The visor sits exactly where the eyes sit; the strap stops
at the silhouette rather than running the full head width.

**Headsets, not televisions.** A screen for a face is an old and free idea, but a boxy CRT with
rabbit-ear antennae worn with a Napoleonic dress uniform is a specific existing character — Prince
Robot IV, from *Saga* (Vaughan and Staples, Image Comics), actively published and heavily
merchandised. Anything carrying those specifics reads as their character whatever it is called, and
this brand cannot afford a second rights problem while the mark's own licence is unresolved. A
visor avoids it and is stronger anyway: a nurse in a headset is what this company does. Keep figures
flat and silent — no antennae, no uniform, nothing playing on the screen.

## 7. What production taught us

Measured from `BOR001_DL_Flyer_PROOF_V2` (DL, 100 × 210 mm), the first artefact this kit was checked
against.

| | In production | Governed value |
| --- | --- | --- |
| Ink | `#0A0203` | `#101619` |
| Paper | `#FFFFFF` | `#F2F4F3` |
| Display | Permanent Marker | Archivo |
| Body | Merriweather 9 pt reversed | Source Serif 4, 12 pt floor, ink on paper |
| Stray | Ubuntu, 3 glyphs | Remove |

Four defects, all now rules above. Permanent Marker sat beside the real hand-lettering and cheapened
it. Body copy was 9 pt reversed serif, which fills in on uncoated stock and thins on coated. The
logo appeared in a white box on a black ground while the front of the same file reversed correctly.
And the URL still read `www.TBC.com.au` in a file named PROOF_V2.

## 8. Applications

| Surface | Layout | Notes |
| --- | --- | --- |
| Flyer, DL | Ink field front, paper back | Body ink on paper. One accent element |
| Module cover | Generated | Type set over, never generated into the artwork |
| Deck | Ink field opener, paper thereafter | One accent per slide |
| Document, proposal, HREC | Chart-margin grid, DESIGN.md §4 | Every outcome claim carries its source in the margin |
| Email signature | Horizontal lockup, ink on paper | No image-only signatures |
| XR | Ink and paper, raised stroke weights | No paper grain. Nothing below AA |

## 9. Quality floor

Responsive to 360 px. Visible keyboard focus, 2 px accent outline at 2 px offset. Body text ≥ 7:1,
large text and UI ≥ 4.5:1. Semantic headings in order. Real `<table>` markup for tabular data. Alt
text that describes clinical content. Print body never below 12 pt. Australian English throughout.

Before shipping, run DESIGN.md §8. Any yes is a rewrite.

## 10. Governance

DESIGN.md is authoritative and changes there, not in a prompt. A one-off override that works twice
belongs in the file. This kit is versioned with it.

**Version 1.0 is a governed draft, not a signed-off brand.** Three blockers stand: the mark licence,
the absence of master artwork, and the five contrast amendments awaiting sign-off in DESIGN.md.

## Files

- `DESIGN.md` — the governing house system. Authoritative.
- `tokens.css` — custom properties, every ratio computed and commented.
- `tokens.json` — the same values as design tokens, with warnings, amendments and status.
- `brand-kit.html` — the visual kit.
- `generate-cover.mjs` — procedural cover generator. Deterministic, no dependencies.
- `logo/` — the mark. Placeholder rasters plus derived transparent ink and paper versions.
