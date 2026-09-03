---
name: sales-followups
description: Run Brad's sales follow-up sweep — find every deal owed a touch, every commitment made on a call and not yet delivered, and every thread that has gone quiet, then draft the actual emails. Use when Brad says "follow ups", "who do I need to chase", "who's gone cold", "what did I promise", "sales sweep", or asks what to send someone. Also use after a sales call to turn the meeting into follow-up actions. Not for pipeline review or forecasting — that is sales-pipeline.
---

# Sales follow-up sweep

## Purpose

Deals in this business do not die from rejection. They die from silence — a scope
that was never revised, a price that was never sent, a champion who moved on while
the thread sat untouched for six weeks. This sweep finds those, and produces drafted
emails rather than a list of reminders.

The output is a small number of things to send today. If it produces twenty actions,
it has failed; rank and cut to the five that matter.

Read `sales-crm/SCHEMA.md` and `sales-crm/STAGES.md` before the first run in a
session. The playbook at `sales/playbook.md` holds the email patterns.

## Step 1 — Pull the CRM

Per the sync protocol in `SCHEMA.md`: if `sales/` is missing or empty, restore it
from the `Sales CRM` folder in Google Drive. If neither exists, run
`sales-crm/BOOTSTRAP.md` instead and say so — a sweep against an empty CRM is
worthless.

## Step 2 — Find what is owed

Four passes. Each finds a different kind of neglect, and the third and fourth are the
ones that find money.

**Overdue next actions.** Every opportunity where `next-action-due` is today or
earlier. These are commitments already written down.

**Stale deals.** Every live opportunity where `last-touch` is older than the cadence
for its stage in `STAGES.md`. Remember `last-touch` means the last *two-way* contact
— a deal where Brad sent three unanswered emails last week is stale, not active.

**Undelivered commitments, from Fireflies.** Search transcripts since the last sweep
for anything Brad said he would do. Phrases that matter: "I'll send", "let me get
you", "I'll put together", "I'll introduce you to", "leave that with me". Cross-check
each against `activity-log.md` — if there is no matching `email-out` or
`proposal-sent` since the call, it is outstanding. This pass catches the deals that
are quietly dying because the ball is on Brad's side of the court and nobody
remembers.

**Unanswered inbound, from Gmail.** Threads with an inbound message more recent than
any outbound reply, from anyone on an account or lead. An unanswered question from a
prospect is the most expensive item on this list.

## Step 3 — Rank

Rank by expected value at risk, not by age:

```
priority = (value × confidence/100) × urgency_multiplier
```

Urgency multiplier: `3.0` if a funding window closes within 60 days, `2.0` if the
ball is on Brad's side of the court and has been for over a week, `1.5` if an inbound
question is unanswered, `1.0` otherwise.

Then apply judgement over the arithmetic. A $15k deal with a champion who just did
something effortful outranks an $80k deal that has been silent for two months. Say
when you are overriding the score and why.

## Step 4 — Draft

Draft the top five as actual sendable emails, using the patterns in
`sales/playbook.md`. For each one:

- Pick the pattern that fits — evidence drop, named next step, funding-window prompt,
  or genuine check-out. Say which one and why in a single line above the draft.
- Pull the specific context from the thread and the transcript. A follow-up that does
  not reference something particular they said is a template, and reads like one.
- Carry something new. If there is nothing new to say, that is a signal the deal
  needs a different move — an introduction, a call, or parking — not another email.
- Keep it to five sentences. These are busy clinicians and academics.
- Propose one clear next step with a date.

Never send "just checking in" or "circling back". Where the honest position is that
four touches have gone unanswered, draft the check-out email and recommend parking
the deal as `dormant`. That is a real outcome, and it frees selling time.

**Create the drafts in Gmail rather than sending them.** Brad reviews and sends.
Only send directly if he explicitly says to, in this session, for a specific email.

## Step 5 — Write back

For every draft created:

- Update the opportunity's `next-action`, `next-action-due`, and — if the draft
  answers a commitment — clear it.
- Append to `activity-log.md`.
- Do **not** update `last-touch`. That field only moves when *they* respond. Getting
  this wrong makes every future sweep blind.

Then push all changed files to Drive and confirm.

## Output format

```
FOLLOW-UP SWEEP — <date>

Owed: <n> actions across <n> deals · $<value at risk> weighted

SEND TODAY
1. <Account> — <OPP-id> — $<value>, <confidence>%
   Why now: <one line — the funding window, the unanswered question, the promise>
   Pattern: <which email pattern>
   Draft: <created in Gmail | inline below>

<...up to 5>

ALSO OWED (not drafted)
- <Account> — <what is owed> — <why it ranked below the cut>

PARK
- <Account> — <n> unanswered touches — recommend dormant, check-out email drafted

CRM UPDATED
<files changed> · Drive sync: <ok | FAILED — reason>
```

## What not to do

- Do not draft a follow-up with no new information in it. Recommend a different move.
- Do not mark a deal as touched when only Brad has spoken.
- Do not manufacture urgency. Real deadlines exist in this sector — budget years,
  grant acquittals, semester dates. Use those, and only those.
- Do not chase a deal that fails the ICP. Recommend dropping it and say why.
