# Canonical numbers — the one set every document must match

**Stood up 30 Aug 2026.** The data room's core defect is four price lists, three unit
costs, five ownership structures and two TAMs. This page is the antidote: one value per
item, its source, and its status. **No document enters the UCAC pack until it agrees
with this page.** CONFIRMED = decided by Brad or evidenced; RECOMMENDED = the agent's
resolution awaiting Brad's yes.

| Item | Canonical value | Source / basis | Status |
|---|---|---|---|
| BVUIP structure | **$300k POC + $1.0M commercialisation = $1.3M total; each round 50/50 ACU : Innovation Victoria** | Brad, 30 Aug 2026 | **CONFIRMED** — Russell's written confirm requested |
| ACU cash obligation | **$650,000** ($150k POC + $500k commercialisation) | Arithmetic of the above | CONFIRMED (as obligation; source of funds open) |
| BVUIP accounting | Financing (SAFE converting to equity), **not** grant income | Business Plan §6 vehicle description | RECOMMENDED — needs CFO |
| TRL | **3, climbing** — 4 is claimed only when recall@5 ≥ 0.85 and safety-tag ≥ 0.95 against the gold-standard eval set | Business Plan §3, held deliberately | **CONFIRMED** — GTM v2.1 and forecast Cover must be corrected to match |
| B2B price list | **The Pricing Model's schedule is canonical: $28,000 / $48,000 / $72,000 / $95,000**, banded by births per year (≤500 / 501–1,500 / 1,501–3,500 / 3,500+) with an explicit **included-enrolled-mothers cap** at each tier (300 / 900 / 2,000 / 5,000). Model gross margins 70 / 61 / 47 / 6%. **Plus a new entry tier at $18,000 for 150 included mothers (24.8% GM)** as the pilot on-ramp; Enterprise needs an inclusion cap with per-mother overage. | Pricing Model sheet 4, read directly | RECOMMENDED — **retires the Business Plan's $25k/$45k/$65k list**, which is 12–15% below it and caused a real costing error on 30 Aug |
| Cohort definition | **20 weeks gestation to 12 months postnatal** | BMC + Product Overview, both 30 Jun 2026 | CONFIRMED |
| Gold-standard eval set | **200–300 queries** (Business Plan) — Quality & Safety Strategy says 100–200 | Business Plan §7 is the later document | RECOMMENDED |
| Pedagogical framework name | **UNKNOWN** — BMC says *AIAP-F*, the PhD's construct is the *AAF (Andragogical Agent Framework)* | — | OPEN |
| Enterprise tier | Two-part tariff with a hard active-mother cap; overage capped or removed | Unit Economics gating item | RECOMMENDED — resolve before any procurement |
| Unit cost per active mother | **Falls with scale: AUD $70.49 / $52.04 / $47.88 / $44.60 per year** at the Foundation / Standard / Network / Enterprise scale points. Avatar video is **69–80%** of it; the entire rest of the platform is $13.95. **Plus AUD $9,300/yr platform support, fixed per tenant**, which the model excludes by design (Cost Engine row 21). | Cost Engine row 26, read directly — `finance/unit_cost_model.py` | **CONFIRMED.** The "three values across 4.8×" were scale points of one engine — $44.60 and $70.44 are both in that row |
| Churn | **10% institutional** (10-year life); 25% B2C | Unit Economics, the venture's own assumption | CONFIRMED (consistency rule) |
| Base case geography | Victorian + Australian only; India, UK/USA and their XR share in a **labelled upside scenario** | Brad, 30 Aug ("fix as you think best" on scalability) | CONFIRMED |
| Peak cumulative burn | **≈$770k per current model** (restated base likely higher); the "$0.15M" claim is retired | Forecast Funding tab | CONFIRMED as the honest figure |
| FY27 funding need | **≈$1.0M incl. 3-month buffer; ≈$720k beyond the POC** | Restatement workbook | RECOMMENDED — CFO to verify |
| Ownership structure | **HOLDING LINE — do not state a structure.** Every document uses one sentence and no more: *"The ownership and shareholding structure of Kindred Care Pty Ltd is to be set out in the Heads of Agreement, currently in preparation with ACU."* Background IP position is separable and stays stated (below). | Brad, 30 Aug 2026 — awaiting ACU's draft approach | **CONFIRMED as the holding line.** Retire "70/30", "held by BoR", and every other specific split from all documents now |
| TAM — Victoria | **52 maternity health service providers, 33 of them regional** | Victorian Premier's office / Maternity Taskforce | **RECOMMENDED — supersedes the Business Plan's "75+ facilities". Use the state's own number** |
| TAM — national | **~285 AU institutions** (~250 maternity services + ~35 universities); ~310,000 births | Forecast Cover (tighter of the two counts) | RECOMMENDED |
| Victorian policy anchors | **Victorian Maternity Taskforce — nine recommendations, government committed; first Chief Midwife appointed to implement; Respectful Maternity and Newborn Care Framework (SCV, 6 Jan 2026); My Maternity Journey consumer platform, completing 2026; MCoC scale-up** | Public reporting — verify against primary sources | RECOMMENDED — **not currently in any pack document** |
| Platform IP | Multi-tenant platform (GCP, ADK, Gemini, Vertex, Cloud Run, admin, analytics) = **BoR background IP** | Business Plan §5; MVP Board (bor-iridia) | **CONFIRMED** — IP Plan 0.3 to correct |
| Forecast period label | **FY2027–FY2031**, one model; V9 (16/10/25) retired, Pricing Model re-baselined | Second-pass review | RECOMMENDED |
| Product language | The Companion · midwifery- and nurse-led · education-only · workforce and equity | Register locks | CONFIRMED |

## The five price lists — for the consolidation pass

