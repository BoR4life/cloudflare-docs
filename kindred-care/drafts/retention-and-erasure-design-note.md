# Retention, disposal and erasure — design note for Hector

**30 Aug 2026.** Architectural, and **the cost of delay compounds daily** — which is why it
sits alongside D-23 and the endpoint check rather than in the compliance backlog.

## The problem in one line

**Retrofitting a right to erasure into a 16-month persistent conversational thread is a
rebuild, not a feature.** Every week of building without it makes it more expensive.

## Why now rather than later

Three forces, all pointing the same way:

1. **Privacy Act Tranche 2** proposes a **right to erasure**, an expanded definition of
   personal information, and a **"fair and reasonable" test applying regardless of consent.**
   Confirmed by the Attorney-General in February 2026 as being progressed — no bill, no
   timetable. So: not law yet, and coming.
2. **A health service will ask now**, whatever the Commonwealth position. Health Records Act
   2001 (Vic) and Information Privacy Act 2009 (Qld) both engage retention and access, and a
   procurement questionnaire will ask what the retention schedule is. There isn't one.
3. **The interface doctrine makes it harder.** The persistent single thread across 16 months
   is the right retention mechanism and the hardest possible erasure target. The two design
   goals are in direct tension and that tension should be designed for, not discovered.

## The hard cases

Erasure in a conversational health system is not a delete statement. Six cases that need a
ruling before they need code:

1. **Partial erasure.** She wants one disclosure removed, not the thread. Is the thread
   addressable at turn level, and does removing a turn corrupt the conversational context the
   rest depends on?
2. **Derived state.** The agent's memory, retrieval indices, embeddings, cached summaries.
   **An embedding derived from erased text is arguably still her personal information.** What
   is the position?
3. **The safety record.** A T3 escalation is a clinical event the health service may be
   obliged to retain, and she may want erased. **These obligations conflict** and the answer
   is almost certainly that safety records are retained under a stated exception — but it
   must be stated, in the transparency statement, before she consents.
4. **Analytics.** ADR-008 already forbids free text in the analytics store, which helps
   enormously. Confirm that k-anonymised aggregates are genuinely non-identifying at the
   cohort sizes involved — **at 150 mothers, k-anonymity is doing more work than at 15,000.**
5. **Backups.** Erasure that leaves the record in backups for 90 days is a position, not a
   failure — but it is a position that must be documented and told to her.
6. **Tenant exit.** A health service ends its contract. What happens to the mothers' threads?
   She is enrolled by the service but the conversation is hers. **This is unresolved and it
   will appear in the first pilot agreement.**

## What to design in now

| # | Capability | Why now |
|---|---|---|
| 1 | **Turn-level addressability** — every turn individually identifiable and deletable | Retrofitting identity onto stored turns is the expensive part. Cheap if the schema carries it from the start |
| 2 | **Derivation lineage** — record what was derived from what | Without it, erasure cannot follow the data into embeddings and caches |
| 3 | **Retention class per data type** | Conversation, safety record, telemetry, enrolment record and consent record almost certainly have different retention periods and different legal bases |
| 4 | **Tombstoning rather than hard delete** | Preserves referential integrity and provides an audit trail proving erasure occurred — which a regulator will want |
| 5 | **Tenant-exit data path** | Will be in the first pilot agreement, so it needs an answer before that agreement is drafted |

## What is needed, and from whom

**From Hector:** feasibility and build cost for items 1 and 2, which are the architectural
ones. Items 3–5 are policy decisions that then need implementing.

**From Brad, with legal input:** the retention schedule itself, and the ruling on hard case 3
— safety records versus erasure. That is a legal question, not an engineering one, and it
must be settled before the transparency statement is written, because she must know before
she consents.

**Sequence:** the schedule and the rulings first, the build second. Building erasure before
deciding what is retained produces the wrong erasure.

## The cheap win available now

**Item 1 alone — turn-level addressability — is most of the value.** If every turn is
individually identifiable from the start, almost every erasure scenario becomes tractable
later. If it is not, they all become migrations.

**Ask Hector whether the schema already carries this.** Given the build quality elsewhere it
may well. If so, this note is largely closed and that is worth knowing today.
