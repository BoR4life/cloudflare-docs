# Stages and exit criteria

These stages are built for how Australian public health services, universities and
government departments actually buy: slowly, through a committee, with money that
comes from somewhere specific and expires on a known date. A generic SaaS funnel
does not fit, because the bottleneck here is almost never interest — it is funding
and procurement.

A deal moves forward **only** when the exit criteria are met. Enthusiasm is not an
exit criterion. If a stage's criteria are not met, the deal stays where it is and
the unmet criterion becomes the next action.

| # | Stage | Baseline confidence | Exit criteria — all must be true to advance |
|---|---|---|---|
| 1 | `identified` | 5 | Organisation fits the ICP and a named individual has been identified as the likely champion. |
| 2 | `contacted` | 10 | Outreach has been sent to that named person. |
| 3 | `engaged` | 20 | **Two-way** conversation has happened. They have replied with something other than an acknowledgement. |
| 4 | `scoped` | 35 | The cohort, delivery mode and rough size are agreed, and a specific problem has been stated in their words. |
| 5 | `qualified` | 50 | Funding source is **named** (which budget, grant or line), the economic buyer is identified, and a decision timeline exists. |
| 6 | `proposal` | 65 | Written proposal or quote issued, priced, with scope and dates. |
| 7 | `procurement` | 80 | Verbally agreed, now moving through their PO / panel / contract / insurance / privacy process. |
| 8 | `won` / `lost` / `dormant` | 100 / 0 / 0 | Signed and invoiced / explicitly declined / no two-way contact in 90 days with no scheduled next step. |

## The qualified gate is the important one

Stage 5 is where this pipeline earns its accuracy. Everything before it is a
conversation; everything after it is a purchase. Deals sit in `scoped` looking
healthy for months because the champion is genuinely enthusiastic and genuinely
has no money.

To pass the gate, three things must be written into the opportunity block:

- **`funding`** — not "they have budget" but *which* budget. A research grant, a
  training line in the operational budget, capital for hardware, or an
  innovation-fund allocation. These behave completely differently.
- **`economic-buyer`** — the person who can commit the money. In a hospital and
  health service this is rarely the educator you have been talking to. In a
  university it is usually the Head of School or a Dean, not the academic running
  the unit.
- **`funding-window`** — the date the money expires. Australian financial year ends
  30 June and unspent budget is frequently forfeited; grant funds have acquittal
  deadlines; university money follows semester planning. This date is where real
  urgency comes from, and it is urgency you can name without pressuring anyone.

If any of the three is unknown, the deal is not qualified, the confidence stays at
35 or below, and the next action is to find the missing one.

## Confidence adjustments

Start at the stage baseline, then adjust — and write the reason into `risks`:

| Signal | Adjust |
|---|---|
| Champion has done something effortful unprompted (booked the room, forwarded to finance, drafted the internal case) | +10 |
| Existing customer expanding | +10 |
| Funding is confirmed operational or already-granted money | +10 |
| Champion is acting, interim or newly appointed | −10 |
| No contact with the economic buyer at all | −10 |
| Deal requires hardware purchase they have not budgeted for | −15 |
| Restructure, machinery-of-government change, or hiring freeze at the account | −20 |
| Last two-way contact more than 30 days ago | −15 |

Cap the result at the next stage's baseline. If a deal in `scoped` computes to 65,
the pipeline is telling you it should have been qualified already — go and qualify
it rather than inflating the number.

## Cadence by stage

Public sector and university buyers move slowly and respond badly to pressure, but
they also genuinely forget. The failure mode here is not chasing too hard, it is
going quiet for two months and losing the thread. Follow-up intervals:

| Stage | Interval between touches | Character of the touch |
|---|---|---|
| `contacted` | 7 days, then 14, then 30, then park | Each one carries something new — never "just checking in" |
| `engaged` | 10–14 days | Useful material: evidence, a comparable deployment, a short answer to their question |
| `scoped` | 7–10 days | Drive toward the funding question |
| `qualified` | 7 days | Drive toward the written proposal |
| `proposal` | 5–7 days | Offer to present it to the decision group |
| `procurement` | 14 days | Ask what document they need next; be the easiest vendor in the process |
| `dormant` | 90 days | Re-open with something genuinely new — a publication, a new cohort format |

Four unanswered touches in `contacted` with no reply means park it as `dormant` and
move on. That is not failure, it is the correct read on a fixed amount of selling
time.
