# Tier economics, read from the model's own cells

**30 Aug 2026, rewritten same day after Brad challenged the first version.** The first
version of this file claimed every tier was loss-making. **That was wrong.** What follows
is rebuilt from the actual cell values in sheets 1, 2 and 4, and reproduces the model's
published margins exactly. Reproducible: `kindred-care/finance/unit_cost_model.py`.

---

## What I got wrong, and why it matters beyond this file

Four errors, all pushing the same way:

1. **I costed the Business Plan's price list against the Pricing Model's cohort.** The
   Pricing Model's tiers are **$28,000 / $48,000 / $72,000 / $95,000**, not the
   $25k/$45k/$65k/$95k I used. Roughly 12–15% low on price at every tier.
2. **I treated birth volume as enrolled volume.** Sheet 4 has an **"Included mothers
   (enrolled)"** column that caps the cohort well below births — Foundation covers 300
   enrolled mothers at a service doing up to 500 births. I costed every mother in the
   catchment.
3. **I used one unit cost at every scale point.** Cost Engine row 26 shows it falling with
   volume: AUD **$70.49 → $52.04 → $47.88 → $44.60** per active mother per year. I applied
   the Foundation figure ($70.49) everywhere, overstating cost by up to 58% at the top.
4. **I added platform support to the model's margins and then reported them as the
   model's.** The Cost Engine sets it to zero on purpose (row 21) — the cover flags
   apportionment as open review item (2). Showing it as a sensitivity is fair; presenting
   the result as the model's own number was not.

**The lesson is bigger than the arithmetic.** The five-price-list problem I have been
flagging since 29 Aug is exactly what caught me: I pulled a price from one document and a
cost from another and did not check they described the same thing. That is precisely the
failure an investor would hit. It is now the strongest argument for the consistency sweep.

---

## The model's actual tier economics — verified

| Tier | Births/yr | Licence | Included (enrolled) | Active | Variable cost | GM | GM incl. support |
|---|---|---|---|---|---|---|---|
| Foundation | up to 500 | $28,000 | 300 | 120 | $8,459 | **69.8%** | 36.6% |
| Standard | 501–1,500 | $48,000 | 900 | 360 | $18,735 | **61.0%** | 41.6% |
| Network | 1,501–3,500 | $72,000 | 2,000 | 800 | $38,301 | **46.8%** | 33.9% |
| Enterprise | 3,500+ | $95,000 | 5,000 | 2,000 | $89,206 | **6.1%** | **−3.7%** |

Sheet 4 publishes 70 / 61 / 47 / 6. Reproduced exactly. **The model is internally sound and
three of its four tiers are healthy** — 34–42% gross margin even after loading the fixed
platform support the model excludes.

**So the pack does not describe a business that loses money on every sale.** My earlier
claim to that effect was false and should not reach anyone.

---

## What does survive, and still matters

### 1. Enterprise is broken, and the model says so itself

6.1% before overhead, **−3.7% after**. The cover's warning is correct and its own remedy is
only half right: raising list to $135k gives 6.0% after support — still thin. **Capping
inclusions at ~3,000 enrolled with a per-active-mother fee above the ceiling is the fix**,
and it is the option written as a maybe. Do both if Enterprise is to survive contact with a
real 4,000-birth service.

### 2. Avatar video is 69–80% of variable cost

| Tier | Variable/active/yr | Avatar | Everything else |
|---|---|---|---|
| Foundation | $70.49 | $56.54 (80%) | $13.95 |
| Standard | $52.04 | $38.09 (73%) | $13.95 |
| Network | $47.88 | $33.93 (71%) | $13.95 |
| Enterprise | $44.60 | $30.65 (69%) | $13.95 |

Gemini, Vertex, Search, Cloud Run and storage together cost $13.95 per active mother per
year. The talking head costs two to four times the entire rest of the platform. **This
holds, and it means D-23 (the LiveAvatar vendor decision, still open on the MVP Board) sets
the venture's gross margin.** It is not a crisis — the margins work — but it is the single
biggest lever on them, and it is currently carried out-of-loop rather than on the critical
path.

