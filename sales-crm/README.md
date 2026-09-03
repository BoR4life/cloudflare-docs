# Sales agent

A file-backed CRM and four skills that run Brad's sales process for Bundle of Rays
Academy, using the Gmail, Fireflies, Google Calendar, Google Drive and Xero
connectors that are already attached.

Built on the same pattern as `financial-checkpoint`: a plain-text store that is the
single source of truth, a data contract that keeps it honest, and short outputs that
end in one decision.

## The four skills

| Skill | Cadence | Question it answers |
|---|---|---|
| `sales-followups` | Daily / a few times a week | What do I need to send today, and what did I promise on a call and not deliver? |
| `sales-pipeline` | Weekly | What is really going to close, and which one deal do I move this week? |
| `sales-prospect` | Ad hoc | Is this account worth the time, who do I talk to, and how do I get in warm? |
| `sales-strategy` | Quarterly | Is the shape of the business right — concentration, segments, pricing, capacity? |

They trigger on ordinary phrasing — "who's gone cold", "what's my forecast", "find me
leads", "where should I focus" — so there is nothing to memorise.

## Layout

```
sales-crm/
  SCHEMA.md          data contract — record formats, sync protocol
  STAGES.md          eight stages, exit criteria, confidence, cadence
  BOOTSTRAP.md       first-run build from Xero, Gmail, Fireflies, Calendar
  templates/         empty CRM files to copy into sales/
.claude/skills/
  sales-followups/   sales-pipeline/   sales-prospect/   sales-strategy/
sales/               live data — GITIGNORED, mirrored to Google Drive
```

## Where the data lives, and why

**This repo is a fork of a public repository, so it is public.** No customer names,
contact details, deal values or email content are committed. The live CRM lives in
`sales/`, which is gitignored, and is mirrored to a `Sales CRM` folder in Google
Drive so it survives container restarts and follows Brad across devices.

Every skill pulls from Drive at the start of a run and pushes after any write, and
reports the sync result. A silent sync failure would mean the next session starts from
stale data, so it is never silent.

## First run

Say "bootstrap the sales CRM". It builds the initial pipeline from sources that
already exist — customers and lifetime value from Xero, live conversations from
Gmail, commitments made on calls from Fireflies, meeting cadence from Calendar —
rather than asking for a pipeline from memory. Ten to fifteen minutes.

Then fill the placeholders in `sales/playbook.md`: the revenue target, real prices,
real proof points. The skills read that file for how to sell, and it is the one part
the sources cannot supply.

## Design decisions worth knowing

**The qualified gate.** A deal does not pass stage 5 until the funding source is
named, the economic buyer is identified and a timeline exists. This is deliberately
strict, and it will demote deals that feel healthy. In a market where budgets are
grant-funded, committee-approved and expire on a fixed date, a warm conversation with
no identified money is not a deal — and a forecast that counts it is not a forecast.

**`last-touch` means two-way contact.** Emails Brad sent and nobody answered do not
count. Without this distinction a deal where he has sent three unanswered emails looks
more active than one waiting on his reply, which is exactly backwards.

**Undelivered commitments are tracked from Fireflies.** The most common reason these
deals go quiet is a scope or a price that was promised on a call and never sent. That
is invisible in an inbox and obvious in a transcript.

**Nothing sends itself.** Every email is created as a Gmail draft for review. The
agent writes to the CRM on its own; it does not talk to customers on its own.

**Outputs end in one decision.** The weekly review names one deal. The quarterly
review names two or three changes. A review that produces nine priorities has spent
the scarce resource, which is attention, not information.
