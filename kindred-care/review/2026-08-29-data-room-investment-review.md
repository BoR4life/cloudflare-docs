# Data room — investment review

**29 Aug 2026, updated 30 Aug 2026 · Confidential — ACU & Bundle of Rays**

> **Resolved 30 Aug 2026 by Brad.** BVUIP is **$300k POC then $1.0M commercialisation —
> $1.3M in total — with each round split 50/50 between ACU and Innovation Victoria.** So
> finding 1 is a labelling-and-amount error in the model, not a scope error: the labels were
> right, the amounts were not. Finding 2 changes shape entirely — the match is 1:1 by
> construction, and the real issue is that **ACU's cash obligation is $650,000** ($150k at
> POC, $500k at commercialisation) against no identified cash pool. The Business Plan's
> "$1,000,000 ceiling" sentence is the thing that is wrong and must be corrected.
> Corrections are worked through in `finance/Kindred_Care_Forecast_Restatement_v1_20260830.xlsx`.

Reviewed from an investor's side of the table, against three tests: **is it accurate**,
**does it marry with the narrative**, and **is it modest**.

**Scope read in full:** Business Plan v2 (Jul 2026), Kindred Care 5yr Forecast FY2027–FY2031,
**Overview — BoR, ACU and Kindred Care v13 (23 Jun 2026, ACU Confidential)**, the Programme
Task Register v2, GTM v2.1, the MVP Board (28 Aug), and the ACU–BoR email trail. The uploaded
register is byte-identical to the Drive copy — 87 tasks, 31 critical path, 77 not started,
6 in progress, 4 complete, unchanged.
**Not yet opened:** Pricing Model v1, Unit Economics LTV/CAC, Business Model Canvas, IP Plan
draft, Product Overview v1, Quality & Safety Strategy, Insurer Channel memo. Those are a
second pass and some findings below will need checking against them.

**Overall.** The Business Plan is genuinely good — disciplined, well-argued, and it holds a
defensible TRL line on purpose. The forecast is properly built: bottom-up, role-by-role,
three-statement, with a documented basis of preparation and its own open-items list. The
problems are not sloppiness. They are **inconsistencies between documents, and a small
number of numbers that do not say what their labels say** — and both are exactly what
diligence is designed to find.

Findings are ordered by what would do the most damage if an assessor found it first.

---

## 1. The BVUIP figures in the forecast do not match their own labels

In the Revenue tab, Grant Funding section:

| Line as labelled | Amount in the model |
|---|---|
| BVUIP — POC round **($300k)** | **$500,000** (FY27) |
| BVUIP — Commercialisation round **($1.0M)** | **$600,000** (FY28) + **$200,000** (FY29) = **$800,000** |

The POC line carries $200,000 more than its label. The commercialisation line carries
$200,000 less. Total BVUIP in the model is **$1,300,000**.

The Business Plan states: *"The total combined investment ceiling under BVUIP is $1,000,000
AUD (to be confirmed)."*

**So the model assumes $300,000 of BVUIP money that the Business Plan says may not exist**,
and the POC line alone is $200,000 above the amount the Business Plan asks for. This is the
first thing a funder checks, because it is their own money. Fix before anything else.

## 2. The model proves the 1:1 match is not being met

The forecast's own Funding tab computes it:

| | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|
| **Cumulative match ratio (ACU : BVUIP)** | **0.12x** | 0.13x | 0.29x | 0.48x | 0.68x |

BVUIP requires **1:1 matched cash**. In FY27 the model matches $500,000 of BVUIP against
$60,000 of ACU **in-kind notional** value — 12%, and in-kind rather than cash. The ratio
never reaches 1.0x across five years.

This is the cash-match blocker, quantified, sitting inside the document that goes to the
funder. GTM v2.1's open dependencies already say ACU has flagged no cash pool exists for the
$250k–$500k match. **Nobody has connected the two.** An assessor will read that row in under
a minute and it will frame the entire assessment.

Either the match is solved, or the model is rebuilt on the match that actually exists and
the gap is disclosed on the face of it. It cannot be left to be discovered.

