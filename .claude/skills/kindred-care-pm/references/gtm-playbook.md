# Go-to-market playbook — Kindred Care

**Kindred Care's buyer is currently UNKNOWN** (see `canonical-facts.md`). This file
is therefore a decision framework, not a plan. Its job is to force the buyer choice
early, because almost every other decision — pricing, evidence, safety design,
regulatory position, raise size — falls out of it.

## The one question that unblocks the market track

> **Who signs the contract, and out of which budget line?**

Not who loves the product. Not who uses it. Who signs, and where the money comes
from. Until that is answered with a named organisation and a named budget, CRL is
capped at 2.

## Five candidate buyers — pick one to lead with

Leading with one does not abandon the others; it decides what gets built and
evidenced first. Trying to serve all five simultaneously is the most common way a
care-sector venture stalls at CRL 3.

| Buyer | Pays for | What they require before signing | Sales reality |
|---|---|---|---|
| **Aged care provider** (residential or in-home) | Staff time saved, resident wellbeing, compliance and quality evidence | Safety and escalation design, privacy position, insurance, evidence from a comparable service, IT/security review | Long cycles, thin margins, committee decisions; the enthusiast is rarely the signer |
| **Disability / NDIS provider or participant** | Funded supports under a plan | Clarity on whether it is a claimable support; participant consent; safeguarding | Funding-rule dependent — verify current NDIS support categories before promising claimability |
| **Health service / PHN / hospital** | Discharge support, chronic condition support, workforce relief | Clinical governance sign-off, likely a regulatory position, integration with existing systems | Slowest cycle, highest credibility payoff, highest chance of tripping the medical-device line |
| **Family / self-pay consumer** | Peace of mind for a parent or relative | Trust, price point, ease of setup for a non-technical older user | Fast to test, brutal on churn and CAC; a real business only at volume |
| **Education / workforce** (via Bundle of Rays and ACU) | Training care workers and students | Curriculum fit, learning outcomes, institutional procurement | Closest to Brad's existing capability and network; smallest cheque; strongest evidence flywheel |

For whichever is chosen, write into `kindred-care/program-board.md`: the named
organisations, the named budget line, the decision-maker's title, and the cycle
length you are assuming.

## Kindred Care's actual unfair advantage — use it deliberately

Care organisations do not buy features. They buy **reduced risk and defensible
evidence**, because they answer to regulators, families, and boards.

Brad is running a PhD that produces peer-reviewed evidence about exactly this class
of product, including its failure modes. That is not a side project sitting next to
the venture — it is the venture's most differentiated GTM asset. Almost no competitor
in this space can put a published, ethics-approved, independently-reviewed evidence
base on the table.

So the sequencing is: **evidence first, features second.** Design pilots to produce
publishable results. Let the papers do the selling.

The constraint on this: the evidence must be genuinely independent to be worth
anything, and the moment Kindred Care markets *on* the research, the COI declaration
has to be visible and honest. Run `acu-jv-and-phd-firewall.md` before any marketing
material references the PhD, ACU, or a published paper.

## Pilots that prove something

Free pilots are easy to get in Australian care and prove almost nothing — a free
pilot tests curiosity, not budget. Design every pilot to clear CRL 5 or 6:

- **Signed agreement** naming scope, duration, and what each side provides.
- **Success criteria written before the pilot starts**, with numbers, agreed by the
  provider. Pre-declared or it is not evidence.
- **Someone accountable for collecting the data** — name them; providers are busy and
  data collection is the first thing dropped.
- **A defined end date and a defined conversion conversation.** Pilots that drift
  become permanent free deployments.
- **Money at CRL 6.** Even a small fee changes the seriousness of the engagement on
  both sides.
- **Ethics coverage** if any of it will be published or feeds Paper 5.

## Pricing — decide the shape before the number

Shape first: per-resident per-month · per-seat · per-service-site licence ·
per-episode · platform fee plus usage · B2B2C where the provider resells to families.

Then anchor the number to the buyer's own economics — a fraction of the staff time
displaced, or of the incident cost avoided — not to your build cost or to what
consumer apps charge. Care buyers will ask you to justify price in their units.

Never price before the buyer choice is made. The same product is a $12/month consumer
subscription and a $60k/year provider licence depending only on who signs.

## Channel

- **ACU** is the highest-value channel *and* a 30% owner *and* the ethics gatekeeper.
  That triple role is an advantage and a governance risk. Every ACU-sourced
  introduction should be logged in the board with what was promised.
- **Peak bodies and provider networks** carry disproportionate weight in Australian
  care — one credible reference travels further than any campaign.
- **This is a small, reputationally networked market.** One bad pilot is known by
  everyone within a year. Prefer three well-run pilots to ten loose ones.

## Competitive position

Maintain a live competitor list in the board, with: what they claim, what they can
evidence, their regulatory posture, and their price where known. Distinguish
companion-AI products, care-provider software incumbents adding AI features, and
overseas products that would need to be localised. Update at every quarterly reset,
and note honestly where a competitor is genuinely ahead — an investor will find them
either way, and being the person who already knows is worth more than the gap costs.

## The artefacts this track must keep current

1. One-sentence product statement any stranger can repeat.
2. ICP definition — named organisations, named roles, named budget line.
3. Pilot protocol template with pre-declared success criteria.
4. Pricing sheet with the reasoning behind the shape.
5. Evidence pack — what can be shown to a buyer today, and what is publishable.
6. Competitor list.
7. Reference list — who will take a call from a prospective buyer.

Anything on that list that does not exist is a milestone on the board, with an owner
and a date. Not a wish.

## Regulatory note

Any claim about clinical benefit, monitoring, triage, or diagnosis changes both the
sale and the legal position — see the regulatory classification gate in
`readiness-ladders.md`. Marketing copy is the most common place a company
accidentally makes itself a medical device. Review every claim against the settled
regulatory position before it is published, and verify current NDIS, Aged Care Act,
and privacy requirements against primary sources at the time of writing rather than
from memory — this sector's rules move.
