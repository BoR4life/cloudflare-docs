# D-23 — the avatar vendor decision. Brief for Hector and Brad

**30 Aug 2026.** The MVP Board carries D-23 as an out-of-loop item, outside the tracked
critical path. **It should be the most tracked decision in the venture**, because three
independent lines of analysis converge on it and each one alone would justify a decision.

---

## Line 1 — Cost

Avatar video is **69–80% of variable cost** (Cost Engine row 26, verified):

| Tier | Variable cost / active mother / yr | Avatar share | Everything else |
|---|---|---|---|
| Foundation | AUD $70.49 | $56.54 (80%) | $13.95 |
| Enterprise | AUD $44.60 | $30.65 (69%) | $13.95 |

Gemini, Vertex, Search, Cloud Run and storage **combined** cost $13.95 per active mother per
year. The talking head costs two to four times the entire rest of the platform.

The tiers are not loss-making — 70 / 61 / 47 / 6% — so this is a lever, not a crisis. But it
is the **largest single lever on gross margin the venture has**, and it also determines
whether the Enterprise tier can be fixed and whether a sub-$20k entry tier has room.

The rate is already optimised: Cost Engine row 13 models it falling $0.19 → $0.128 → $0.114
→ $0.103 USD/min with volume. **So the remaining variable is minutes, and minutes are a
product decision.**

## Line 2 — Product

The working metaphor has been FaceTime. It demos superbly and it is wrong as a default,
because a video call is synchronous, full-attention and socially costly — and the moments of
highest need are 2am, feeding, one hand, dark room, not wanting to wake anyone.

**The moments of highest need are the moments video is least usable.**

There is also no evidence anywhere in the data room that mothers want a talking head. Not in
the Customer Discovery summary, not in the SMART start retention data. Hector's own note
against the 40-minute assumption reads *"Conservative — could be 30 if voice-only is
dominant."*

The proposed rule: **video for demonstration, not for conversation.** Latch position,
bathing technique, infant CPR positioning, settling holds — genuinely visual, and a
demonstration beats a paragraph. A conversation about anxiety or feeding volumes is not
visual at all.

*Caveat, stated so we do not overclaim: research on disclosure to virtual humans is
mixed-to-positive. A face on the agent is not inherently suppressive. The friction comes from
her camera being on and from the attention demand.*

## Line 3 — Data sovereignty

**HeyGen / LiveAvatar is a US processor.** If any part of a mother's conversation reaches it
to generate speech or video, that is a **cross-border disclosure of health information under
APP 8**, where health information is *sensitive information* and Kindred Care remains
accountable for what the overseas recipient does with it.

For a **Victorian public health service this may be a hard blocker independent of price.**
The same question applies to the STT and TTS vendors the board lists as pending
credentialing — and STT is the higher-risk of the two, because it carries what she said
rather than what the Companion replied.

**Unknown and blocking:** what exactly is sent to the avatar vendor? Full utterance text? A
rendered audio stream? A pre-approved script with no conversational content? These are three
completely different risk positions and the answer decides the option set.

---

## The options

| Option | Cost | Product fit | Sovereignty | Verdict |
|---|---|---|---|---|
| **A. Video standard, 40 min/mo** | Worst | Wrong for the 2am use case | Worst — continuous conversational content offshore | Not recommended |
| **B. Video capped ~10 min/mo, included** | Better | Still defaults to the wrong metaphor | Same exposure, smaller volume | Interim only |
| **C. Voice + text standard; video for demonstration, metered** | **Best** | **Best** — matches how the product is actually used | **Best** — demonstrations can be pre-rendered from approved content, so no conversational content need leave | **Recommended** |
| **D. No avatar** | Best | Loses genuine value on visual technique | No exposure | Over-correction |

**Option C has a property the others do not:** if video is used for *demonstration of
approved content* rather than *conversation*, the clips can be **pre-rendered and cached**.
The vendor then never receives a mother's words at all — it renders from the corpus, not from
her. That converts the highest-risk processor into one that touches no personal information.

**That is the crux of the recommendation.** It resolves all three lines simultaneously:
minutes collapse, the interface matches the need, and the sovereignty exposure disappears
rather than being mitigated.

---

## What is needed to decide

**From Hector, this week:**
1. What data actually reaches the avatar vendor today, precisely.
2. Whether pre-rendering demonstration clips from approved corpus content is feasible in the
   current architecture, and at what build cost.
3. The regional endpoint check (`endpoint-check-for-hector.md`) — same class of question.
4. Whether STT can be sourced onshore, and at what quality cost.

**From the pilot, in eight weeks:** avatar minutes per active mother per month, and modality
choice when video is available but not the default. That measurement settles the assumption
underneath all of it.

**Recommendation: adopt Option C in principle now, subject to Hector's feasibility answer,
and instrument the pilot to confirm the minutes.** Do not wait for the pilot to make the
decision — wait for the pilot to confirm it.
