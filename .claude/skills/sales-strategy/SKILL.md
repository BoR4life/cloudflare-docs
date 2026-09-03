---
name: sales-strategy
description: Run Brad's quarterly sales strategy review — win/loss analysis, revenue concentration, segment and pricing performance, capacity against the target, and the two or three changes worth making next quarter. Use when Brad says "sales strategy", "quarterly review", "where should I focus", "why am I not closing", "revenue plan", or asks about concentration risk, pricing or which segment to push. Not for weekly forecasting — that is sales-pipeline.
---

# Quarterly sales strategy review

## Purpose

The weekly review asks whether the deals will close. This one asks whether the shape
of the business is right: which segments are worth the effort, where the pricing is
wrong, how exposed the revenue is, and whether the capacity exists to hit the target
at all.

Run it quarterly, and always in April–May — before 30 June, while there is still time
to act on the Australian financial year, and while buyers still have money that
expires.

Read `sales-crm/SCHEMA.md`, `sales/playbook.md` and the full history in
`sales/opportunities.md` and `sales/activity-log.md`.

## Step 1 — Revenue reality, from Xero

Pull actual revenue by customer for the current and two prior financial years. Xero is
the source of truth here; the CRM is not. Build:

- Revenue by account by FY, with the trend for each
- Revenue by segment — health service, university, government department, publisher
- New versus repeat revenue
- Concentration: top account and top two as a share of total

Concentration is the standing risk in this business. Where the top two accounts are
more than half of revenue, that is the headline of the review, not a footnote — the
same way an unexplained gap is the headline of the financial checkpoint. Say what
happens to the year if the largest account does not repeat, in dollars.

Also flag revenue that has stopped: any account with revenue in a prior FY and none in
the current one. Each is a re-engagement candidate, and re-engagement is cheaper than
anything in the prospecting list.

## Step 2 — Win/loss

From closed deals in `sales/opportunities.md`:

| Cut | What it tells you |
|---|---|
| Win rate by segment | Which buyer type actually converts |
| Win rate by source | Whether referral and expansion beat outbound, and by how much |
| Average cycle length by segment | What to promise about timing, and what to plan cash around |
| Average deal size by segment | Where the effort pays |
| Loss reasons, grouped | The pattern worth fixing |
| Stage where deals die | Where the process is weakest |

The most useful cut is where deals die. In this sector the usual answer is between
`scoped` and `qualified` — enthusiasm that never found a budget. If that is the
pattern, the fix is qualifying harder and earlier, not selling harder.

If the sample is too small to support a conclusion, say so rather than reading a trend
into four deals. Note what is directional and what is noise.

## Step 3 — Pricing

- Realised price versus list, by segment
- Where discounts were given, and whether they won the deal
- Hardware versus education mix — hardware revenue at low margin flatters the top line
  and hurts the business
- Whether the productised arm is priced to scale or is being sold like an engagement

## Step 4 — Capacity

The constraint in this business is Brad's time, not demand. Compare the revenue target
against realistic capacity:

- Deals needed at current average size to hit the target
- Selling time available per deal at the current cycle length
- Delivery capacity if those deals all land — the failure mode where the pipeline
  works and delivery cannot absorb it
- Where the productised arm can carry revenue that the engagement arm cannot

If the target requires more deals than there is time to sell and deliver, say so
plainly and state what has to change: price, scope, segment mix, or the target itself.

## Step 5 — The changes

End with **two or three** changes for next quarter. Not a strategy document. Each one:

- The change, in a sentence
- The evidence from steps 1–4 that supports it
- What it is expected to be worth
- The first action, with a date

Anything that cannot be started next quarter is not a change, it is an aspiration.
Leave it out.

## Step 6 — Update the playbook

Fold what was learned back into `sales/playbook.md`: objections that got better
answers, ICP weights that the win/loss data contradicts, pricing that should move,
segments to add or drop. This is what makes the playbook compound rather than
calcify. Push to Drive.

## Output format

```
SALES STRATEGY — <quarter>

REVENUE
FY<current> to date  $<x>   vs FY<prior> same point  $<x>   <change>
By segment:   <segment> $<x> (<n>%) ...
Concentration: top account <n>%, top two <n>%
<one line on what happens to the year if the largest does not repeat>

STOPPED BUYING
<account> — last revenue FY<x> — $<lifetime> — <re-engagement view>

WIN/LOSS
Win rate: <n>% overall  ·  by segment: <...>
Deals die at: <stage> (<n> of <n> losses)
Loss pattern: <the grouped reason>
<what is directional vs what is too small a sample>

PRICING
<findings>

CAPACITY
Target $<x> needs <n> deals at $<avg>  ·  available selling time supports <n>
<verdict — and what has to change if it does not reconcile>

CHANGES FOR NEXT QUARTER
1. <change> — <evidence> — worth ~$<x> — first action: <action> by <date>
2. ...
```

## What not to do

- Do not read a trend into a handful of deals. Say when the sample is too small.
- Do not produce a strategy with more than three changes in it.
- Do not let concentration risk sit as a footnote when it is the main finding.
- Do not recommend growth that delivery cannot absorb.
