# CRM data contract

The CRM is plain markdown, one record per block, in the **live data directory**.

## Where the data lives

| Layer | Location | Committed? |
|---|---|---|
| Working copy | `sales/` at repo root | **No** — gitignored |
| Canonical store | Google Drive folder `Sales CRM` | n/a |
| Templates + logic | `sales-crm/`, `.claude/skills/sales-*` | Yes |

**This repository is a fork of a public repo, so it is public.** Customer names,
contact details, deal values and email content must never be committed. Everything
real lives in `sales/`, which is gitignored, and is mirrored to Google Drive so it
survives container restarts and follows Brad across devices.

### Sync protocol

Every skill in this set runs the same two steps:

1. **Pull, at the start of any run.** If `sales/` is missing or empty, search Google
   Drive for the `Sales CRM` folder and download `playbook.md`, `accounts.md`,
   `opportunities.md`, `activity-log.md`, `leads.md` into `sales/`. If the folder
   does not exist, run the bootstrap in `sales-crm/BOOTSTRAP.md` instead.
2. **Push, after any write.** Update the corresponding Drive file. Never leave a
   change only in the container — it will be lost when the session ends.

If a Drive write fails, say so in the output. A silent failure means the next
session starts from stale data.

## Files

### `sales/opportunities.md`

The core file. One block per live deal. Never delete a block — move it to stage
`won`, `lost` or `dormant` and keep it, because win/loss history is what makes the
strategy skill useful.

```
## OPP-014 — Nursing simulation rollout
account:        Northern Rivers University
contact:        <name>, <role>
economic-buyer: <name>, <role>          # who signs; often not the contact
procurement:    <name or "not yet identified">
stage:          proposal
value:          58000
currency:       AUD
funding:        operational              # grant | operational | capital | research | unknown
funding-window: FY26/27, must spend by 30 Jun 2027
confidence:     55
expected-close: 2026-11-30
next-action:    Send revised scope excluding hardware
next-action-due: 2026-09-04
last-touch:     2026-08-22               # last two-way contact, not last email sent
source:         existing customer expansion
competitor:     <name or none known>
risks:          No confirmed budget line; champion is acting head until Nov
```

**Field rules**

- `stage` — one of the eight in `STAGES.md`. A deal only moves forward when the
  exit criteria for its current stage are met, not when it feels like progress.
- `value` — bare number, no symbols or separators, so it can be summed.
- `funding` — the single most predictive field in this business. A deal with no
  identified funding source is not a real deal regardless of how warm the
  conversation is; it belongs in `scoped` at best.
- `funding-window` — public health, university and government money expires. Record
  the deadline it must be spent by. This drives urgency that is real rather than
  manufactured.
- `confidence` — integer 0–100. Set it from the stage's baseline in `STAGES.md`,
  then adjust for named, written-down reasons. Never round up out of optimism.
- `last-touch` — the date of the last **two-way** contact. An unanswered email you
  sent is not a touch. This distinction is the whole basis of the follow-up sweep.
- `next-action` — a specific thing Brad does, in a verb. "Follow up" is not an
  action. "Send the revised scope excluding hardware" is.
- `next-action-due` — every live deal has one. A deal with no dated next action is
  the definition of a stalled deal and the pipeline skill will flag it.

### `sales/accounts.md`

One block per organisation, independent of any single deal. Accounts outlive
opportunities, and in this business the same account buys repeatedly.

```
## Northern Rivers University
type:            university            # hhs | university | govt-dept | publisher | private-provider | other
segment:         health & nursing faculty
region:          NSW (Lismore)
relationship:    customer               # prospect | active-opportunity | customer | dormant-customer | lost
lifetime-value:  45000                  # AUD, from Xero
first-won:       2025-09
contacts:
  - <name>, <role> — champion
  - <name>, <role> — economic buyer
  - <name>, <role> — procurement
buying-cycle:    Semester planning Nov–Feb (S1) and Jun–Jul (S2)
notes:           Prefers evidence-backed procurement; cited DEFINE work in last scope.
```

### `sales/contacts` — not a separate file

Contacts live inside their account block. A contact who changes employer becomes a
new line under the new account, with the old one marked `— departed <date>`. In this
sector people move between health services and universities constantly, and a
champion who moves is a warm lead at their new employer, not a lost contact. The
prospecting skill checks for this explicitly.

### `sales/leads.md`

Unqualified organisations that fit the ICP but have had no contact, or contact that
has not yet produced a two-way conversation. One line each, so the list stays
scannable.

```
- Example Regional HHS | hhs | QLD | ICP fit 8/10 | no contact | source: HHS directory | 2026-08-30
```

A lead is promoted to an opportunity block in `opportunities.md` the moment there is
a two-way conversation with a named person. Until then it stays here.

### `sales/activity-log.md`

Append-only. Never edit or reorder past entries; this file is the audit trail that
makes "what did we actually do last quarter" answerable.

```
2026-08-30 | OPP-014 | Northern Rivers University | email-out | Sent revised scope, hardware excluded
2026-08-28 | OPP-014 | Northern Rivers University | meeting   | Fireflies: FF-8821. Champion confirmed budget sits with faculty, not IT.
```

Types: `email-out`, `email-in`, `meeting`, `call`, `proposal-sent`, `invoice-sent`,
`stage-change`, `note`.

### `sales/playbook.md`

The reusable selling material: ICP definition, offers and pricing, proof points,
standard objections and the answers that have worked, and the email patterns. It is
the only file the skills read for *how to sell* rather than *what is happening*.
Update it whenever an objection gets a better answer — it compounds.

## Reading the files

Skills read these with `grep` and `sed` rather than loading whole files, so keep the
block format exact. Useful patterns:

```sh
# every deal in a given stage
grep -n "^stage: *proposal" -B 12 sales/opportunities.md

# every deal with an overdue next action
grep -n "^next-action-due:" sales/opportunities.md

# total value of the live pipeline
grep "^value:" sales/opportunities.md | awk '{s+=$2} END {print s}'
```
