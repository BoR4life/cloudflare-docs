# Pricing doctrine

Read before any pricing, quoting, tier, forecast-revenue or procurement work.
The canonical numbers live in `kindred-care/canonical-numbers.md`; this file is the
reasoning behind them, so the agent defends the position rather than reciting it.

## The first principle: category sets the ceiling, not the feature set

Whatever the Companion is called decides what it can be sold for, before a single
capability is discussed.

**"Patient education" has no budget line.** No Australian public health service holds a
patient-education cost centre with tens of thousands of discretionary dollars in it. A
buyer who files the Companion there will compare it to Raising Children Network, hospital
handouts and every free pregnancy app, and it becomes the first thing cut in a tight year.

**Workforce capacity and equity of access do have budget lines**, and they are the
Victorian Maternity Taskforce's own stated problems. Same product, same price tag, a
category where the number is defensible.

So: **the framing lock is a pricing control, not a messaging preference.** If a document
drifts into patient-education language, the price schedule in that document is already
undefended. Fix the framing before arguing the number.

## The schedule — the Pricing Model's, read from its own cells

| Tier | Births/yr | Licence | Included (enrolled) | Active | GM | GM incl. support |
|---|---|---|---|---|---|---|
| Foundation | up to 500 | $28,000 | 300 | 120 | 69.8% | 36.6% |
| Standard | 501–1,500 | $48,000 | 900 | 360 | 61.0% | 41.6% |
| Network | 1,501–3,500 | $72,000 | 2,000 | 800 | 46.8% | 33.9% |
| Enterprise | 3,500+ | $95,000 | 5,000 | 2,000 | 6.1% | **−3.7%** |
| *proposed entry* | *pilot cohort* | *$18,000* | *150* | *60* | *—* | *24.8%* |

**This retires the Business Plan's $25k/$45k/$65k schedule**, which sits 12–15% below and
caused a real costing error on 30 Aug. When a price and a cost come from different
documents in this venture, check they describe the same thing before doing arithmetic.

Three things about this table the agent must not lose:

1. **Every tier caps included enrolled mothers well below the birth volume.** Foundation
   covers 300 enrolled at a service doing up to 500 births. The licence buys a **cohort, not
   a catchment.** Costing a tier against its full birth volume overstates cost badly.
2. **Unit cost falls with scale** — AUD $70.49 / $52.04 / $47.88 / $44.60 per active mother
   per year, because the modelled avatar rate drops from $0.19 to $0.103 USD/min with
   volume. Never apply one figure across all tiers.
3. **Platform support is AUD $9,300/yr, fixed per tenant**, and the model excludes it from
   tier margins by design (Cost Engine row 21; cover review item 2). Quote model margins and
   all-in margins as two separate numbers, and say which is which.

## The entry tier: cut included mothers, not price

Brad's direction on 30 Aug was that the lowest tier sit under $20,000 to clear a procurement
threshold. Foundation's constraint is not its price — it is that $9,300 of fixed support
sits under a small cohort. So reduce inclusions:

| Included (enrolled) | Active | Cost | GM at $18,000 | Support as % of cost |
|---|---|---|---|---|
| 100 | 40 | $12,120 | 32.7% | 77% |
| **150** | **60** | **$13,530** | **24.8%** | **69%** |
| 200 | 80 | $14,940 | 17.0% | 62% |
| 300 | 120 | $17,759 | 1.3% | 52% |

**$18,000 for 150 included mothers.** A genuine first-pilot cohort, so the price is honestly
small rather than structured to look small — which keeps it clear of the contract-splitting
line. It slots below Foundation without disturbing the tiers above, and it means the model's
discount caps (Assumptions 1.4: 25% routine, 35% foundation, 50% pilot for six months) stay
unspent, so the list price survives the first sale. The real trade-off is not margin — it is
whether 150 mothers generate enough evaluation evidence. 100 pays better and may be too thin.

## Avatar video is 69–80% of variable cost

| Tier | Variable/active/yr | Avatar | Everything else |
|---|---|---|---|
| Foundation | $70.49 | $56.54 (80%) | $13.95 |
| Enterprise | $44.60 | $30.65 (69%) | $13.95 |

Gemini, Vertex, Search, Cloud Run and storage together cost $13.95 per active mother per
year. The talking head costs two to four times the entire rest of the platform.

The margins work, so this is a lever rather than a crisis — but it is the **biggest single
lever on gross margin the venture has**, and it is controlled by one open decision. Hector's
larger-bundle rate is already modelled (Cost Engine row 13, falling $0.19 → $0.103), so the
remaining question is product shape: is avatar video standard, capped, or a metered premium?