## 3. BVUIP is treated as income, but the Business Plan describes it as investment

The forecast's basis of preparation states grants are *"recognised as income against
milestones AND received in cash — flows through P&L and cash flow"*, and BVUIP sits inside
**Grant Funding (non-trading income)**.

The Business Plan describes BVUIP Round 1 as *"Pre-incorporation co-investment; SAFE with
side letter; binding agreement for post-incorporation shares"* — that is equity, not a grant.

Running equity through the P&L overstates income by **$530,000 in FY27** and **$665,000 in
FY28**, and it flatters EBITDA correspondingly:

| | FY27 | FY28 |
|---|---|---|
| EBITDA as presented | ($258,990) | ($292,649) |
| EBITDA with BVUIP removed from income | **≈($758,990)** | **≈($892,649)** |

The business is roughly three times more loss-making in FY27 than the P&L shows. An
accountant reviewing this for ACU will raise it, and it is better raised by you.

## 4. Two documents quote different prices for the same product

| Tier | Business Plan | Forecast (FY27) | Gap |
|---|---|---|---|
| <500 births | $25,000 | **$16,200** | −35% |
| 500–2,000 | $45,000 | **$32,250** | −28% |
| 2,000–4,000 | $65,000 | **$59,679** (>2,000, incl. universities) | −8% |
| 4,000+ Enterprise | $95,000 + overage | **absent from the model** | — |

The Business Plan has four tiers; the model has three and no Enterprise tier at all. The
Business Plan notes pilot sites get preferential pricing for three years, which may explain
the lower fees — but the model indexes those fees at 3% p.a. for five years and **never
steps up to list**, so list pricing is never realised anywhere in the forecast.

Two prices for one product, in one data room, with no reconciliation note between them.

## 5. The model is two-thirds offshore, and both narrative documents say it is not

FY29 trading revenue by geography:

| | FY29 | Share |
|---|---|---|
| Australia B2B | $604,624 | 20% |
| **India B2B** | **$1,446,139** | **48%** |
| International (UK/USA) | $556,973 | 18% |
| B2C + XR | $423,939 | 14% |

**66% of FY29 trading revenue is outside Australia.** India alone is 2.4× Australian revenue.

Against that:

- The Business Plan: *"International expansion (India, UK, Gulf) is **post-pilot upside, not
  the primary investment thesis**."*
- GTM v2.1 §4.5: *"International revenue — a deliberately conservative position."*
- GTM v2.1 open dependency: *"**no India revenue is attributed to Kindred Care until an
  executed Kindred Care contract exists**."* The model attributes $13,125 in FY27 and
  $563,925 in FY28.

This is the sharpest narrative break in the data room, and it lands on the worst possible
reader. **Breakthrough Victoria is Victorian money that requires Victorian economic
benefit.** A model where two-thirds of revenue is offshore, presented alongside a business
plan that calls international "upside, not the thesis", invites the question of which
document to believe.

The model's own Cover tab already flags it as an open item for Brad: *"Confirm whether
International (UK/USA) stays in base case or moves to a labelled upside scenario."* It
should move — along with India — into a clearly labelled upside case, leaving a base case
that is Victorian and Australian.

The India ramp also needs its own defence: **2 customers in FY27 to 45 in FY28** — 43 net
adds in a year, with an India BD lead at 0.5 FTE and a channel described as replicating the
founder's origin-company relationships. That is the least evidenced number in the model and
the largest.

## 6. Zero churn across five years

The revenue build accumulates customers and never loses one — AU 6 → 13 → 24 → 40 → 54,
India 2 → 45 → 70 → 86 → 105, international 1 → 6 → 15 → 28 → 42. There is no churn
assumption anywhere.

This is the most visible optimism in the model. Health service contracts carry
termination-for-convenience; the international evidence on this product class shows a **43%
pooled user dropout**; and a five-year forecast with 100% logo retention is not a forecast
an experienced investor accepts. Add a churn line — even 5–10% — and the model gains more
credibility than the revenue it costs.

