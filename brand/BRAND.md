# Bundle of Rays — Brand Kit

Version 0.1 — 03 Sep 2026. Working draft.

## The premise

The primary mark was drawn by [Jean Jullien](https://en.wikipedia.org/wiki/Jean_Jullien_(designer)):
two black brush-ink forms that read as lungs and as a pair of faces in profile, above hand-lettered
type. It is warm, human, slightly funny, and completely un-clinical.

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

**Open issue:** the file in `logo/` is a 225 × 224 px raster. That is a web thumbnail, not a
master. Source the original vector or high-resolution artwork from Jean Jullien's studio before
any print, signage, garment or XR-texture use — everything above 96px will fall apart otherwise.

## XR-specific notes

Headset rendering punishes thin strokes and low contrast. Inside a build: raise minimum stroke
weight, never place type below AA, and prefer the Ink-on-Ray and Paper-on-Deep pairings, which
have the most headroom. Paper grain should be dropped entirely in-headset — at foveated
resolutions it turns into shimmer.

## Files

- `tokens.css` — CSS custom properties, including a dark-ground inversion.
- `tokens.json` — the same values as design tokens, with contrast ratios and warnings inline.
- `logo/bundle-of-rays-primary.png` — placeholder raster. See open issue above.