## The bottom tier and the regional network

**33 of Victoria's 52 maternity providers are regional** — small, and mostly Foundation or
the entry tier. That is not unprofitable: Foundation makes 37% all-in.

The problem is shape, not viability. **Platform support is fixed per tenant, and at
Foundation it exceeds the entire variable cost** ($9,300 against $8,459). So ten regional
services under one tenant pay $9,300 once instead of $93,000. Sell **one regional network
licence** with small services as covered sites — the same answer as the central/state
licence below, reached from the cost side, which is a reason to believe it.

## The probity line on thresholds

Pricing an entry engagement so it genuinely sits under a threshold is legitimate when **the
engagement is genuinely that small** — which is why the entry tier is defined by a real
150-mother cohort rather than by a discount. Structuring a known larger deal to sit under a
threshold, or splitting it into several small contracts, is contract splitting; procurement
officers are trained to find it, and this venture carries ACU's name.

Two things the agent states whenever thresholds come up:

- **Thresholds usually attach to total contract value over the term, not annual value.** A
  three-year agreement at $18,000 a year is a $54,000 procurement. Verify before any
  strategy rests on it.
- A small pilot buys **speed to first evidence**, not permanent avoidance of procurement.
  Say so to the buyer rather than let them discover it.

## Above the tiers: the central/state licence

The largest plausible first deal is not twenty services at $65k. It is a state programme —
Safer Care Victoria, or Taskforce implementation funding — buying once for all Victorian
public maternity. Different contract, different number, and **absent from every model**.
Price it as a per-service-equivalent rate falling with scale, with a floor. Route it via
Russell; Elisa McDonald sits at the junction of the Taskforce, SCV and My Maternity Journey.

## Two rules that are not about the number

**Pilots at list price, funded externally.** Price transparency in Victorian public health
is high — FOI, procurement disclosure, and a small peer network of maternity directors who
talk to each other. Site one's price becomes the permanent reference price. So the pilot is
paid at list from grant or programme money and the concession is taken **in-kind**:
evaluation design, co-design workshops, academic co-authorship. Identical economics for the
buyer, list price protected, and a truer description of the exchange. This supersedes the
"three-year pilot discount stepping to list" mechanic.

**Set the entry band against the procurement threshold on purpose.** Where $25,000 sits
relative to a service's direct-engagement threshold decides whether a first sale takes six
weeks or six months. Thresholds vary by each service's own policy and are unverified —
confirm per target site. Landing under the threshold is worth more than the revenue
difference between tiers.

## The gate

**Not unit cost — that is known** (AUD $70.49 → $44.60 per active mother per year by scale
point, Cost Engine row 26). Three of four tiers are healthy. What actually gates:

1. **Enterprise at 6.1%, −3.7% after platform support.** The model flags it itself. The fix
   is the inclusion cap with per-mother overage above the ceiling — not the list-price rise
   written beside it, which only reaches 6.0% after support. Do both if Enterprise is to
   survive contact with a real 4,000-birth service.
2. **D-23, the LiveAvatar vendor decision** — 69–80% of variable cost, carried out-of-loop
   on the MVP Board rather than on the critical path. Report its age at every checkpoint
   alongside the two ACU-side blockers.
3. **Two unmeasured assumptions everything rests on.** Engagement at 40% (the model says in
   bold: *"must be tracked from Day 1 of pilot"*) and 40 avatar minutes per active mother
   per month, which Hector himself hedged. Neither has ever been measured.

Also live, all real and all in the model's own cells: Cost Engine row 11 hardcodes video
uptake at 40% where Assumptions says 35% and the note beside it says 75%; the enrolled
period is 12 months where the cohort is ~16.6; and sheet 4's flag reads *"if engagement
tracks at <60% it may be loss-making"*, which is backwards.

**Prices may be quoted internally against the Pricing Model schedule. Nothing goes to a
buyer before D-23.**

Working: `kindred-care/finance/2026-08-30-unit-cost-resolved.md`, reproducible via
`kindred-care/finance/unit_cost_model.py` — which also records the four errors in the first
version of that analysis, because the failure mode is instructive: a price from one document
costed against a cohort from another.

## Forecast rule

The downside case assumes **revenue is grant and programme money for the first 24 months**,
not health-service operating budgets. A base case that has hospitals paying from operating
budgets in year one is describing the exception, not the rule.

## The hard stop

The agent sets positions and defends logic. It does not give pricing or procurement advice
that binds — a quote to a real buyer, a tender response, or a contracted rate goes to Brad,
and a contracted rate below list goes to Brad with the reference-price consequence stated.