## 7. Negative cash and negative net assets in year one

| | FY27 | FY28 |
|---|---|---|
| Closing cash | **($35,241)** | **($20,557)** |
| Net assets | **($64,990)** | $25,861 |

The model shows the company with negative cash at both year ends and **negative net assets
at 30 June 2027**. The equity line is described as *"sized to maintain cash buffer"* and
plainly is not.

Presenting a forecast in which the company is balance-sheet insolvent in year one, to an
investment committee at which ACU would become a shareholder, raises a directors'-duties
question before it raises a commercial one. Re-size the FY27 equity injection so closing
cash holds a real buffer — three months of operating cost is the usual test.

## 8. TRL is now stated four different ways

| Source | Position |
|---|---|
| **Business Plan v2** | **TRL 3**, deliberately: *"We hold the line at TRL 3 so that every readiness claim downstream is one we can evidence."* |
| Programme Register | TRL 3→4 *via the funded POC*; *"TRL 4 never claimed up front"* |
| **Forecast Cover tab** | *"**TRL 4 at FY27 start.** BVUIP POC ($300k) funds the TRL3->4 Victorian pilot"* — self-contradictory in one sentence |
| **GTM v2.1** | *"current state — a validated prototype at **Technology Readiness Level 4**"* |

**The Business Plan is right and I was wrong on 29 August.** I assessed TRL 4 from the MVP
Board's shipped volume. That was the wrong test. This venture's own instrumented definition
of TRL 4 is *recall@5 ≥ 0.85 and safety-tag triggering ≥ 0.95, measured against a
gold-standard evaluation set* — and that eval set does not exist yet (register P4-04 and
P3-06, due 2 Oct, not started). A level is evidenced, not claimed. **The correct, modest,
and strategically necessary position is TRL 3, climbing.**

It is also commercially self-defeating to claim otherwise: **if you are already at TRL 4,
the POC has no R&D left to fund.** The GTM v2.1 claim and the forecast Cover line both
undercut the investment case they are meant to support. Both must change to match the
Business Plan.

## 9. Ownership is stated three ways, and none of them is agreed

| Source | Position |
|---|---|
| PhD canonical facts | 70/30 BoR / ACU |
| Business Plan §6 | **[TO BE AGREED]** — contribution-based, *"does not of itself determine majority equity"* |
| Forecast Cover | Kindred Care Pty Ltd *"to be incorporated; **held by Bundle of Rays Pty Ltd**"* — a wholly-owned subsidiary |

A 70/30 JV, an undetermined contribution-based split, and a BoR subsidiary are three
different companies. The 70/30 figure has been carried through internal documents as though
settled; the Business Plan says explicitly that it is not.

Related: the model shows **$1,750,000 of cumulative share capital** by FY30 with no price
per share, no ownership percentages and no dilution. UCAC's checklist requires *"dilution /
cap table"* by name.

## 10. Smaller accuracy items

- **TAM.** Business Plan: *"~300 services and ~310,000 births"* nationally. Forecast Cover:
  *"~250 AU maternity services + ~35 universities = TAM ~285."* Pick one.
- **Revenue table in the Business Plan is empty** — FY27/FY28/FY29 all read `[from model]`.
  A business plan going to an investment committee with placeholder revenue.
- **"Bill [co-signatory]"** — placeholder in the key personnel table. It is Bill Russell.
- **Leadership succession is described three ways**: Business Plan says a recruited lead
  becomes CEO/MD *at incorporation* with Brad moving to the Board; the Register says handoff
  *6–12 months post-funding*; Brad describes Marie as *co-CEO*. Key-person succession is a
  standard diligence question and three answers is worse than any one of them.
- **Component naming.** The Business Plan names *CLARA AI engine* and the *AIDA agent
  framework*; the MVP Board and product name *Elena* and *Agent B*. Same system, different
  vocabulary across documents.
- **Data residency.** Business Plan says GCP *australia-southeast1* (Sydney); the MVP Board
  says *inference in Sydney, data in Melbourne* (southeast2). If data really is held in
  Melbourne, the Business Plan is **under-selling a Victorian-sovereignty fact that BVUIP
  will value**. Confirm and state it.
