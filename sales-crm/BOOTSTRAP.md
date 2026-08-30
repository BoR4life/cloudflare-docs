# Bootstrap — first run only

Run this once, when `sales/` does not exist and there is no `Sales CRM` folder in
Google Drive. It builds the initial CRM from sources that already exist rather than
asking Brad to type in a pipeline from memory.

Takes 10–15 minutes. Every figure that lands in the CRM carries where it came from
and when, in the same way the financial ledger does — a deal value with no source is
a guess, and guesses are what make a pipeline useless.

## 1. Create the store

```sh
mkdir -p sales
cp sales-crm/templates/*.md sales/
```

Then strip the template placeholder blocks from each file, leaving the headers.

## 2. Accounts, from Xero

Xero is the only source that knows what has actually been paid, so it seeds accounts
rather than opportunities.

- `get_organisation_financial_year` — establish the FY boundaries.
- `get_top_customers_by_revenue` for the current and two prior financial years.
- `get_contacts` for names and contact details on those accounts.

For each customer, write an account block with `relationship: customer`,
`lifetime-value` summed across the years pulled, and `first-won` from the earliest
invoice. Record the FY split in `notes` — it shows which accounts are growing and
which have gone quiet, which is the first thing the strategy skill looks at.

An account that bought two years ago and nothing since is `dormant-customer`, and
that is a lead, not a closed chapter. Re-engaging one is cheaper than any new logo.

## 3. Live conversations, from Gmail

Search the last 120 days for two-way threads with the account domains found above,
plus threads matching the ICP: `nursing`, `simulation`, `clinical education`,
`health service`, `faculty`, `VR training`, `proposal`, `quote`, `scope`.

For each thread with a genuine two-way exchange, create an opportunity block. Set:

- `stage` by the evidence in the thread, judged against the exit criteria in
  `STAGES.md` — not by how warm it reads. Most threads land in `engaged` or
  `scoped`. Very few pass the qualified gate, and that is the honest picture.
- `last-touch` to the date of the most recent message **from them**. If the last
  three messages are all outbound, the deal is colder than it looks and the
  follow-up sweep needs to know that.
- `value` only where a number was actually discussed. Otherwise `0` and a note in
  `risks` that it is unsized.
- `funding: unknown` unless a budget, grant or line item is explicitly named. Do not
  infer funding from enthusiasm.

## 4. Commitments, from Fireflies

`fireflies_get_transcripts` for the last 120 days. For each meeting matching an
account or prospect:

- Pull the summary and action items.
- Extract anything Brad **committed to** — pricing to send, a scope to revise, an
  introduction to make. Each becomes a `next-action` on the relevant opportunity,
  dated. Undelivered commitments from past calls are the single most common reason
  these deals go quiet, and they are invisible until you go looking.
- Extract anything **they** committed to, into `risks` or `notes`.
- Log each meeting in `activity-log.md` with the transcript ID.

## 5. Cadence, from Calendar

`list_events` for the last 180 days and the next 60. Establish per-account meeting
cadence and record it in the account's `buying-cycle`. Add any upcoming meeting as a
dated next action so it gets a brief prepared.

## 6. Playbook

Copy the template to `sales/playbook.md` and fill what the sources support: real
deployments as proof points, real objections found in email threads, real prices from
issued quotes. Leave the rest as placeholders — a placeholder is honest, an invented
case study is not.

## 7. Reconcile before finishing

The equivalent of the financial ledger's reconciliation step:

- Every account in Xero with revenue is an account block.
- Every opportunity references an account that exists in `accounts.md`.
- Every live opportunity has a `next-action` and a `next-action-due`.
- Every opportunity past `scoped` has a named `funding` and `economic-buyer`, or is
  demoted to `scoped` with finding the missing one as its next action.

Report anything that fails these checks rather than quietly fixing it. A pipeline
that fails reconciliation on day one is telling you something true.

## 8. Push to Drive

Create the `Sales CRM` folder in Google Drive and upload all five files. Confirm each
upload succeeded and report the folder link. From this point the pull/push protocol
in `SCHEMA.md` applies to every run.
