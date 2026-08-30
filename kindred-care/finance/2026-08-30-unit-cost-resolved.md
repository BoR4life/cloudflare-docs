# Unit cost is not unknown — and every tier is underwater

**30 Aug 2026.** Rebuilt from Hector's own cost engine, not from the summary figures
carried in the pack. Reproducible: `kindred-care/finance/unit_cost_model.py`.

**Sources.** `BoR AI Avatar Pricing` (owner hector@clinops.cloud, last modified 2 Mar
2026) — the original cost engine. `Kindred Care - Pricing Model_v1_DRAFT_Brad_May1_26`
sheets 1–4, which state on their own cover that they are *"a generalised version of the
BLS / Cultural / Oncology cost blocks Hector developed in BoR_AI_Avatar_Pricing.xlsx."*

---

## 1. The blocker was mis-stated. Unit cost is knowable today.

I have been reporting *"unit cost stated three ways across 4.8×, blocks every margin
claim, open since May."* That framing was wrong and it cost time.

The model publishes **AUD $5.87 per active mother per month** on sheet 3 (Margin Tiers).
Rebuilding it from Hector's inputs reproduces that figure exactly:

```
40 avatar min/mo × 40% uptake × USD $0.19/min  +  USD $0.75 GCP
  = USD $3.79/mo  × 1.55  =  AUD $5.87/mo  =  AUD $70.44/yr
```

**$70.44 is not one of three competing numbers. It is the variable cost per *active*
mother per year, and it is derived, sourced and correct.** The other figures in
circulation are almost certainly the same engine expressed per *enrolled* mother, or with
Year-1 GCP credits applied, or before platform support — different denominators, not
different answers. The blocker is a **units problem, not a knowledge problem**, and it can
be closed this week without waiting on Hector.

### One live defect in the reconciliation

The figure reconciles at **40% uptake**. But Assumptions 1.2 states the video uptake rate
as **35%**, and the note beside that cell still reads *"75% of active mothers actually use
the avatar feature"* — a note left behind when the value was changed. 40% is the
**engagement rate** from Assumptions 1.3 (active mothers as a share of enrolled), which is
a different variable entirely.

**The cost formula appears to reference the engagement cell where it should reference the
video uptake cell.** Three values (35 / 40 / 75) for one input, in the model everything
else derives from. Hector to confirm — but note the error is *conservative*: the true cost
at 35% is slightly lower, and nothing below changes materially.

---

## 2. Avatar video is 80% of variable cost

Per active mother per year:

| Component | AUD | Share |
|---|---|---|
| **Avatar video (HeyGen/LiveAvatar)** | **$56.54** | **80%** |
| GCP — Gemini, Vertex, Search, Cloud Run, storage, the entire rest of the platform | $13.95 | 20% |

The Companion's whole cloud and model stack costs less than a quarter of what the talking
head costs. **This is the finding.** Everything about the venture's unit economics is a
consequence of one product decision.

---

## 3. Every tier in the schedule is loss-making as modelled

A 1,000-birth service — 400 active mothers on the model's own 40% engagement — with
platform support at USD $500/month per tenant (**fixed per tenant**, Hector F10), and
before the USD $12,000 one-off setup:

| Scenario | Annual cost | Licence | Gross margin |
|---|---|---|---|
| As modelled | AUD $37,498 | $25,000 | **−50.0%** |
| At a sub-$20k entry tier | AUD $37,498 | $18,000 | **−108.3%** |
| Hector's larger-bundle rate ($0.128/min) | AUD $30,117 | $25,000 | **−20.5%** |
| Avatar capped at 20 min/mother/month | AUD $26,189 | $25,000 | **−4.8%** |
| **Avatar capped at 10 min/mother/month** | AUD $20,534 | $25,000 | **+17.9%** |
| **Voice and text only, no avatar video** | AUD $14,880 | $25,000 | **+40.5%** |

Two things follow immediately.

**Hector's bundle discount does not rescue it.** His open comment of 26 May — *"we can
upgrade to a larger bundle to have better per minute cost"* — is worth 33% off the avatar
rate and still leaves the tier 20% underwater. The rate is not the problem.

