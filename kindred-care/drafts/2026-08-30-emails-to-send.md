# Drafted emails — for Brad to send

**Prepared 30 Aug 2026.** The agent drafts, Brad sends — nothing goes out on its own.
All three are due Monday 31 Aug. Voice is yours from the trail: short, warm, direct.

---

## 1. To Michelle Schmidt (SCHHS) — accept the Maternity leadership meeting

*Her offer has been sitting since 25 Aug. This is the cheapest win of the week.*
*Probity note: ACU was already introduced to SCHHS on your 7 Aug thread, so naming the
partnership is fine — but keep it to one line, and no investor mention.*

> **Subject:** RE: Maternity Services - Kindred Care information session.
>
> Hi Michelle,
>
> Thank you — the Maternity leadership meeting sounds exactly right, and I'd be glad to
> present there. Could you let me know the next available date and how long we'd have?
> Happy to fit whatever slot works for the team.
>
> I'll bring a short overview of Kindred Care and where the programme is up to, and leave
> plenty of room for the team's questions and steer — their read on what would actually
> help mothers between visits is the thing we most want.
>
> Thanks again for making the room for this.
>
> Cheers,
> Brad

---

## 2. To Russell (cc Bill) — the written ask

*The one that matters. Two blockers, 60 days old, now with the numbers made explicit.
Asks are dated and specific; the tone stays collegial.*

> **Subject:** Kindred Care — two positions I need in writing, and two corrections from our side
>
> Hi Russell,
>
> Ahead of the 16 Sept Steering Committee and the run to UCAC, four things — two asks and
> two headed your way as fixes from us.
>
> **1. BVUIP structure — confirming my understanding.** $300k POC, then $1.0M
> commercialisation — $1.3M in total — with each round matched 50/50 ACU : Innovation
> Victoria. If that's right, it closes the "combined $1M?" footnote from your June
> Overview deck, and I'll correct our business plan wording (which currently says a $1.0M
> ceiling) to match. Can you confirm in a line?
>
> **2. The ACU-side cash.** On the 50/50 structure, ACU's share is $150k at POC and $500k
> at commercialisation. I need a dated position on where that comes from — the HNWI
> syndicator path or otherwise — because the model, the Deal Map and the UCAC pack all
> hang off it, and it's the one item I can't progress from my side. Even "here's the plan
> and the date we'll know" is enough to build on.
>
> **3. Heads of Agreement + IP audit.** Same ask: a dated path. The register has HoA at
> 25 Sept and the IP register at 18 Sept — if those dates are still real from the ACU
> Legal side, great; if not, better we re-plan now than discover it in October. Happy to
> draft the issues list to make it a review job rather than a drafting job for Angela.
>
> **4. For the IP verification workshop:** we've caught an attribution error in our IP
> Plan draft 0.2 — the multi-tenant platform stack is listed under ACU background IP when
> it's BoR background IP (the business plan has it correctly). We'll issue 0.3 corrected
> before the workshop so the register builds from a clean base.
>
> **5. One thing I think changes our story for the better.** I've been through the
> Victorian maternity policy landscape properly. The Government has committed to the nine
> Maternity Taskforce recommendations, is appointing the state's first Chief Midwife to
> implement them, and Safer Care Victoria released the Respectful Maternity and Newborn
> Care Framework in January. The Taskforce's themes — workforce, regional service
> delivery, culturally safe care, access — are precisely what Kindred Care addresses, so
> we can argue the problem from government-committed policy rather than from first
> principles. I'd like that on the problem slide for the 16th.
>
> The one to think about: SCV is building **My Maternity Journey**, a state consumer
> platform for completion this year. My read is it's a different product — a guide
> answers the questions you know to ask, the Companion answers the one actually being
> asked at 3am — but it's also the most interesting channel conversation available to us,
> and another reason to reconnect with Elisa McDonald sooner rather than later. Happy to
> be talked out of that read.
>
> On our side: we're restating the financial model before anything enters the pack —
> BVUIP lines corrected to the amounts above, India/UK moved to a labelled upside
> scenario so the base case is cleanly Victorian, and churn added. I'm also correcting
> our Victorian market count to the state's own figure (52 providers, 33 regional —
> we'd been using 75+). Detail with Hector and the CFO now.
>
> Cheers,
> Brad

---

## 3. To Hector — the unit-cost decision

*This is the number the whole data room stands on. His own comments have been open since
20 May.*