- **R&D tax incentive is $0 in FY27 and FY28.** The 50% haircut plus the grant-funded
  exclusion zeroes it in the two years of greatest need. If BVUIP is equity rather than a
  grant (finding 3), the exclusion may not apply and this is real cash being left out.
- **Gross margin 79%→87%** excludes the Midwife Educator (human-in-the-loop, in employment
  costs) and assumes ACU clinical content review stays free forever. Both are delivery
  costs. Worth one sensitivity showing margin if ACU in-kind is priced.
- **FY27 shows $78,365 of Australian B2B licence revenue from 6 customers**, while the
  Business Plan and GTM describe FY27 as the pilot year with conversion to paid licences in
  FY28. Pilots that pay a licence in the same year they are pilots need explaining.

## 11. What is missing entirely

**Required by UCAC and absent:** exit strategy · founder's pitch pack · cap table and
dilution · pre-money valuation · Heads of Agreement · IP register v1 · ACU 2033 alignment
and Risk Appetite statement.

**Expected by any investor and absent:**

- **A downside case.** There is one scenario in the data room and it goes up. No bear case,
  no sensitivity on price, churn, India, or the timing of the cash match.
- **Existing BoR investor terms.** The Business Plan's risk table names *"multi-layer VC
  interests"* and says existing BoR investor terms are *"documented in the data room"*. They
  were not in the folders enumerated. If BoR has existing investors, their terms shape
  everything about a KC-Co cap table — this is a first-hour diligence item.
- **Signed customer evidence.** Nothing above Step 1 on the venture's own engagement ladder.
  The Business Plan targets 3–4 Victorian LOIs by Oct–Nov 2026; none exist yet.
- **The appendices the Business Plan says exist.** It lists Statement of Work v2, IP Audit
  Draft 0.2, TRL Position Note, Early Adopter Engagement Strategy v1, LOI Template and a
  Data Room Index as *"available in the data room"*. I did not find them in the data-room
  folders. Either they are elsewhere, or the Business Plan is promising documents that are
  not there — which is itself a diligence finding.
- **The $1.22M forecast reconciliation** flagged in Pricing Model v1 and awaiting CFO
  sign-off. Not yet examined; must be closed in the same pass.

---

## 12. From the Overview deck — four findings, one of them the origin of finding 1

Russell's Overview deck (v13, 23 Jun) is the structural document the rest of the pack hangs
off. Reading it against the Business Plan and the model:

**a. The $1M ambiguity started here, and it was flagged as a question.** Slide 4 sets the
POC at *"≤ $300,000"* and the start-up round at *"≤ $1,000,000 \*\*"* — with the footnote
*"\*\* ?? – combined total investment $1M?"*. **ACU asked this question on 23 June and it
has never been answered.** In the ten weeks since, it has silently hardened into a $1.3M
assumption inside the forecast (finding 1). This is the cleanest possible example of an open
question becoming a number: put it back to Russell as a question, not as a model input.

**b. The entity ladder has four rungs, and the model shows a different structure.** The deck
runs **KC-S (scoping) → KC-U (Kindred Care Unincorporated) → KC-Co (start-up)**, with KC-U
as the unincorporated JV between ACU and BoR under a Head Unincorporated JV agreement. The
forecast Cover says KC-Co is *"held by Bundle of Rays Pty Ltd"* — a wholly-owned subsidiary,
which is not the same animal. Add this to finding 9: ownership now has three stated
positions and the deck implies a fourth path.

**c. There is a third revenue stream in ACU's framing that appears nowhere in the
investment documents.** The deck names **KC-SC — Kindred Care & ACU Short Courses** and
describes *"3 streams · KC / PhD / SC"*. Neither the Business Plan nor the forecast models
short courses at all. Either it is a live stream that is missing from the numbers, or it has
been dropped and ACU's own deck is stale. It should not be ambiguous in a document Russell
is presenting from.

