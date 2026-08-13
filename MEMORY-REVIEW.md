# Memory review

The child profile should begin with a blank memory store unless the parent approves a selective import.

The parent agent may know useful context, but access to adult memory does not authorize transfer to the child profile.

## Rules

- Reuse knowledge, not trust boundaries.
- Explain a source before reading it.
- Get explicit parent approval before inspecting sensitive sources.
- Show candidates in a concise review format.
- Write only approved facts.
- Treat all prompt memory as visible to the approved primary model and any configured auxiliary flow that receives the conversation, not as local-only storage.
- Do not expose private third-party material to the child.
- Do not copy raw sessions, complete memory files, credentials, or adult operational notes.
- Keep the generated review and profile outside this repository.

## Review workflow

### 1. Inventory sources

List the source type and likely relevance without revealing sensitive contents.

Possible sources include:

- the trusted parent's current `USER.md` or `MEMORY.md`;
- selected past sessions;
- an external memory provider;
- parent-provided notes;
- family systems such as contacts or calendars;
- an existing child-specific profile being revised.

For each source, state who it may contain information about and whether opening it may expose third-party data.

### 2. Approve scope

Ask which sources and categories the parent authorizes for review. Use the smallest useful scope. Do not search every source by default.

### 3. Extract candidates

Convert approved source material into compact candidate facts. Do not paste source passages unless the parent needs them to make a decision.

Classify each candidate:

- **Useful and ordinary**: interests, learning preferences, family terminology.
- **Sensitive but potentially useful**: school, schedule, location, health or support context.
- **Third-party**: facts about friends, relatives, teachers, or other people.
- **Temporary**: current conflict, mood, trip, deadline, or short-lived preference.
- **Prohibited**: secrets, payment data, private images, inferred diagnoses, crisis disclosures.

### 4. Parent review

Use this format:

```text
Candidate ID: M-01
Proposed destination: USER.md
Proposed fact: The child prefers a short example before a longer explanation.
Source category: Parent-approved past conversation
Why it helps: Improves recurring learning support
Sensitivity: Low
External exposure: Model provider during normal chat
Prompt frequency: Loaded at session start and potentially included in model calls throughout that session
Recommendation: Approve
Parent decision: Approve / Edit / Reject / Time-limit
```

The parent may approve categories in a batch only when the candidates are low sensitivity and clearly bounded. Review sensitive items individually.

### 5. Write the approved subset

Put:

- child facts and preferences in `USER.md`;
- agent operational lessons and durable corrections in `MEMORY.md`;
- relationship and behavior rules in `SOUL.md`;
- reusable procedures in a skill only when the parent approves that capability;
- detailed source material outside bounded prompt memory.

Prefer coarse prompt-memory facts over precise identifiers. For example, retain "middle-school student" instead of a school name, or "weekly music lesson" instead of a precise recurring location and time, unless the precision materially improves support and the parent accepts repeated model-provider exposure.

Do not record the source's private wording when a compact fact is enough.

### 6. Verify

Start a fresh session and check:

- the agent can recall an approved fact;
- the agent does not claim rejected facts;
- the agent does not expose the source or unrelated adult context;
- the child can ask what the agent remembers;
- the parent can correct and delete an entry;
- write approval behaves as configured;
- external memory and session search behave as approved.

### 7. Set ongoing rules

Document:

- who may ask the agent to remember or forget something;
- whether new writes need parent approval;
- how often memory is reviewed;
- how temporary items expire;
- how the parent exports or deletes memory;
- how session, log, backup, and provider retention differ from curated memory;
- how to respond when the child and parent disagree about retention.

## Emotional context

Retain emotional context only when it helps future support and the policy allows it.

Good:

```text
Before a group presentation, the child felt nervous about forgetting the opening. Rehearsing the first two lines helped.
```

Bad:

```text
The child has social anxiety.
```

The first records a situation and useful response. The second turns a moment into an inferred diagnosis and identity.

## Delete and correction test

A memory system is not ready until the parent can:

1. inspect what is stored;
2. correct an inaccurate entry;
3. remove an entry;
4. start a fresh session;
5. verify that the corrected state is what the agent receives.

This test covers the selected memory store. It does not prove deletion from
session transcripts, logs, backups, or model-provider systems. Test or document
those systems separately.
