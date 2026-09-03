# LinkedIn — data contract and what gets measured

LinkedIn cannot be read from this environment (network-blocked) and scraping it breaks
LinkedIn's User Agreement and risks the account. Two legitimate feeds exist, and both
are enough for engagement analysis and lead-finding.

## Feed 1 — the official data export (quarterly)

LinkedIn → Me → Settings & Privacy → Data privacy → **Get a copy of your data** →
"The works" (larger archive). Arrives by email as a zip within ~24 hours.

Drop the zip into the Drive folder **Sales CRM / linkedin-exports/** named
`linkedin-YYYY-MM-DD.zip`. `scripts/linkedin_export.py` reads it.

Files used, and what each answers:

| File | Answers |
|---|---|
| `Connections.csv` | Who is in the network, where they work now, when they connected. Mapped against the ~200 addressable organisations → warm routes in. Position/company diffs between exports → **champions who have moved**. |
| `Shares.csv` | Every post: date, text, URL. The publishing history. |
| `Reactions.csv` / `Comments.csv` | What *Brad* engaged with — the "50 people" list, measured rather than assumed. |
| `Invitations.csv` | Sent vs received, with messages — inbound interest and outreach conversion. |
| `messages.csv` | Every DM. Grep for organisations in the CRM → conversations that never made it into the pipeline. |
| `Profile.csv` / `Positions.csv` | Headline and About as written — checked against the positioning in `sales/linkedin-plan.md`. |
| `Endorsement_Received_Info.csv`, `Recommendations_Received.csv` | Social proof inventory for the Featured section. |

What the export does **not** contain: impressions, reach, profile-view counts, or
per-post reaction counts on Brad's own posts. Those are only in the LinkedIn UI.

## Feed 2 — notification emails (continuous)

LinkedIn emails every reaction, comment, mention, profile view digest, connection
request and InMail. Read by the sales skills the same way Gmail is read now — **but
only if they land in `brad@bundleofrays.com`**. As at 2026-09-04 none do; the LinkedIn
account is registered to a different address.

Fix, once: LinkedIn → Settings → Sign in & security → Email addresses → add
`brad@bundleofrays.com` and make it primary. Then Settings → Notifications → set
"Posting and commenting", "Connecting", "Messaging" and "Who viewed your profile" to
email. From that day, every engagement event is a Gmail message the CRM can read.

## Metrics that matter (and the ones that do not)

Measured monthly from the two feeds, written to `sales/linkedin-metrics.md`:

- **Conversations traceable to a post** — the only metric that decides whether the
  channel is working. Target: 3 by 1 Jan 2027 (`linkedin-plan.md`).
- **Named-list coverage** — of the 50 target people, how many did Brad comment on this
  month (from `Comments.csv`), and how many engaged back (from notification emails).
- **Inbound** — connection requests and DMs from ICP organisations, by organisation.
- **Champion movement** — connections whose company changed since the last export.
- **Publishing consistency** — posts per week against the two-a-week cadence.

Not measured: follower count, impressions, "engagement rate". Vanity for a market of
500 people.

## Post-level engagement (semi-manual, monthly)

Per-post reactions and comments are visible only in the UI. Monthly, Brad opens
Profile → Activity → Posts and pastes the last month's posts with their reaction and
comment counts into a Drive doc named `linkedin-posts-YYYY-MM`. Ten minutes. The
script merges it with `Shares.csv` and reports which formats (appraisal, build-in-
public, deployment note, PhD) actually produce comments from target people.