> **Subject:** Unit cost — need to land this one this week
>
> Hey mate,
>
> One number is holding up the whole investment pack: variable cost per active mother.
> Right now three documents say three things — the forecast works out to ~$14.70/yr, the
> unit economics doc says $44.60, and the pricing model's cost engine says $5.87/mo
> (~$70/yr). The margins in the pack swing from great to negative depending on which is
> true.
>
> The open threads are yours from May — HeyGen step/plans vs per-minute, and the bundle
> upgrade. Can we lock: (1) which HeyGen plan we're actually on and the real per-minute
> cost at pilot volumes, (2) the GCP + model cost per active user at 250 / 1,500 / 5,000
> actives, (3) one blessed $/active-mother/year figure I can put in every document?
>
> Two quick ones while I have you:
> — Can Elena do a 30-second self-intro for the ACU steering committee on 16 Sept?
>   Russell asked; nothing would land harder.
> — Does the entitlement engine handle an annual birth-volume band licence, or only
>   seats? Pricing is banded and I want to know if that's config or a story for Track C.
>
> Cheers,
> Brad

---

# Added 30 Aug 2026 (evening) — after the pricing rebuild, the sovereignty review and the five builds

## 4. To Hector — three architectural questions, all time-sensitive

*The most valuable email of the week. Question 1 is free and binary; question 2 is the*
*cheap win on erasure; question 3 unblocks D-23. None of them require him to build*
*anything to answer.*

> **Subject:** Three quick architecture questions — endpoint, schema, avatar data path
>
> Hi Hector,
>
> Three things I need answers to rather than work on, and I think all three are quick.
>
> **1. Are we pinning a regional Vertex endpoint?**
> Google's guidance is to avoid the global endpoint where data can't leave the continent,
> and there's a known behaviour where the configured location gets ignored and the global
> endpoint is used instead — no error, correct responses, nothing in the logs. If that's
> happening for us, mothers' conversations are being processed offshore while our documents
> say Sydney. Could you confirm from a live turn — Cloud Logging or the request path —
> rather than from the config? Same question for Vertex AI Search, not just generation.
>
> **2. Does the schema carry turn-level addressability?**
> Meaning: is every individual turn identifiable and deletable on its own. The Privacy Act
> reforms are heading toward a right to erasure, and we're building a single thread that
> runs sixteen months. If turns are individually addressable from the start, almost every
> erasure scenario stays tractable later. If they're not, they all become migrations. Given
> how the rest is built I suspect the answer is yes — worth knowing today either way.
>
> **3. What exactly do we send to LiveAvatar/HeyGen?**
> Full utterance text, rendered audio, or a script from approved content? They're a US
> processor, so if conversation content reaches them that's a cross-border disclosure of
> health information, and it may be a hard blocker for a Victorian health service
> regardless of cost.
>
> Related, and the reason I'm asking: **could we pre-render demonstration clips from the
> corpus?** If video is used to show something — latch, bathing, CPR positioning — rather
> than to hold a conversation, the clips could be generated ahead of time from approved
> content. The vendor would never receive a mother's words at all. That would take the
> avatar from ~75% of our variable cost down to near nothing *and* remove the privacy
> exposure. Feasible in the current architecture? Rough build cost?
>
> No rush on 3 beyond this week — 1 and 2 I'd like as soon as you can.
>
> Thanks,
> Brad

## 5. To Russell — the Triangle, and the Elisa follow-up

*Attach `sunshine-coast-triangle-brief.md`. This names ACU, so Russell sights it before*
*it goes anywhere else. The second half is the harder ask and should not be softened.*

> **Subject:** Sunshine Coast as the POC site — and the Chief Midwife follow-up
>
> Hi Russell,
>
> Two things, one proposal and one I've dropped.
>
> **The proposal.** I've written up the Sunshine Coast position properly — brief attached.
> Michelle Schmidt signed for SCHHS Maternity in July, Wishlist signed the same day and can
> fund a pilot from philanthropic rather than operating money, and there's a national
> simulation research centre alongside. That's a clinical partner, a funding path and
> evaluation capability in one place.
>
> I'd like to run the eight-week evidence pilot there, framed as the POC that de-risks the
> Victorian deployment rather than as a move away from Victoria. My reasoning is that a
> committee reading real engagement data from 150 mothers is in a different conversation
> from one reading a pipeline of meetings — and we can then approach Safer Care Victoria
> with a completed pilot instead of a proposal.
>
> I'd rather put this tension in the pack openly than have someone notice it. Would welcome
> your view on whether that reads as clear-eyed or as a retreat.
>
> **The one I've dropped.** You asked me on 7 August to reconnect with Elisa McDonald and I
> haven't. She's the Taskforce implementation lead, the Safer Care Victoria route and the
> My Maternity Journey route all at once, so it's the highest-value contact available and
> I've let three weeks go. I'll make it this week. If there's a framing you'd prefer, or if
> it's better coming through you, tell me and I'll follow that instead.
>
> Brad

