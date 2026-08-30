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
| B2B price list | **Three tiers anchored to births per year: <1,000 = $25,000 · 1,000–2,500 = $45,000 · 2,500+ = $65,000.** Plus a separate central/state licence line (not a fourth tier). **Pilots at list price, funded externally; concession taken in-kind, never as a discounted dollar figure.** | Brad, 30 Aug 2026 — direction on pricing | RECOMMENDED — **stays RECOMMENDED until unit cost closes.** Five schedules currently in the room, see below |
| Cohort definition | **20 weeks gestation to 12 months postnatal** | BMC + Product Overview, both 30 Jun 2026 | CONFIRMED |
| Gold-standard eval set | **200–300 queries** (Business Plan) — Quality & Safety Strategy says 100–200 | Business Plan §7 is the later document | RECOMMENDED |
| Pedagogical framework name | **UNKNOWN** — BMC says *AIAP-F*, the PhD's construct is the *AAF (Andragogical Agent Framework)* | — | OPEN |
| Enterprise tier | Two-part tariff with a hard active-mother cap; overage capped or removed | Unit Economics gating item | RECOMMENDED — resolve before any procurement |
| Unit cost per active mother | **UNKNOWN** — three documents say ~$14.70 / $44.60 / $70.44 a year | Hector to settle (email drafted) | **OPEN — blocks every margin claim** |
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

## Why the bands change unit — and a band error nobody has caught

Every existing schedule bands by **active mothers**. Health services do not know that
number and cannot verify it; they know **births per year** exactly, and publish it.
Banding by births makes the price a rate a buyer can self-select against instead of a
quote they have to argue about.

The two units are not interchangeable, and the conversion has been missed. The cohort
runs 20 weeks gestation to 12 months postnatal — about **16.6 months, or 1.38 years**.
So at steady state:

> **active mothers ≈ births per year × 1.38**

Which means the current bands sit roughly here in birth terms:

| Existing band (active mothers) | Actually corresponds to |
|---|---|
| <500 | <360 births/year |
| 500–2,000 | 360–1,450 births/year |
| 2,000–4,000 | 1,450–2,900 births/year |
| 4,000+ | 2,900+ births/year |

**A 2,000-birth service is a ~2,760-active-mother service.** Under the existing schedule
it lands in the *Large* band at $65k, not the *Medium* band a reader would assume. Any
quote built by eyeballing births against the current table is wrong by one tier. This
is a live pricing error, not a presentational one — flag it to Hector alongside unit cost.

## The three-tier schedule, and what sits above it

| Tier | Births per year | Annual licence |
|---|---|---|
| 1 | under 1,000 | **$25,000** |
| 2 | 1,000 – 2,500 | **$45,000** |
| 3 | over 2,500 | **$65,000** |

Four tiers is one too many for a product with no reference customer — it invites a buyer
to negotiate down the ladder. Three, with the top band open-ended, removes that move.
The retired $95k Enterprise tier is not lost: it becomes the floor of the central licence.

**The central/state licence — missing from every model.** The most likely large first
deal is not twenty health services at $65k. It is a state programme — Safer Care Victoria,
or Taskforce implementation funding — buying once, centrally, for all Victorian public
maternity. Different contract shape, different number, and **it does not appear anywhere
in the pricing model or the forecast.** With Elisa McDonald sitting at the junction of the
Taskforce, Safer Care Victoria and My Maternity Journey, it may also be the nearest one.
Model it as a per-service-equivalent rate falling with scale, with a floor.

## Two pricing rules that are not about the number

**1. Pilots at list price, funded externally.** Price transparency in Victorian public
health is high — FOI, procurement disclosure, and a small peer network of maternity
directors who talk. Whatever site one pays becomes the reference price permanently, and
site two's procurement team will find it. So the pilot is **paid at list from grant or
programme money**, and the concession is taken in-kind: BoR contributes the evaluation
design, the co-design workshops and the academic output. Identical economics for the
customer, list price protected, and a more accurate description of the actual exchange.
*This supersedes the "3-year pilot discount stepping to list" mechanic.*

**2. Set the entry band against the procurement threshold, deliberately.** Where $25,000
sits relative to a health service's direct-engagement threshold decides whether a first
sale takes six weeks or six months. Thresholds vary by each service's own procurement
policy and are **not verified** — Lois or Marie to confirm for the target sites. If the
entry band can be set below the threshold on purpose, that is worth more than the revenue
difference between tiers.

## The gate

None of the above converts from RECOMMENDED to CONFIRMED while **unit cost is stated
three ways across 4.8×** ($14.70 / $44.60 / $70.44 per active mother per year, open since
May). Clinical governance cost — Agent B supervision, clinical review, RAG corpus
maintenance — is largely fixed and does not shrink for a small site, so **Tier 1 at $25k
may be below cost.** Unit cost is the gate. Everything else in pricing is estimation until
Hector closes it.

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
