---
name: sales-pipeline
description: Run Brad's weekly pipeline review — reconcile the CRM against Gmail, Fireflies, Calendar and Xero, enforce stage discipline, produce an honest weighted forecast against the revenue target, and name the one deal to move this week. Use when Brad says "pipeline", "pipeline review", "what's my forecast", "how's the pipeline looking", "weekly sales review", or asks what deals are stalled. Also use to add, update or re-stage a deal. Not for drafting follow-up emails — that is sales-followups.
---

# Weekly pipeline review

## Purpose

An honest read of what is actually going to close, on data that has been reconciled
against reality rather than recalled. Five customers produced last financial year's
revenue; at that concentration a single deal moving a quarter is the difference
between a good year and a bad one. The forecast has to be trustworthy, which means
it has to be conservative.

The discipline that makes this work is the qualified gate in `sales-crm/STAGES.md`:
funding named, economic buyer identified, timeline known. Deals that have not passed
it do not get counted as though they have.

Read `sales-crm/SCHEMA.md` and `sales-crm/STAGES.md` before the first run in a
session.

## Step 1 — Pull and reconcile

Restore `sales/` from Drive per the sync protocol. Then reconcile — this is the part
that keeps the forecast honest, and skipping it invalidates the review.

For every live opportunity, check the CRM against the sources:

| Check | Source | What it catches |
|---|---|---|
| Is `last-touch` right? | Gmail — last inbound message on the thread | Deals that look active but are not |
| Any meeting since the last review? | Fireflies, Calendar | Stage changes nobody recorded |
| Any commitment made and not delivered? | Fireflies action items vs `activity-log.md` | Deals stalled on Brad's side |
| Did it invoice? | Xero | `won` deals still sitting in `procurement` |
| Does the stage still hold? | Exit criteria in `STAGES.md` | Optimistic staging |

Every correction gets applied to the CRM and logged. **Report the corrections** — a
review that silently fixes six wrong stages hides the fact that the pipeline was
wrong, which is itself the finding.

## Step 2 — Enforce stage discipline

Walk every live deal against the exit criteria. Three specific tests:

**The qualified gate.** Any deal at `qualified` or beyond with `funding: unknown`, no
named `economic-buyer`, or no `funding-window` gets demoted to `scoped`, and finding
the missing element becomes its next action. This will feel harsh and it is the
single most valuable thing this review does. A deal that cannot name where the money
comes from is a conversation.

**The dated action test.** Any live deal with no `next-action-due`, or one more than
30 days out, is stalled. Say so plainly.

**The dormancy test.** Any deal with no two-way contact in 90 days and no scheduled
next step moves to `dormant`. It stays in the file — dormant accounts are the
cheapest re-engagement source there is — but it leaves the forecast.

## Step 3 — Recompute confidence

For every deal, recompute from the stage baseline plus the adjustments table in
`STAGES.md`. Where the computed figure differs from what is recorded, use the
computed one and note the change. Confidence that only ever moves up is not a
forecast.

## Step 4 — Forecast

```
weighted = Σ (value × confidence / 100)
```

Report three horizons: this quarter, this financial year (AU FY, ends 30 June), and
the next 12 months. For each, show committed (`procurement` and beyond), probable
(`qualified` and `proposal`), and possible (everything earlier) separately. Do not
present a single blended number — the mix matters more than the total, and a pipeline
that is all "possible" is an empty pipeline with good manners.

Compare against the target in `sales/playbook.md`. Where there is a gap, state the
gap in dollars and in deals-at-average-size, and say what would have to be true to
close it. Be direct about it: the useful version of this review is the one that says
"this does not get there" early enough to act on.

Flag concentration explicitly. If one account is more than 30% of the weighted
pipeline, or the top two are more than 50%, name it as a risk with the revenue
history behind it.

## Step 5 — The one deal

End with a single recommendation: the one deal to move this week, and the specific
action that moves it. Not a list. The constraint in a business this size is Brad's
attention, and a review that ends in nine priorities has spent it.

Choose by leverage — where does one action produce the largest change in weighted
pipeline — not by deal size.

## Step 6 — Write back and push

Apply all corrections, append stage changes to `activity-log.md`, push to Drive,
confirm the sync.

## Output format

```
PIPELINE REVIEW — <date>

RECONCILED
<n> corrections applied: <one line each — what was wrong, what it is now>

POSITION
Live deals:    <n>  ·  $<total>
Weighted:      $<weighted>
  Committed    $<x>  (<n> deals, procurement+)
  Probable     $<x>  (<n> deals, qualified/proposal)
  Possible     $<x>  (<n> deals, earlier)

FORECAST
This quarter   $<weighted>  vs target $<x>   <gap>
FY26/27        $<weighted>  vs target $<x>   <gap>
Next 12mo      $<weighted>

<one paragraph: does this get there, and if not, what would have to be true>

STAGE CHANGES
<deal> — <from> → <to> — <why>

STALLED
<deal> — <days since two-way contact> — <what it is waiting on>

RISK
Concentration: <top account> is <n>% of weighted pipeline
<other named risks>

THIS WEEK
<the one deal> — <the one action> — <why this one>
```

## What not to do

- Do not advance a deal because the conversation was encouraging. Exit criteria only.
- Do not blend committed and possible into one forecast number.
- Do not soften the gap to target. Brad needs the real number early, not a kind one.
- Do not delete lost or dormant deals. Win/loss history is what makes the strategy
  review possible.
