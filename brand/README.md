# Bundle of Rays — brand kit

Version 1.0. Governed by [`DESIGN.md`](./DESIGN.md), which is authoritative.

| File | What it is |
| --- | --- |
| [`DESIGN.md`](./DESIGN.md) | The house visual system. Authoritative — where this kit disagrees, it is wrong. |
| [`BRAND.md`](./BRAND.md) | The brand: mark, colour, typography, texture, generation, applications, governance. |
| [`tokens.css`](./tokens.css) | Custom properties. Every ratio computed and commented. |
| [`tokens.json`](./tokens.json) | The same values as design tokens, with warnings, amendments and status. |
| [`brand-kit.html`](./brand-kit.html) | The visual kit. Self-contained; opens in any browser. |
| [`generate-cover.mjs`](./generate-cover.mjs) | Procedural cover generator. Deterministic, no dependencies. |
| [`logo/`](./logo) | The mark, plus derived transparent ink and paper versions. |

## Three blockers before sign-off

1. **Licence.** The mark is Jean Jullien's artwork *Us*. The permission on record (Studio Jean
   Jullien, 02 Jun 2025) covers *The Just Us Show* only — "limited to this project only", no fee,
   no ongoing use — and the wordmark lockup is an ungranted derivative. A written licence for
   company identity is required.
2. **Master artwork does not exist.** The only supplied asset is 225 × 224 px with a baked white
   background. The transparent ink and paper versions in `logo/` are derived from it, not from
   originals, and are not fit for print, signage, garments or XR textures.
3. **Five contrast amendments** proposed in `BRAND.md` await sign-off in `DESIGN.md`, including
   `--state-caution`, which fails even the 4.5:1 floor and cannot carry type.

## Quick use

```bash
node brand/generate-cover.mjs BOR-114 --ratio social --out build/
```

Ink, paper and one accent. Red, amber and green are reserved for genuine clinical state and are
never brand colours.