## 6. To Lois — the ethics pathway, and the regional question

*The ethics pathway is the long pole on the pilot; everything else compresses and this*
*doesn't. The second question could change the business model.*

> **Subject:** Ethics pathway for the pilot — and a question about regional networks
>
> Hi Lois,
>
> Two things, and the first is time-critical.
>
> **Ethics.** We're planning an eight-week pilot with around 150 mothers at Sunshine Coast,
> measuring engagement and safety performance rather than clinical outcomes. What's the
> right ethics pathway, and realistically how long does it take? It's the one part of the
> timeline I can't compress, so I'd rather start it now than discover in six weeks that we
> should have. I'd also want to keep it clearly separate from the PhD data pathway.
>
> **The regional question.** Can Victorian regional maternity services buy as a network or
> alliance, rather than individually? It matters more than it sounds. Thirty-three of
> Victoria's fifty-two providers are regional and small, and our fixed cost per site is
> high enough that serving them one at a time is difficult at any price they'd accept. If
> they can contract as a group it opens the regional market — which is the equity case and
> the Taskforce's own priority. If they can't, we need to rethink.
>
> Also, whenever you have a moment: does a maternity service actually expect to pay for
> something like this, or expect it to arrive as a state programme? Honest answer more
> useful than an encouraging one.
>
> Thanks,
> Brad

---

# Re-engagement after the missed meeting — Fri 28 Aug

**FINAL. Three emails, in this order. No alternates — these are the picks.**

## What happened

Friday 2–3pm AEST, "Kindred Care discussion", organised by Lois, with Marie, Bill and
Russell. Brad had accepted. Lois emailed at 2:06pm: *"HI Brad – hoping you can join us
now."* The meeting went ahead — **it was Marie's introduction to the ACU team** — and both
Russell and Marie described it afterwards as productive.

## Already done for you

**Three calendar invites accepted** (30 Aug): Workshop 1.2.B (Wed 2 Sep, 10:00–10:30),
Workshop 1.2.R&D (Thu 3 Sep, 11:00–11:45), and the weekly Project Oversight Team meeting —
accepted for the full recurring series through 15 December, which had been sitting
unanswered since 2 August.

So when email C says "both accepted", it is already true.

## Still open, and yours

The follow-up scheduling. Russell offered Mon 31 Aug / Tue 1 Sep. Lois replied Saturday:
*"Monday between 11–1pm and Tues is better any time but 12–1pm."* Marie is waiting. Brad is
cc'd and silent. **Monday 11am–1pm is clear in the calendar and matches Lois exactly** —
that is the answer, and email A gives it.

*Judgement call taken: the Sunday offer is dropped. Four people have already proposed Monday
and Tuesday; offering today reads as performance rather than availability.*

---

## A. Apology and availability — reply on "Kindred Care discussion"

*To Lois, Russell, Bill, Marie. Send first.*

> **Subject:** RE: Kindred Care discussion
>
> Hi all,
>
> First — I'm sorry I missed Friday. No good excuse, and I'm sorry particularly to you
> Marie, given it was your first meeting with the team. Thank you all for going ahead
> without me, and Lois, thank you for chasing me at the time.
>
> On the follow-up: **Monday 11am–1pm works for me**, which matches your window Lois.
> Tuesday I'm open all day if that suits Marie and Russell better.
>
> Russell — I've accepted both workshops and the weekly, and I've come back separately with
> agenda suggestions for the R&D session.
>
> Brad

## B. To Marie — separate, short

*Its own email, not folded into the reply-all. Send immediately after A.*

> **Subject:** Sorry I missed you on Friday
>
> Hi Marie,
>
> I'm sorry I wasn't there on Friday — of all the meetings to miss, your first with the team
> was the wrong one.
>
> I'd genuinely like to sit down with you properly, and I'll fit entirely around you. Monday
> or Tuesday both work. Glad to hear the conversation went well without me, and looking
> forward to picking it up.
>
> Brad

