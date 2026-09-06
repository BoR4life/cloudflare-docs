# Interface doctrine — how mothers engage with the Companion

Read before any work on modality, channel, engagement design, retention, or the avatar
vendor decision (D-23). Adopted 30 Aug 2026 on Brad's question *"how will people engage
with agents?"*

## The metaphor is wrong, and the metaphor drives the build

The working mental model has been **FaceTime** — you call Elena and she appears. It demos
superbly and it is right for one narrow class of use. It is wrong as the primary metaphor,
because a video call is **synchronous, full-attention, scheduled and socially costly**. It
demands you be presentable, have hands and quiet available, commit a block of time, and
tolerate no interruption.

Now place that against when a mother actually needs the Companion: 2am, feeding, one hand,
dark room, not wanting to wake the baby or her partner. A waiting room. Mid-nappy-change.
Crying and not wanting to be seen. Ninety-second fragments.

**The moments of highest need are the moments video is least usable.** The cost analysis
reached the same conclusion from the spreadsheet (avatar is 69–80% of variable cost); this
reaches it from the user. Two independent lines, same call.

**State the caveat accurately.** Research on disclosure to virtual humans is mixed-to-
positive — people often disclose *more* to an agent they believe is not human-observed. So
a face on the agent is not inherently suppressive. The friction comes from **her camera
being on** and from the synchronous full-attention demand. Those are separable, and they
have different fixes. Do not overclaim this point.

## The right model: a midwife you can text

What a trusted midwife relationship actually is: mostly short asynchronous exchanges;
occasionally a longer conversation when something matters; she knows your history so you
never re-explain; reachable at odd hours without ceremony.

That gives four design commitments:

1. **One persistent thread across the full 16 months** — not sessions. This is what makes
   it a companion rather than a chatbot you re-summon, and it is the retention mechanism: a
   thread with history in it is far harder to abandon than an app you must re-enter.
2. **Text is the default surface.** Fastest, quietest, one-handed, lowest social cost, best
   at 2am.
3. **Voice one tap away**, for when typing is impractical — driving, holding a baby, low
   literacy, low vision.
4. **Video is a deliberate choice, never the front door.**

The platform already supports all of this — Chat shipped, Call live, modality switching
working. **The open question is which is the default and which is the affordance**, and the
product is currently built as though Call is the front door.

## The rule for video: demonstration, not conversation

**Video earns its place where the content is genuinely visual.** Latch position. Bathing
technique. Infant CPR positioning. Perineal care. Settling holds. A demonstration is worth
far more than a paragraph.

A conversation about anxiety, feeding volumes, or whether this discharge is normal is not
visual at all.

This single principle does three things at once: it puts video where it adds value, it
collapses the cost problem (a handful of high-value demonstrations instead of 40 minutes a
month of talking-head conversation), and it gives Hector a **product** argument for D-23
rather than a spreadsheet one — which is a much stronger place to argue from.

## The platform question: it is already built

BoR has already built an agent deployment platform. Read the MVP Board: Workbench, deploy
gate, templates with clone and export, tenant management, RAG corpus management, alerts
inbox (VS-067→097). That is not a Kindred Care feature set. The history confirms it — BLS
tutor, Cultural Awareness tutor, Oncology patient support, ECG trainer, financial education
agent, VU paramedicine avatars, all costed off one framework in Hector's original sheet.

**The question is not whether to build it. It is whether to name it.**

- **Do not reposition the raise.** ACU and Innovation Victoria are funding a maternal health
  venture with Victorian benefit, not a horizontal platform. A platform pitch would weaken
  the raise, not strengthen it.
- **The platform is BoR background IP; Kindred Care is the first vertical.** This is already
  exactly the IP position — platform owned by BoR, licensed to the JV, not assigned. The
  structure already tells the truth.
- **Say it plainly when diligence asks.** "This framework has been deployed across six use
  cases" is evidence of maturity, not distraction.

**The consequence for interfaces:** if one shell serves multiple verticals, modality cannot
be hardcoded. A paramedicine avatar patient genuinely needs video — assessing the patient
*is* the exercise. A student BLS tutor is different again. A mother at 2am is different
again. So: **one shell, modality defaults configured per tenant, each vertical choosing its
own front door.** That makes the platform genuinely reusable and fixes Kindred Care's cost
shape in the same change.

## The channel question — open, and worth testing

Should Kindred Care be an app at all? The equity case — regional, CALD, underserved mothers
— describes precisely the cohort least likely to install an app, keep it installed and
re-open it across 16 months. An app store, storage space and app-switching all work against
the stated mission.

Counter-pressure is real: consent management, tenant isolation, data residency and the
safety architecture all want a controlled surface, and RLS-backed isolation cannot be done
over SMS.

Likely answer: **a PWA with link-based enrolment** — the enrolment-code model already exists
— plus notification-driven re-entry. No app store, no install, controlled surface. **Flag
this as open, not settled.**

## Everything here is answerable by the pilot

Which modality do mothers actually choose? How many avatar minutes do they use when video is
available but not the default? Does the persistent thread hold them across 16 months? What
is the real engagement rate against the modelled 40%?

Eight weeks with 150 mothers answers all of it — and resolves D-23, validates or kills the
engagement assumption, and produces the first efficacy signal, simultaneously. **The agent's
standing position: the build is not the bottleneck, evidence is.**