**Correction within the correction:** I said Hector's larger-bundle rate was "never
actioned." Wrong — Cost Engine row 13 already models the rate falling with volume
($0.19 → $0.128 → $0.114 → $0.103 USD/min). His comment annotates a bundle rate that is
in the model.

### 3. Platform support is the binding constraint at small scale

AUD $9,300/year, **fixed per tenant**. At Foundation it is *larger than the entire variable
cost* ($9,300 vs $8,459) and takes the tier from 70% to 37%.

This is the real, well-founded version of the regional-network argument: it is not that
small services are unprofitable — Foundation makes 37% all-in. It is that **the fixed
per-tenant line dominates their cost base**, so ten regional services under one tenant pay
$9,300 once instead of $93,000. The conclusion survives; the reasoning is now sound.

### 4. Three input problems, all real

- **Cost Engine row 11 hardcodes video uptake at 40%; Assumptions 1.2 says 35%**, and the
  note beside that cell still reads "75%". Three values for one input. The error is
  conservative (overstates cost), but it sits in the cell everything derives from.
- **Engagement at 40% is unvalidated** and the model says so in bold — *"must be tracked
  from Day 1 of pilot."* Every margin above moves with it.
- **Enrolled period is 12 months**, but the cohort is 20 weeks gestation to 12 months
  postnatal, ≈16.6 months. Understates enrolled mothers by ~38%.
- Sheet 4's own flag reads *"if engagement tracks at <60% it may be loss-making"* — that is
  backwards. Lower engagement means fewer active mothers against a fixed licence, so higher
  margin. Minor, but it is a note Hector is being asked to act on.

---

## Brad's actual question: can an entry tier sit under $20,000?

**Yes — by cutting included mothers, not by cutting price.** Foundation's problem is not
the licence, it is that $9,300 of fixed support sits under a small cohort.

| Included (enrolled) | Active | Cost | GM at $18,000 | GM at $19,500 | Support as % of cost |
|---|---|---|---|---|---|
| 100 | 40 | $12,120 | **32.7%** | 37.8% | 77% |
| 150 | 60 | $13,530 | **24.8%** | 30.6% | 69% |
| 200 | 80 | $14,940 | 17.0% | 23.4% | 62% |
| 250 | 100 | $16,349 | 9.2% | 16.2% | 57% |
| 300 | 120 | $17,759 | 1.3% | 8.9% | 52% |

**Recommendation: an entry tier at $18,000 covering 150 enrolled mothers — 24.8% gross
margin.** That is a genuine first pilot cohort, so the price is honestly small rather than
structured to look small, which keeps it clear of the contract-splitting line. It clears a
$20k threshold, and it slots below Foundation without disturbing the four tiers above it.

At 100 enrolled it reaches 33% and is even safer, but 100 mothers may be too thin to
generate the evaluation evidence the pilot exists to produce. **150 is the balance between
margin and statistical usefulness — and that trade-off, not the price, is the decision.**

---

## What actually changes in the pack

- **The tier prices are not the problem.** Stop redesigning them. The Pricing Model's
  $28k/$48k/$72k/$95k schedule is defensible at three of four tiers.
- **Fix Enterprise** — inclusion cap plus per-mother overage above the ceiling.
- **Add the sub-$20k entry tier** at 150 included mothers, as the pilot on-ramp.
- **Adopt the Pricing Model's schedule as canonical** and retire the Business Plan's
  $25k/$45k/$65k list. Two schedules 12–15% apart is what caused this error; it will cause
  someone else's.
- **D-23 goes on the critical path.** It sets 69–80% of variable cost.
- **Instrument avatar minutes and engagement per mother from pilot day one.** The model's
  own two most load-bearing assumptions, neither measured.
- **Related-party note:** platform support and setup are ClinOps costs, and ClinOps is
  Hector's company. Normal and disclosable; an investor will ask.