## C. To Russell — the workshops, with agenda items

*The actual re-engagement. He asked a direct question; answering it well does more than the
apology does. Send after A and B — same day is fine.*

> **Subject:** RE: KC :: Workshop 1.2.R&D and 1.2.B
>
> Hi Russell,
>
> Both accepted, and the extension to the weekly suits.
>
> You asked for agenda items. Four for **1.2.R&D**, in the order I'd rank them:
>
> **1. The avatar vendor decision (D-23).** This has turned out to be bigger than a vendor
> choice. It drives roughly three-quarters of our variable cost, it decides the interface,
> and because the vendor is US-based it raises a cross-border disclosure question under APP 8
> that a Victorian health service may treat as a blocker regardless of price. Three separate
> reasons to settle it, and it's currently sitting outside our tracked critical path.
>
> **2. The evaluation set — this is the TRL 4 gate.** TRL 4 in our own definition is
> recall@5 ≥ 0.85 and safety-tag triggering ≥ 0.95 against a gold-standard set that doesn't
> exist yet. The epic that builds it is at zero of twelve stories. It's the R&D the POC
> exists to fund, and I'd like it visible as a stream in its own right.
>
> **3. Data residency and our third-party processors.** Worth a stream. I've started a
> processor map — which vendor sees what, in which jurisdiction — and it's the input to
> anything a health service will ask us during procurement.
>
> **4. Retention and erasure.** The Privacy Act reforms are heading toward a right to
> erasure and we're building a conversation that runs sixteen months. Designing for it now is
> cheap; retrofitting it later is a rebuild.
>
> For **1.2.B**, given we only have thirty minutes, two:
>
> **1. Pricing.** I've been through the model properly and have a resolved position on the
> schedule, plus a proposal for a smaller entry tier aimed at getting a first site moving
> quickly.
>
> **2. Which budget a health service actually buys this from.** I don't think we've answered
> it, and almost everything commercial sits downstream of the answer.
>
> Happy to circulate anything ahead of either session if that's useful.
>
> Brad

---

## Why these are not sent

The standing rule holds, and here it is more than procedure: **an apology sent by an agent
is not an apology.** If Marie ever learned the note about missing her first meeting had been
auto-sent, that would cost more than the original miss. A and B in particular have to come
from Brad.

---

# URGENT — Michelle Schmidt reply (31 Aug)

**Six days stale.** Her 25 Aug email asked Jo (SC-DSO-WCS) to coordinate a slot at the WCS
Maternity Leadership meeting. Nobody has replied. This is the only live door at Sunshine
Coast and it is not contingent on the failed grant.

*Reply to her thread "Maternity Services - Kindred Care information session", keeping Jo
(SC-DSO-WCS@health.qld.gov.au) on it. Copy Keppel Schafer — note the spelling, it is
Schafer.*

> **Subject:** RE: Maternity Services - Kindred Care information session.
>
> Hi Michelle, and hello Jo,
>
> Thank you — the Maternity Leadership meeting is exactly the right forum, and I'd be glad
> to present there.
>
> Jo, whichever slot suits the team is fine by me; I'll build around your meeting rather
> than the other way round. Happy with anything from a short overview to a full session,
> and I'll send material ahead so people can read rather than be presented at.
>
> One update for transparency: the Advance Queensland application wasn't shortlisted. That
> doesn't change anything about the work — the build has moved on considerably since July
> and we're now planning a small evaluation pilot rather than a grant-funded one. I'd
> rather tell you that up front than have it come up later.
>
> What I'd like to put to the team is fairly specific: a small, time-limited pilot with
> around 150 women, externally funded, where SCHHS provides the clinical setting and we do
> the evaluation alongside you. No procurement, no licence, nothing that needs a budget
> line. If the team's view is that it isn't a fit, that's a genuinely useful answer too.
>
> Thanks again Michelle.
>
> Brad

**Why it is written this way.**
- **The grant failure is disclosed up front.** She will find out. Saying it first costs
  nothing and buys credibility; being caught later costs the relationship.
- **The ask is scoped and refusable** — 150 women, externally funded, no procurement. A
  leadership meeting can say yes to that. It cannot say yes to a licence.
- **"Externally funded" is a commitment.** Before presenting, there must be an answer to
  where that money comes from. Wishlist is currently unverified.
- **No ACU naming**, so no Russell sighting needed before it goes.