| Tier band | Business Plan | Unit Economics | **Product Overview** | Pricing Model | Forecast FY27 |
|---|---|---|---|---|---|
| Small | $25,000 (<500) | $28,000 (<500) | **$17,500 "from"** (<500) | tiered by active mothers | $16,200 |
| Medium | $45,000 (500–2,000) | $48,000 (501–1,500) | **$35,000** (500–2,000) | — | $32,250 |
| Large | $65,000 (2,000–4,000) | $72,000 (1,501–3,500) | **$55,000** (>2,000) | — | $59,679 |
| Enterprise | $95,000 + overage (4,000+) | $95,000 (3,500+) | **absent** | — | absent |

Five schedules, three sets of band boundaries, two tier-name sets. **The Product Overview
is the document headed "INVESTOR DATA ROOM"** and carries the second-lowest prices.
Consolidate to the canonical row above.

## The tier table, verified against the model's own cells

| Tier | Births/yr | Licence | Included (enrolled) | Active | Variable cost | GM | GM incl. support |
|---|---|---|---|---|---|---|---|
| Foundation | up to 500 | $28,000 | 300 | 120 | $8,459 | **69.8%** | 36.6% |
| Standard | 501–1,500 | $48,000 | 900 | 360 | $18,735 | **61.0%** | 41.6% |
| Network | 1,501–3,500 | $72,000 | 2,000 | 800 | $38,301 | **46.8%** | 33.9% |
| Enterprise | 3,500+ | $95,000 | 5,000 | 2,000 | $89,206 | **6.1%** | **−3.7%** |

Sheet 4 publishes 70 / 61 / 47 / 6. Reproduced exactly. **Three of four tiers are healthy**
— 34–42% even after loading the AUD $9,300 fixed platform support the model excludes.

Two features of this schedule matter and are easy to miss:

- **Every tier caps included enrolled mothers well below the birth volume.** Foundation
  covers 300 enrolled at a service doing up to 500 births. The licence buys a cohort, not a
  catchment. Costing a tier against its whole birth volume overstates cost badly — that is
  the error the 30 Aug first-pass review made.
- **Unit cost falls with scale**, $70.49 → $44.60 per active mother per year, because the
  modelled HeyGen rate drops from $0.19 to $0.103 USD/min with volume. Applying one figure
  across all tiers is wrong in both directions.

## The proposed entry tier — Brad's sub-$20k question

Foundation's constraint is not its price, it is that AUD $9,300 of fixed per-tenant support
sits under a small cohort. Cut included mothers, not price:

| Included (enrolled) | Active | Cost | GM at $18,000 | Support as % of cost |
|---|---|---|---|---|
| 100 | 40 | $12,120 | **32.7%** | 77% |
| **150** | **60** | **$13,530** | **24.8%** | **69%** |
| 200 | 80 | $14,940 | 17.0% | 62% |
| 300 | 120 | $17,759 | 1.3% | 52% |

**Recommended: $18,000 for 150 included mothers, 24.8% GM.** A genuine first-pilot cohort,
so the price is honestly small rather than structured to look small — which keeps it clear
of the contract-splitting line. Clears a $20k threshold and slots below Foundation without
disturbing the tiers above. The real trade-off is not margin but whether 150 mothers
generate enough evaluation evidence; 100 pays better and may be too thin.

## Two pricing rules that are not about the number

**Watch the reference price.** Transparency in Victorian public health is high — FOI,
procurement disclosure, and a small peer network of maternity directors. Whatever site one
pays becomes the anchor. The model already carries discount caps (Assumptions 1.4: 25%
routine, 35% foundation customer, 50% pilot for 6 months with Pricing Committee approval) —
use the **entry tier** as the on-ramp rather than discounting Foundation, so the discount
caps stay unspent and the list price stays intact.

**Set the entry band against the procurement threshold deliberately.** Thresholds vary by
each service's own policy and are unverified — and usually attach to *total contract value
over the term*, so a three-year deal at $18,000/yr is a $54,000 procurement. Confirm before
any strategy rests on it.

## The gate — restated twice on 30 Aug; this is the correct version

An earlier version of this page claimed every tier was loss-making. **That was wrong and is
retracted.** It costed the Business Plan's prices against the Pricing Model's cohort, used
the Foundation unit cost at every scale point, and read birth volume as enrolled volume.

What is actually gating:

1. **Enterprise at 6.1%, −3.7% after support.** The model flags it. The fix is the inclusion
   cap with per-mother overage — not the list-price rise written beside it, which only
   reaches 6.0% after support.
2. **D-23, the LiveAvatar vendor decision.** Avatar video is 69–80% of variable cost, and
   D-23 is carried out-of-loop on the MVP Board rather than on the critical path.
3. **Two unmeasured assumptions everything rests on** — 40% engagement and 40 avatar minutes
   per active mother per month. The model itself says engagement *"must be tracked from Day
   1 of pilot."*

**Prices may be quoted internally against the Pricing Model schedule. Nothing goes to a
buyer before D-23.** Full working, including the four errors in the first version, in
`kindred-care/finance/2026-08-30-unit-cost-resolved.md`.

## Documents that already meet the standard

Worth naming, because they are the template for the rest:

- **Business Model Canvas v1.0** — locks correct, investor unnamed, and the ACU
  relationship described exactly as the probity rule requires: *"an active, multi-pathway
  partnership exploration, not a confirmed commercial partnership."* Copy this framing.
- **Product Overview v1.0** — TRL 3 stated correctly, *"Bundle of Rays owns the underlying
  platform"* stated correctly, institutional investor unnamed.

Both are dated 30 Jun 2026 — one day before GTM v2.1, which breaks the locks they follow.

**Rule:** a change to any row propagates to every document the same week, and the row's
source column is updated. This page is the consistency sweep's checklist.
