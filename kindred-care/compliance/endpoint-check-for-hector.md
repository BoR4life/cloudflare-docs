# Vertex endpoint check — for Hector, this week

**30 Aug 2026.** Free, binary, and it either confirms a claim the pack is already making or
destroys it. Highest priority item in the compliance stack because everything else depends
on the answer.

## The claim being made

Kindred Care documents state processing runs in **australia-southeast1 (Sydney)**. Data at
rest almost certainly does. **Model inference may not.**

## The defect class

Google's own guidance is to **avoid the global endpoint where data cannot leave a
continent**, and to pin a regional endpoint explicitly. There is a known behaviour in which
Vertex AI **ignores `GOOGLE_CLOUD_LOCATION` and falls through to the global endpoint** —
reported against API-key auth ([gemini-cli #27984](https://github.com/google-gemini/gemini-cli/issues/27984)).

If that is happening in `bor-iridia`, **mothers' conversations are being processed outside
Australia and nobody knows.** It fails silently: no error, no log line, correct responses.

## What to check

1. **Is the endpoint pinned regionally?** Confirm the client is constructed against
   `australia-southeast1-aiplatform.googleapis.com`, not the global endpoint, and not
   relying on an environment variable alone to get there.
2. **Which auth path is in use?** API key vs service-account / ADC. The reported defect is
   associated with API-key auth.
3. **Same question for Vertex AI Search**, not only for generation. RAG queries carry
   conversation-derived text.
4. **Prove it rather than read it.** Confirm from the request path or from Cloud Logging
   which regional endpoint was actually hit on a live turn — the same evidence standard the
   build already holds itself to. A config value that says Sydney is documentation; a logged
   regional endpoint on a real turn is evidence.

## If it is wrong

Not a crisis — it is a configuration fix and a short remediation note. It becomes a crisis
only if it is discovered by a health service's security assessor after we have asserted
onshore processing in writing. **Fix it before the claim is made, not after.**

## The related finding, whichever way this goes

**Google's formal AI/ML data residency (DRZ) commitment is offered only in US and EU
locations.** ML processing is *supported* in australia-southeast1, but there is **no
contractual data-residency guarantee for the ML layer in Australia**
([data residency docs](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)).

That gap exists even with the endpoint pinned correctly. It is disclosable and manageable —
but it must be **disclosed by us in the first procurement conversation**, with the
mitigations stated, rather than found by their assessor.