**Neither does raising the price.** Break-even at the modelled 40 minutes is AUD $37,498
for a service we are offering at $25,000. No Victorian regional maternity service is
paying $37,500, let alone the ~$62,000 a 40% margin would require.

### The top of the schedule is worse, and the model already said so

The cover flags it: *"⚠ KEY: At 40% engagement, the Enterprise tier shows a NEGATIVE gross
margin because the $95K licence doesn't scale with the 5,000 active-mother pool …
recommend Enterprise either caps inclusions at ~3,000 active with above-ceiling per-mother
fees, or raises list to ~$135K."*

Correct diagnosis. **The proposed remedy is inadequate by a factor of 2.7.** At 5,000
active mothers the cost is AUD $361,770. At the suggested $135,000 the tier is still
**168% underwater**. Capping inclusions at 3,000 active is the half of that recommendation
that actually works, and it is the half expressed as a maybe.

---

## 4. What this actually means

**The pricing problem is a cost-architecture problem wearing a pricing costume.** No tier
design, no procurement threshold, no per-mother rate schedule fixes a product that costs
$37,500 to deliver and sells for $25,000. Every hour spent on the tier table before this is
settled is an hour spent decorating the wrong number.

**And it is settleable, because the decision is still open.** The MVP Board of 28 Aug lists
**D-23, the LiveAvatar vendor decision**, as an out-of-loop item — not yet made. The
Companion runs voice and text today; the avatar is a vendor commitment not yet entered.

Three viable shapes, in order of preference:

1. **Voice and text as the standard product; avatar video as a metered premium.** 40.5%
   gross margin at the existing $25,000 tier — precisely the Foundation-tier target in
   Assumptions 1.4. Mothers who want the avatar buy minutes, or the service buys a block.
   The cost then scales with the revenue that causes it, which is the only structure that
   survives at every tier.
2. **Avatar included but hard-capped at ~10 minutes per mother per month**, with overage
   billed. 17.9% margin at $25,000 — thin, but positive and defensible, and it preserves
   the demo.
3. **Avatar at 40 minutes as modelled.** Requires roughly $62,000 from a 1,000-birth
   service to hit target margin. Not a Victorian regional product at any price.

**The evidence for option 1 is not only financial.** Hector's own note against the
40-minute assumption reads *"Conservative — could be 30 if voice-only is dominant."* He has
already flagged that voice may dominate. Nobody has measured it, because no pilot has run.

### The one number that decides it

**Avatar minutes per active mother per month is now the single most valuable measurement in
the pilot** — ahead of recall@5 and ahead of safety-tag triggering, because those two
determine whether the product works and this one determines whether the business does. It
must be instrumented from day one of the first pilot, per-mother, and reported weekly.

---

## 5. Hector's two open comments, both unanswered since May

| Date | Anchor | Comment | Status |
|---|---|---|---|
| 20 May | Assumptions!C16 | *"@brad current Essential or Business pricing includes 30 seconds per credit."* | **OPEN** — the correction that doubled cost/minute from $0.0909 to $0.19. Applied to the value; the note beside it was never updated |
| 26 May | Cost Engine!D13 | *"we can upgrade to a larger bundle to have better per minute cost."* | **OPEN** — worth ~33%, does not change the conclusion |

Hector was right on both, three months ago, and the second one has never been actioned.
Whatever vendor D-23 lands on, negotiate the bundle.

---

## 6. What changes in the pack

- **Retire the "unit cost unknown" blocker.** Replace with: *variable cost AUD $70.44 per
  active mother per year, of which 80% is avatar video; the open question is the product
  decision, not the number.*
- **No tier price is defensible until D-23 is decided.** Everything in
  `canonical-numbers.md` stays RECOMMENDED, and the gate is now named correctly.
- **The forecast's gross margins are wrong** wherever they assume the modelled avatar
  volume. The restatement workbook needs a COGS rebuild once D-23 lands.
- **Platform support is fixed per tenant** at AUD $9,300/year. At a 300-birth service that
  is 73% of the entire cost base. This is the arithmetic behind the regional-network
  conclusion: one tenant covering ten small services pays it once, not ten times.
- **Related-party note for diligence:** platform support and setup are ClinOps costs, and
  ClinOps is Hector's company. Normal, disclosable, and an investor will ask.
