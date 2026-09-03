# Bundle of Rays — Brand Kit

Version 0.1 — 03 Sep 2026. Working draft.

## Licence status — read this first

**The mark is not owned by Bundle of Rays, and the permission on record does not cover
using it as a company logo.** Resolve this before the kit is applied to anything.

The artwork is *Us* by [Jean Jullien](https://en.wikipedia.org/wiki/Jean_Jullien_(designer)).
It was not commissioned for Bundle of Rays. The email record with Studio Jean Jullien reads:

- **01 Jun 2025** — permission requested to use the existing *Us* artwork for *The Just Us Show*,
  a monthly 30-minute VR gathering for nurses and teachers, in promotional material and virtual
  set design, with credit.
- **02 Jun 2025** — Sarah, Studio Jean Jullien: *"Jean is happy to let you use US, It would have to
  be limited to this project only, ie not used again over consecutive conferences etc. If you're ok
  with that, no fee for you."*
- **02 Jun 2025** — the studio asks how long the show will run. The reply proposes a year, or an
  initial six months, and raises using it *"potentially as an implied logo for the show"*.
- **No further reply on record.** The six-month term and the logo use were never agreed.

So the grant is: *Us*, for The Just Us Show, that project only, no fee, no ongoing use. What the
kit currently assumes is different on every axis — a different entity (Bundle of Rays Academy Pty
Ltd rather than a community show), indefinite use, trademark use as a company identity, and a
derivative work, since a hand-lettered "BUNDLE OF RAYS" wordmark has been added beneath the
artwork. None of that was granted.

**What to do.** Go back to Studio Jean Jullien and ask for a written licence covering company
identity: scope, territory, term, permitted media (print, digital, garments, XR textures), and
whether the wordmark lockup is allowed as a derivative. Expect a fee — the free grant was
explicitly tied to a single community project. If the studio declines, or the fee doesn't work,
commission a new mark. Do not print, register, or ship the current lockup until one of those two
things has happened.

Everything below is a sound system for this artwork, and it is worth keeping — but it is
contingent on that licence.

## The premise

Tagline in use: **Interactive education where learning is reality.**

The mark is two black brush-ink forms that read as lungs and as a pair of faces in profile, with
the wordmark set beneath. It is warm, human, slightly funny, and completely un-clinical.

That mark is the constraint, not a decoration sitting on top of one. Every decision below follows
from it. A brush-ink logo cannot sit on a gradient, inside a glass card, or beside a glowing
purple "AI" flourish without one of the two looking like a mistake — and it will not be the logo
that looks wrong, it will be everything else.

The strategic value is that healthcare and university procurement decks are saturated with
clinical blue, stock headset photography and circuit-board overlays. A hand-drawn ink mark on
uncoated paper is instantly distinguishable in that room. Protect that.

## Colour

Jullien's method is a single black brush line with flat block colour filled in digitally. The
palette copies that logic: ink and paper do the work, four flats do the shouting, nothing blends.

### Core

| Token | Hex | Role |
| --- | --- | --- |
| Ink | `#14110F` | The mark, and all body type on paper. Warmed off pure black — brush ink on paper is never `#000`. |
| Paper | `#F6F1E7` | Default ground. Uncoated and warm, not white. |

Ink on Paper is **16.70:1** — AAA. This pairing carries the brand. The rest is seasoning.

### Flats — for fills

Set type on these to Ink, with one exception.

| Token | Hex | Type on top | Contrast | Level |
| --- | --- | --- | --- | --- |
| Ray | `#E8A33C` | Ink | 8.72 | AAA |
| Pulse | `#E24E38` | Ink | 4.82 | AA |
| Breath | `#3F8F5B` | Ink | 4.74 | AA |
| Deep | `#2B47C8` | **Paper** | 6.57 | AA |

Deep is the only inverting colour. Ink on Deep is 2.54:1 — never set black type on it.

Ray is the "rays" in the name: light through something. It is the closest thing to a signature
colour and it takes black type beautifully at AAA. If one colour appears, make it Ray.

### Deep variants — for coloured type

| Token | Hex | On Paper | Level |
| --- | --- | --- | --- |
| Ray Deep | `#6F480E` | 7.15 | AAA |
| Pulse Deep | `#A62E1D` | 6.16 | AA |
| Breath Deep | `#26603B` | 6.62 | AA |

Deep (`#2B47C8`) is already text-safe on Paper at 6.57 and needs no variant.

### Rules

Two colours per surface, maximum: Ink plus one flat. Three only on a cover or a poster. The
palette fails the moment it becomes a rainbow — Jullien's restraint is doing the work, not the
number of colours available.

Never tint, never blend, never gradient between two flats. If you need a lighter Ray, use less
Ray, not a paler Ray.

## Typography

The wordmark is hand-lettered. Do not chase it with a lookalike display font — nothing will match
it, and the near-miss looks worse than an honest contrast.

| Role | Family | Weights | Notes |
| --- | --- | --- | --- |
| Display | Archivo | 600, 700 | Tracking `-0.02em`. Blunt grotesque; holds its own beside heavy ink. |
| Body | Source Serif 4 | 400, 600 | Measure capped at 68ch. |
| Mono / data | IBM Plex Mono | 400, 600 | Code, IDs, figures. |

All three are SIL OFL 1.1. That is deliberate: **you can embed them in Unity and Unreal builds
without a licence problem.** Commercial foundry licences routinely exclude embedding in an
application binary, which is exactly what an XR module is. Do not swap these for a paid face
without reading the EULA's embedding clause first.

The heading-grotesque-plus-body-serif pairing also keeps long-form pedagogy and academic writing
credible. A sans-on-sans system reads as SaaS marketing, which undersells the research.

## Texture

Three permitted textures. They all come from print, because the mark comes from ink.

1. **Paper grain** — over full-bleed grounds only, `0.045` opacity. Never behind body copy at
   higher than that; it eats small type.
2. **Brush edge** — rough, drawn edges on containers and dividers, derived from the mark's own
   stroke. Rules are `2.5px`, not hairlines. Corner radius `2px` — the mark has no soft corners.
3. **Risograph misregistration** — a `2px` offset of a flat behind black type or a black shape.
   Use on covers and titles, sparingly. It reads as printed and human.

Prohibited, without exception: gradients, drop shadows, glassmorphism, glow, bevel, and
stock XR imagery with circuit-board or neural-network overlays. Every one of them fights the mark
and dates the brand to a vendor category you are trying to leave.

## Logo use

Clear space: the height of the wordmark's cap on all four sides. Minimum reproduction: 24mm wide
in print, 96px wide on screen — below that the eyes fill in and the forms go muddy.

Reproduce in Ink on Paper, or reversed Paper on Ink. It may sit on Ray. It may not sit on Pulse,
Breath or Deep — the black forms lose separation. Never recolour the mark itself, never outline it,
never add a strapline inside the lockup.

Credit Jean Jullien wherever the mark appears. Crediting was a condition of the original
permission and is the right thing regardless.

**Open issue:** the file in `logo/` is a 225 × 224 px raster with a baked white background. That is
a web thumbnail, not a master. Any vector or high-resolution artwork has to come from Studio Jean
Jullien — and asking for it is the same conversation as asking for the licence above, so do both at
once.

## XR-specific notes

Headset rendering punishes thin strokes and low contrast. Inside a build: raise minimum stroke
weight, never place type below AA, and prefer the Ink-on-Ray and Paper-on-Deep pairings, which
have the most headroom. Paper grain should be dropped entirely in-headset — at foveated
resolutions it turns into shimmer.

## What is actually in production

Measured from `BOR001_DL_Flyer_PROOF_V2` (DL, 100 × 210 mm), the first real artefact this kit has
been checked against. Worth recording, because the kit either matches it or departs from it
deliberately — it should never drift by accident.

| | In production | This kit | Note |
| --- | --- | --- | --- |
| Ink | `#0A0203` | `#14110F` | Same instinct — both warmed off pure black. The kit's is slightly lighter and more olive, which holds ink's character better at large sizes. Adopting it is a real change; make it a decision. |
| Paper | `#FFFFFF` | `#F6F1E7` | A genuine departure. Production is pure white; the kit proposes warm uncoated. Decide before the next print run. |
| Colour | none | four flats | The palette has no precedent in anything printed. Consistent with "ink and paper carry the brand", but it means the flats are untested. |
| Display | Permanent Marker | Archivo | See below. |
| Body | Merriweather 9 pt | Source Serif 4 | Small step; both serifs, same role. |
| Stray | Ubuntu 10 pt, 3 glyphs | — | Three characters in a fourth typeface. Almost certainly unintentional, and it drags a whole extra font embed into the print file. Remove. |

### Permanent Marker has to go

This is the single most consequential fix in the pack. Permanent Marker is a free Google font and
the default "handwritten" face on the internet. Setting headlines in it puts a mass-produced
imitation of hand-lettering directly beside genuine hand-lettering by a serious illustrator — and
the imitation doesn't borrow the real one's credibility, it lends it its own cheapness. The real
lettering starts to look like the same trick.

This is exactly the "don't chase the hand-lettering, contrast with it" rule above, and the flyer is
what happens when it isn't followed. Archivo in the display role fixes it: it makes no claim to be
handmade, so the wordmark stays the only handmade thing on the page and keeps all of its value.

### Print notes

Body copy on the flyer is 9 pt Merriweather reversed white out of near-black. That is a real print
risk rather than a screen one — reversed serifs at that size fill in on uncoated stock and thin out
on coated. Reversed type is for display. Body copy is ink on paper; if a dark ground is
unavoidable, set it in Archivo at 10 pt minimum, not a serif at 9.

The logo on the back sits inside a visible white box on a black ground — the baked-white-background
raster, showing up in production exactly as predicted. The front of the same flyer reverses
correctly, so usable artwork exists somewhere; the back is a dropped-in PNG. Another reason the
master-file request matters.

`www.TBC.com.au` is still a placeholder in a file named PROOF_V2. Check this was caught before any
print run.

## The ink field

The strongest device in the brand is already in use and was not written down, so it is written down
now. The flyer's front is a single full-bleed field of ink with a torn brush edge, the pair of eyes
knocked out in paper, and the wordmark beneath. No photograph, no colour, no explanation.

It is better than anything invented for this kit. It is confident, unmistakably the mark, and it
works at DL, at poster, and as a cover. Treat it as the primary layout for anything whose job is
recognition rather than information — covers, opening slides, back pages, merchandise.

Rules: the field bleeds off at least three edges; the edge is torn or brushed, never a straight cut
or a rounded rectangle; the eyes are knocked out to paper, never filled with a flat; and it carries
either the wordmark or a headline, never both plus body copy. If it needs body copy, it is the
wrong layout.

## Generation

Second influence: [someform](https://someform.studio/) — Matthias Winckelmann and Helge Kiehl,
Berlin. Their practice is identity built from logic, and they routinely hand clients bespoke
software so brand assets can be generated in-house rather than commissioned one at a time.

Be clear about what is and isn't borrowed. someform's rendered surface is simulated-photographic
— high-gloss procedural 3D, immaculate materials. Adopt that literally and it fights the ink mark;
you'd have two brands arguing on one page. What transfers is the **method**: define the identity
as rules, then build the tool that applies them. That is rendered here in this brand's own
vocabulary — flat shapes, ink, paper, riso offset.

This matters practically, not just philosophically. Course modules, XR scenes, cohort material and
partner decks are needed at volume, and there is no design team to draw each one.

`generate-cover.mjs` produces module artwork from a seed. It is deterministic: `BOR-114` resolves
to the same cover forever, so the decision never has to be stored, briefed or remembered.

```
node brand/generate-cover.mjs BOR-114
node brand/generate-cover.mjs BOR-114 --ratio social --out build/
node brand/generate-cover.mjs BOR-101 BOR-114 "Deteriorating Patient" --out build/
```

Ratios: `cover` (1200×1600), `social` (1200×630), `square` (1200×1200), `scene` (1920×1080).

The shape vocabulary is taken from the mark itself and nothing else — the arch (its lung/face
form), the ray bundle, the pair of eyes. Four composed archetypes keep output composed rather than
random: `arch-and-rays`, `the-pair`, `corner-rays`, `horizon`, `crew`. Adding to or reordering that
list reshuffles every existing seed, because the archetype is the first draw — lock it before
covers go into production. The seed also picks one of the four
flats and, about a quarter of the time, a reversed ink ground — which uses the dark-ground token
values, not tints, because Deep is only 2.54:1 against Ink and has to lift before it can sit on it.

Two rules govern the generated layer. It never uses more than ink, paper and one flat, same as
everything else. And it is a **backdrop** — type is set over it in the normal system, never
generated into the artwork, so covers stay legible and translatable.

If the mark licence resolves into a new commissioned mark rather than Jullien's *Us*, this
generator is the part of the kit that survives unchanged: swap the shape vocabulary, keep the
method.

### Characters

The mark's forms already read as figures with faces, so the cast is not an invention — it is the
mark at small scale. A crew is a row of three to five of them at varying heights, most wearing a
headset visor, one keeping the mark's own eyes so the family resemblance stays visible.

The visor sits exactly where the eyes sit. That substitution is the whole idea: these are our
people, and they are in headsets. The strap stops at the silhouette rather than running the full
head width — a band jutting into open paper reads as a mistake, not a headset.

**Headsets, not televisions.** A screen for a face is an old and free idea, but a boxy CRT with
rabbit-ear antennae, worn with a Napoleonic dress uniform, is a specific existing character —
Prince Robot IV, from *Saga* (Brian K. Vaughan and Fiona Staples, Image Comics). That book is
actively published and heavily merchandised. Anything with those specifics reads as their
character no matter what we call it, and this brand cannot afford a second rights problem on top
of the mark.

A visor avoids all of it and is the stronger choice anyway: a nurse in a VR headset is literally
what this company does, so the cast says the business out loud and cannot be mistaken for anyone
else's. Keep the figures flat, keep them silent, give them no antennae, no uniform, and nothing
playing on the screen.

## Files

- `tokens.css` — CSS custom properties, including a dark-ground inversion.
- `tokens.json` — the same values as design tokens, with contrast ratios and warnings inline.
- `generate-cover.mjs` — procedural cover generator. Deterministic, no dependencies.
- `logo/bundle-of-rays-primary.png` — placeholder raster. See open issue above.

## Status

v0.1 working draft. Blocked on the licence question above, and on palette sign-off.
