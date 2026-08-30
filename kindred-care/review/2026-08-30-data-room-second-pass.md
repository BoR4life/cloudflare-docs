# Data room — investment review, second pass

**30 Aug 2026 · Confidential — ACU & Bundle of Rays**

Second pass over the documents not opened on 29 Aug. **Read in full:** Pricing Model v1
(with Hector's open comments), Unit Economics / LTV / CAC, IP Plan Draft 0.2.
**Still unread:** Business Model Canvas v1.0, Product Overview v1, Quality & Safety Draft
Strategy, Insurer Channel memo. The first three are unlikely to change the picture; the
insurer memo is explicitly a Phase-3 reference document.

Three corrections to my own first pass are recorded at the end.

---

## 1. The number that decides whether this is a business

**Unit cost per active mother is stated three different ways, spanning 4.8×.**

| Source | Variable cost per active user | Per year |
|---|---|---|
| **FY27–31 Forecast** | $7.00 compute + $22.00 video at 35% uptake | **≈$14.70** |
| **Unit Economics (B2C, at scale)** | — | **$44.60** |
| **Pricing Model, Cost Engine** | **$5.87 per month** | **$70.44** |

The forecast's 79%–87% gross margins depend entirely on the $14.70 figure. At the Pricing
Model's own $70.44, FY29 COGS on 48,850 active users would be roughly **$3.4M against
$3.03M of trading revenue** — gross margin negative at scale.

This is not a rounding difference. It is the difference between a business and not one,
and **both documents flag it as unresolved**:

- Forecast Cover, open items: *"Hector: Confirm cloud/dev-tooling cost basis (HeyGen
  step/plans vs per-minute) — 'Cloud platform & dev tooling' line is provisional."*
- Pricing Model, Hector's comments (20 and 26 May, still open): *"current Essential or
  Business pricing includes 30 seconds per credit"* and *"we can upgrade to a larger bundle
  to have better per minute cost."*

**Nothing else in this review matters as much.** Every margin, every LTV:CAC ratio and the
entire capital-efficiency thesis rests on which of these three numbers is true. It has been
open since May. It needs Hector, a HeyGen plan decision, and one afternoon.

## 2. The IP Plan gives BoR's platform to ACU

IP Plan Draft 0.2 lists, under **ACU background IP**:

> *"Multi-tenant AI Agent framework — Operational on GCP — ADK, Gemini, Vertex Search,
> Cloud Run; tenant isolation; admin UI; Looker analytics"*

That is Hector's build. The MVP Board evidences it as `bor-iridia` — four platform
services, multi-tenant isolation, admin console, Cloud Run. And the Business Plan, three
months later, lists it correctly under **BoR**: *"AI platform architecture (GCP)… analytics
dashboards, multi-tenant infrastructure, SSO, billing, all codebase and documentation.
Remains BoR property."*

**The IP Plan attributes Bundle of Rays' core platform to ACU, in a document prepared for
ACU Commercialisation.** The Business Plan is later and correct, so this is very likely a
drafting error rather than a position — but Draft 0.2 is still in the data room, and IP
register v1 (register task P2-05, due 18 Sep) draws on it. If this propagates into the IP
register or the Heads of Agreement it becomes extremely expensive to unwind.

The register's own rule is *"do not assert unverified ACU IP — diligence liability."*
Asserting BoR's platform **as** ACU IP is the more damaging version of the same error.

**Fix before the 11 Sep IP verification workshop (MTG-03).**

## 3. A fourth price list, and the tier bands don't line up either

| Tier | Business Plan | Unit Economics | Forecast FY27 |
|---|---|---|---|
| Foundation | **$25,000** (<500) | **$28,000** (<500) | **$16,200** (<500) |
| Standard | **$45,000** (500–2,000) | **$48,000** (501–1,500) | **$32,250** (500–2,000) |
| Advanced / Network | **$65,000** (2,000–4,000) | **$72,000** (1,501–3,500) | **$59,679** (>2,000, incl. universities) |
| Enterprise | $95,000 (4,000+) | $95,000 (3,500+) | **absent** |

Four documents, four price schedules, **and three different sets of band boundaries**.
The tier is called *Advanced* in the Business Plan and *Network* in Unit Economics — and
GTM v2.1 uses *Network* when describing SCHHS, so the GTM aligns with Unit Economics while
the Business Plan stands alone.

An assessor comparing any two of these will ask which is the price. There is currently no
answer in the data room.

## 4. The capital-efficiency claim is contradicted by the forecast

Unit Economics opens with the venture's headline commercial claim:

> *"The model targets a cumulative peak cash burn of approximately **$0.15M**, drastically
> lower than the $5–10M typically required by comparable health-tech ventures."*

The FY27–31 forecast's own cumulative free cash flow:

| | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|
| Cumulative FCF | ($235,241) | ($620,557) | **($770,046)** | ($660,142) |

**Peak cumulative burn is $770,046 — 5.1× the claimed $0.15M.** On the restated Australian
base case it is materially worse again.

This is the most quotable sentence in the data room and it does not survive contact with
the model behind it. Either restate the claim to the real figure — which is still a
genuinely efficient number for a health-tech venture and worth saying proudly — or remove
it. Do not leave it for an assessor to compute.

## 5. The sales model is described two ways

Unit Economics justifies a CAC of **0.8× ACV** on the basis that the ACU channel
*"bypasses the need for an expensive, traditional enterprise sales force in the first two
years of commercialization."*

The forecast hires, in FY28 — year two:

| Role | FY28 cost |
|---|---|
| Head of Sales (0.5 FTE) | $84,150 |
| BD Lead — National (1.0) | $142,800 |
| BD Lead — International (0.5) | $51,000 |
| Customer Success — International (0.5) | $48,450 |
| Marketing & Content (1.0) | $147,900 |
| **Total commercial** | **$474,300** |

Against 7 net Australian customer adds in FY28. Even attributing only half that cost to the
Australian motion, CAC lands near or above 1.0× ACV before marketing spend — not 0.8×.

The channel advantage is real and worth claiming. The claim that it removes the need for a
sales force is contradicted by the venture's own hiring plan two tabs away.

## 6. What Unit Economics gets right, and should be copied

**The Enterprise tier is disclosed as broken, in writing.** *"Structural vulnerability…
compresses the gross margin to 6.1%, resulting in an unviable LTV:CAC ratio of 0.8x…
a required gating item before full-scale commercial procurement deployment."*

That is the most honest paragraph in the data room and it is exactly the register that the
rest of the pack should be written in. Disclosing your own weakest tier before an investor
finds it is worth more than the tier.