**d. The BV gate is a two-step that sits after the ACU chain, and the model may be a year
early on cash.** The deck describes a **BVIC 'for notice' presentation**, a positive-outcome
milestone, then a **BVIC 'investment' presentation**, then a BVIC recommendation to
co-invest. Meeting 12 puts 'for notice' *"around October"*. So the real sequence is:

`UCAC 16 Oct → VC 23 Oct → IC 30 Oct → BVIC for-notice → BVIC investment → recommendation → contracting (SAFE + side letter + Head JV)`

The register calls the 30 Oct IC submission the *"PROGRAMME END-POINT"*. It is the end of the
ACU chain, not the end of the road to money. **The forecast books $500,000 of BVUIP POC cash
inside FY27 (by 30 Jun 2027).** That is possible but tight, and FY27 closing cash is already
negative (finding 7). One slip in the BVIC sequence pushes the cash into FY28 and the FY27
hole deepens. The model needs a timing sensitivity on first BVUIP cash.

**Also from the deck, two smaller checks:**

- **The VR avatar is scoped *out* of the POC** — *"Product — MVP (procure-level companion)
  (not prelim. VR avatar)"*. But the Business Plan lists avatar generation among POC
  deliverables, and the forecast carries HeyGen video-avatar COGS from FY27 ($12,705) plus
  capitalised *"Cached Avatar + XR"* software. Costs are in, scope is out.
- **Idaho or Iowa.** The deck names *"Idaho (USA)"* among international advisory adopters;
  GTM v2.1's CRC-P consortium names the *"Iowa Department of Public Health"*. Different
  states. One of them is wrong.

**One thing the deck does well and the rest of the pack should copy.** It splits the PhD
explicitly into **KC-PhD (Kindred Care-aligned outcomes)** and **non-KC-PhD**. ACU has
already drawn the research/commercial firewall in its own structural document. Brad's
documents should mirror that language exactly — it is the strongest available answer to the
independence question, and it comes from ACU rather than from the founder.

---

## What I would do, in order

1. **Fix the BVUIP numbers** so labels and amounts agree, and reconcile the total against
   the stated $1.0M ceiling. One hour. Nothing else should go out before this.
2. **Decide the accounting treatment of BVUIP** — investment or grant — and restate the P&L.
   This changes EBITDA materially and needs the CFO.
3. **Move India and UK/USA into a labelled upside scenario** and rebuild a base case that is
   Victorian and Australian. This is the single biggest improvement to how the pack reads at
   Breakthrough Victoria.
4. **Resolve TRL to 3, everywhere.** Correct GTM v2.1 and the forecast Cover tab to match the
   Business Plan. It is the honest position and it is the one that makes the POC fundable.
5. **Add churn**, re-size the FY27 equity injection so cash and net assets stay positive, and
   add one downside case.
6. **Reconcile the two pricing tables**, or state in both which is list and which is pilot.
7. **Settle ownership language** — one position, stated identically in every document, even
   if that position is "to be agreed through contribution-based valuation".
8. **Confirm the appendices exist**, and locate the existing BoR investor terms.
9. **Put the $1M ceiling back to Russell as the question it was on 23 June** — combined
   total, or $300k plus $1M? Everything in the model's funding stack depends on the answer.
10. **Add a timing sensitivity on first BVUIP cash**, given the BVIC two-step sits after the
    30 Oct IC submission.
11. **Resolve KC-SC** — model the short-courses stream or remove it from the ACU deck.

## The honest summary

Nothing here is fatal and nothing here is dishonest. The Business Plan in particular is
better than most at this stage — the TRL discipline is genuinely impressive and should be
protected, not diluted.

But the data room currently tells **two different stories about how big this is and where
the money comes from**, and the more optimistic one is in the spreadsheet. Investors read
the spreadsheet last and trust it most. Bringing the model back to the Business Plan's own
modesty — Victorian base case, TRL 3, BVUIP at the amount actually sought — costs nothing
except forecast revenue that was never going to be believed anyway, and it buys the one
thing this venture cannot manufacture later: the assessor's trust that when you say a
number, it is the number.