One caveat: **the Business Plan states the fix as already designed** (*"The Enterprise tier
uses a two-part tariff ($95,000 base to a 1,200-active cap, plus per-active overage)"*)
while Unit Economics says it *"is being actively restructured"* and remains a gating item.
Done in one document, pending in the other.

Two further notes on that tier: B2C economics are stated to be *"only positive when
supported by the amortized platform unit costs achieved at Enterprise-level scale"* — so
the B2C case depends on the tier that does not yet work. And the per-active overage is the
mechanism that turns engagement, which is Kindred Care's job, into the customer's financial
risk. A capped two-part tariff is the safer structure.

## 7. The IP Plan is strong, and three things in it are being under-used

The thesis — *"layered protection, not a patent moonshot"*, software patents unlikely to
survive post-*Aristocrat*, the institutional moat as the strongest layer — is well judged
and honestly argued. *"Frontier-model performance will be matched within 18 months. RAG
architectures are commodity."* Very few ventures write that down.

Three assets in it appear nowhere else:

- **Nine patentable concepts** from a 2022 ipCapital Group invention inventory across the
  broader BoR portfolio. Not in the Business Plan, the forecast or the GTM.
- **A ten-avatar multicultural library** — First Nations, grandmother, peer-aged and CALD
  figures with a warmth and psychological-safety methodology. This is a genuine
  differentiator against Eve and it is not in the competitive section.
- **A physical welcome pack** — box, journal and magnet, listed under registered designs.
  **This is the tangible enrolment artefact the retention evidence calls for.** The SMART
  start cohort that retained a median 167 days had a physical package; self-enrolment
  retained zero. The pack already exists as a design intention — it should move into the
  pilot protocol and the cost model.

**One modesty flag.** The content-governance moat is rated *"STRONG — TODAY"* on the basis
of *"four years of continuous ACU clinical governance over a maternal corpus."* The corpus
is a 40-document set that the POC exists to build. It is a strong moat **by FY29**; today
it is a plan. Re-rate it honestly — the argument is more persuasive as "this compounds and
cannot be caught up" than as a claim about today.

**And the trademark position needs a current answer.** As at April 2026 the Kindred Care
word and device marks were *"filing as priority"* — i.e. not filed. Given a generic-leaning
name in a market where Cabrini already holds "Eve", confirm whether the marks are now filed
and whether a clearance search has been done. This is cheap now and expensive later.

## 8. The IP Plan gives the cleanest ownership structure — and it is a fifth version

> *"BUNDLE OF RAYS Pty Ltd — Founding shareholder. ACU — Founding shareholder.
> KINDRED CARE PTY LTD — Operating company · Owns all foreground IP · Holds licences from
> both parents. BREAKTHROUGH VICTORIA — post-investment shareholder under BVUIP,
> investment only, no IP contribution."*

That is coherent, matches the Overview deck's KC-U → KC-Co intent, and is almost certainly
the right structure. It is also the **fifth** stated ownership position:

| Source | Position |
|---|---|
| PhD canonical facts | 70/30 BoR / ACU |
| Business Plan §6 | [TO BE AGREED] |
| Forecast Cover | *"held by Bundle of Rays Pty Ltd"* — subsidiary |
| **IP Plan** | **BoR + ACU founding shareholders; BV post-investment** |
| Overview deck | KC-S → KC-U → KC-Co, with private investors in scope |

Adopt the IP Plan's version everywhere, or say explicitly that it is to be agreed. The
forecast's "subsidiary" line is the outlier and should go.

**One term BV will scrutinise:** *"Improvements to licensed IP flow back to the licensor
and re-license to the JV."* Improvements to BoR's platform funded with BVUIP money would
accrue to BoR rather than to the company BV has invested in. It is a common JV term and
defensible, but prepare the answer.

## 9. Two more revenue streams that exist in pricing and not in the forecast

The Pricing Model carries two priced streams the FY27–31 forecast does not model at all:

- **Sheet 8 — Nurse Workforce Readiness (NWR)**, per-FTE pricing for workforce and
  education functions, annotated *"FY27 onwards in the forecast."* It is not in the
  forecast.
- **Sheet 5 — B2B Education Licence**, a two-part tariff with a program licence plus
  per-student fee, *"ACU and UoW = founding-partner tier."* The forecast merges universities
  into health-service Tier 3 rather than pricing them separately.

With KC-SC (short courses) from the Overview deck, that is **three priced or named streams
outside the financial model**. Either they are real and the model understates the business,
or they are not and the pricing model overstates the offer. Both are fixable; neither
should be ambiguous at UCAC.

## 10. The $1.22M reconciliation gap — what it actually is

Pricing Model sheet 9 reconciles tier sales against:

> *"Forecast revenue (Detailed Breakdown view, per **Three-Way Forecast V9, 16/10/25**)"*

That is the Bundle of Rays three-way forecast dated **16 October 2025**, covering FY26–FY29.
It has since been superseded twice — by the "Forecast FY26–FY30 v2" the GTM cites, and by
the current Kindred Care FY2027–FY2031 model.

**So the $1.22M gap sits between two views of a forecast that is ten months old and no
longer the operative document.** The instruction to get CFO sign-off on that reconciliation
before BVUIP submission is therefore the wrong fix.

**The right fix is to re-baseline the Pricing Model against the current FY27–31 forecast and
retire the V9 reconciliation entirely.** That also removes a fourth forecast-period label
(FY26–FY29) from a data room that already carries FY26–FY30 and FY27–FY31.

---

## Three corrections to my first pass

1. **"No downside case anywhere" was wrong.** Pricing Model **sheet 10 carries a
   Bear / Base / Bull scenario framework** for the Australian Health stream. The scaffolding
   exists — it simply is not carried into the forecast, the Business Plan or the GTM.
   Wiring it through is a much smaller job than building one.
2. **Use 10% churn, not the 8% I proposed.** Unit Economics already assumes *"an
   institutional churn rate of 10% (a 10-year customer lifetime)"*. The venture has a
   documented assumption; the forecast should use it. Consistency beats my number.
3. **The $1.22M gap is not a live reconciliation item** — see finding 10. Re-baseline
   rather than reconcile.

## Revised order of work

Ahead of everything in the first pass:

1. **Settle the unit cost** with Hector and a HeyGen plan decision. Every margin claim in
   the data room depends on it, and it has been open since May.
2. **Correct the IP Plan's ACU/BoR platform attribution**, before the 11 Sep IP
   verification workshop.
3. **Restate or remove the $0.15M peak-burn claim.**
4. **Pick one price list**, with one set of band boundaries and one set of tier names.
5. **Re-baseline the Pricing Model** to the FY27–31 forecast; retire the V9 reconciliation.
6. Then the first-pass list: BVUIP amounts, match presentation, base-versus-upside,
   TRL to 3, churn at 10%, FY27 equity re-size.

## The honest summary, second pass

The individual documents are better than their sum. The Business Plan's TRL discipline, the
Unit Economics disclosure of the broken Enterprise tier, and the IP Plan's refusal to
promise a patent moonshot are all the work of people telling the truth about a hard thing.

What is missing is a **single set of numbers**. Four price lists, three unit costs, five
ownership structures, four forecast periods and a headline burn figure five times the model
behind it. None of it is dishonest. All of it is what happens when good documents are
written months apart and never reconciled against each other.

The fix is not more work — it is one pass that makes every document say the same thing, and
a rule that nothing enters the pack until it agrees with the others. That rule is now in the
agent, and the consistency sweep is item 8 on its backlog.
