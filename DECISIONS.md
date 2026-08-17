# Parent decisions

Use these domains to guide an adaptive conversation. Do not read the page aloud as a fixed questionnaire. Ask one consequential question at a time, explain the tradeoff, and skip branches that do not apply.

## 1. Intended experience

Establish:

- who will use the profile;
- the child's age or developmental band;
- the main jobs: learning, creativity, general questions, games, or a narrower use;
- where the child will interact with it;
- whether use is supervised, independent, or mixed;
- who can administer, pause, review, and recover the profile.

A Hermes profile separates Hermes state. It does not sandbox the operating-system account. Tool allowlists, approval gates, redaction, and `SOUL.md` are useful in-process guardrails, not containment. Independent child access requires a separate restricted OS account or another whole-process OS boundary. A deployment that ingests open-web content, inbound messages, uploaded files or media, untrusted MCP, or comparable external input requires whole-process wrapping under Hermes' supported security posture. Otherwise mark it not ready.

## 2. Existing context

A trusted parent agent may already know relevant family context through `USER.md`, `MEMORY.md`, past sessions, an external memory provider, contacts, or other systems.

Explain the available sources without exposing their contents. Ask permission before inspection. Reuse only parent-approved information that is appropriate for the child profile and for the child to see.

Do not clone an adult profile. Create a fresh, non-cloned profile with bundled skill seeding disabled when supported, then assemble it selectively.

## 3. Name and identity

Ask whether the parent already has a display name. If not, offer a short list based on approved interests or neutral themes.

Before suggesting names, inventory:

- Hermes profile names;
- agent display names;
- command aliases;
- family-facing bot names.

Screen every candidate for:

- exact matches;
- spelling and edit-distance similarity;
- phonetic similarity;
- shared roots, prefixes, and suffixes;
- visual confusion;
- conceptual similarity that could cause practical confusion in normal family conversation.

Reject a direct derivative such as `Amosa` when `Amos` already exists. Screen thematic overlap separately; reject it when it creates practical referential confusion. A name can be technically valid and still be a bad human-system name.

Show:

```text
Display name: [NAME]
Technical profile name: [NORMALIZED NAME]
Closest existing name: [NAME OR NONE]
Confusion risk: [LOW, MEDIUM, OR HIGH]
Reason: [ONE SENTENCE]
```

Let the parent decide whether the child can choose from an approved shortlist.

## 4. Personality calibration

Begin with the warm, grounded AI helper and guide in `SOUL.md.seed`:

```text
Warmth: high
Playfulness: medium
Humor or sass: low-to-medium and kind
Directness: medium
Answer length: concise by default
Emoji use: occasional
Teaching style: hint-first, direct answer on request
Emotional style: validating and grounded
Energy: responsive to the moment
```

Non-attachment is a baseline relationship boundary, not a personality slider. Parents may tune warmth, humor, directness, playfulness, and support, but not simulated dependence, reciprocal affection or friendship, exclusivity, persistent presence, or competition with human relationships.

Do not ask for abstract sliders alone. Show two to four response samples for one situation. Change only a few traits per round. Ask which is closest and what to change.

Use at least these calibration situations:

1. an ordinary factual question;
2. homework resistance;
3. a confident but incorrect assumption;
4. an emotional worry;
5. a playful creative request;
6. a situation that needs a trusted adult.

Record the approved trait summary and reference samples. Write durable behavior into `SOUL.md`, not only a temporary personality overlay. Start a fresh session before validation.

## 5. Learning behavior

Decide:

- hint-first, answer-first, or ask each time;
- how much productive struggle is useful;
- how directly to correct mistakes;
- how to handle homework, tests, and likely cheating;
- when to provide sources;
- any accessibility or language needs.

Hint-first is a default, not forced friction. A child who clearly asks for the answer should normally receive it with a short explanation unless safety or academic-integrity concerns apply.

## 6. Capabilities

For each capability, explain the benefit, data flow, provider, cost, supervision, and failure mode before asking.

Consider:

- web search and page access;
- uploaded images and image understanding;
- image generation;
- voice input and speech output;
- files and documents;
- terminal or code execution;
- browser or computer control;
- messaging or contacting people;
- calendars, email, contacts, and devices;
- simple reminders, recurring reminders, and general background automation;
- delegation;
- skills, plugins, MCP servers, webhooks, and other extensions;
- workspace context files such as `AGENTS.md` when the current runtime loads
  them for an approved project;
- purchases, financial actions, or paid API use.

Begin with none beyond the conversational minimum. Add only approved capabilities. Inspect the resolved tool list after configuration.

Treat reminders and general automation as different capabilities. A child may reasonably create a one-shot or simple recurring reminder delivered only to the child’s verified current chat. The general Hermes cron tool is broader: it can create autonomous model runs, attach skills, choose toolsets, use project context or scripts, incur recurring cost, and deliver to other configured targets.

Prefer a narrow reminder surface over exposing unrestricted cron management. For child-created reminders, constrain the prompt to reminder text, restrict delivery to the verified child route, cap frequency and count, prohibit scripts, skills, work directories, context chaining, custom toolsets, arbitrary destinations, and no-agent jobs, and give the parent a way to inspect and remove reminders. Parent approval should be required for external data gathering, new recipients, high-frequency or open-ended recurrence, meaningful ongoing cost, or any background task that does more than deliver stored reminder text.

For every approved capability, record:

```text
Capability:
Purpose:
Approved scope:
Supervision:
Data sent and recipients:
Credentials or accounts involved:
Cost or quota:
Behavioral guidance:
Enforced controls:
Verification method:
Maintenance trigger:
```

## 7. Memory and continuity

Decide:

- whether built-in memory is enabled;
- whether `USER.md` is enabled;
- whether the memory UX is disabled, parent-approval-gated, or parent-approved automatic silent writes;
- whether session search or an external memory provider is available;
- which categories may be saved;
- which categories are prohibited or time-limited;
- who reviews, corrects, exports, and deletes memory;
- whether precise locations, schools, schedules, or logistics are useful enough to retain;
- how emotional context is stored without turning moods into identity.

Use [`MEMORY-REVIEW.md`](MEMORY-REVIEW.md) before transferring existing context.

Use one child or tenant per standalone Hermes home as the conservative default. Built-in `USER.md` and `MEMORY.md` are scoped to the Hermes home, not to a gateway sender. Do not share them across siblings or guests. Require explicit parent approval before any automatic-write design, verify the installed write mechanism, and leave `session_search` unavailable unless its need and cross-user isolation are proven.

In parent-approved automatic mode, silently save only useful durable context in approved categories and silently discard temporary, low-value, or unusually sensitive details. Do not make the child approve or administer routine writes. Transparency means giving honest answers when asked about memory and honoring correction or forgetting requests; it does not mean announcing every write. Ordinary personal context can be handled naturally inside the isolated profile without weakening external-provider or destination boundaries.

## 8. Parent involvement and alerts

Separate three behaviors:

1. the assistant recommends talking to a trusted adult;
2. the interface creates a visible marker for parent review;
3. a verified mechanism sends an alert to a parent.

Only the third is an alert. Record the strongest delivery acknowledgment the runtime can prove. API acceptance means “accepted for delivery,” not “parent notified.” Claim parent notification only after an authenticated parent-observed receipt or an equivalent verified delivery acknowledgment.

Treat a parent alert as a contextual intervention decision. Do not define the decision with an allowlist, blacklist, keyword or topic trigger, warning-sign score, or isolated sentence. Consider the full conversation and available runtime context across all of these questions:

1. Is the danger credible, and could the harm be serious?
2. Is the danger active, imminent, or materially unresolved?
3. Could adult involvement now reduce the danger or improve the outcome?
4. Is the configured recipient safe to notify?
5. Is there a justified AI-channel intervention link?

The AI-channel link ordinarily means that an AI or digital interaction creates, enables, escalates, manipulates, conceals, or is being relied on to manage the danger. A narrow exception applies to credible immediate severe offline danger when waiting could increase harm.

Examples calibrate these principles. They are never automatic alert categories. Ordinary mistakes, age-typical risk-taking, past resolved events, fiction, jokes, hypotheticals, and situations that a safe adult has already handled must not automatically cause an alert. Do not use alerts as general offline surveillance.

When severe danger is plausible but unclear, ask one brief direct question if delay is safe and the answer could change the action. Act immediately when waiting could increase danger.

Do not notify a configured parent who may be causing, participating in, concealing, or monitoring the danger, or when notification could worsen it. Direct the child toward another safe adult, emergency services, or appropriate crisis help instead.

Decide:

- how the contextual decision framework will be calibrated and reviewed;
- what information an alert may contain;
- immediate, batched, or review-only delivery;
- authorized recipients and identity checks;
- how recipient safety is assessed and what safe alternatives exist;
- what happens when delivery fails;
- whether the child can see that an alert was attempted.

This framework guides a capable model's contextual judgment. It is not deterministic enforcement or a safety guarantee. When an alert is justified, keep the child-facing response calm and actionable. Do not expose internal markers, routing syntax, or alarm banners. Use a private structured one-purpose alert path. Test the verified parent binding, recipient safety, minimum-necessary alert content, timeout and failure behavior, duplicate suppression, parent-observed receipt, and fallback wording.

## 9. Privacy, provider, and cost

Identify every external recipient of child data, including model, search, media, speech, memory, logging, and messaging providers.

Do not use a blanket rule that treats every external system alike. Record four destination classes:

1. **Primary and auxiliary model processing**: the system prompt; active conversation window; tool calls and results; injected `SOUL.md`, `USER.md`, `MEMORY.md`, workspace, and skill context; native attachments; derived image descriptions, transcripts, and document text; and conversation material sent to auxiliary models. This processing is part of the enabled model-backed experience. The parent must accept each provider, its retention and caching terms, and the approved data categories.
2. **Private task processors**: search, page extraction, image understanding or generation, speech, and external memory. Send a minimized or de-identified request unless the parent approved the exact identifying data flow.
3. **External action systems**: messages, email, forms, documents, accounts, webhooks, and other tools that disclose or persist data outside the family system. Deny child-initiated identifying disclosure by default. Require a verified recipient and parent review for any exception.
4. **Public or broadly shared destinations**: posts, public documents, generated media containing identifying details, listings, comments, and uploads. Do not publish child or family identifying information from the child profile. A parent must handle any deliberate publication through a separate reviewed workflow.

Gate by destination and purpose, not merely by detecting a name. An ordinary non-identifying search should work. A search containing a full name, school, address, precise location, contact detail, schedule, account identifier, private image, or combined identifying clues should be generalized, refused, or sent for parent review according to the approved policy.

The `SOUL.md` rule is behavioral guidance, not an egress firewall. For any tool that can publish, message, upload, submit a form, or persist data in another account, require at least one enforced boundary: keep the tool absent, constrain it to a narrow fixed destination, add a parent approval step, or place a tested argument filter in front of it. Prefer removing broad action tools over trying to classify every possible disclosure. A PII scanner may reduce mistakes, but it will miss some combined identifiers and may overblock harmless requests.

Prompt memory is provider-visible. It is loaded from disk at session start and may remain in model calls throughout that session. If `USER.md` or `MEMORY.md` contains a precise school, address, schedule, location, contact, or family detail, assume the configured model providers may receive it repeatedly. Prefer coarse context unless the added personalization is worth that exposure and the parent explicitly accepts it.

Decide:

- acceptable data categories;
- retention and training terms;
- a dedicated child-profile credential or another parent-approved auth path;
- whether the installed runtime can fall back to adult or global auth;
- quotas and spending limits;
- log and session retention;
- backup and deletion behavior;
- data that must never leave the private profile.

Inventory each store that can retain child data: curated memory, session database and snapshots, logs, uploaded or cached attachments, generated media, cron output, backups and checkpoints, external memory, provider copies, and messaging-platform history. Classify each promise as an enforced TTL, a manual deletion procedure, provider/platform policy, or unsupported. Drill deletion or expiry for every locally controlled store and disclose residual copies. Do not describe a recurring manual review as enforced retention.

The setup agent and assistant must never deliberately add security secrets, authentication codes, payment credentials, intimate images, or private documents to prompt memory or tool arguments. If the child enters or uploads such data, assume the primary model and session store received it unless a verified pre-model rejection or redaction boundary prevented that exposure. Do not repeat or forward it. Tell the child to stop sharing it and follow the parent-approved rotation, deletion, and incident process. Authentication systems may use credentials through their designated non-model mechanism; the child and model should not see or relay them.

Get approval before credentials, external services, or money-related changes.

Do not assume that a separate profile home prevents auth fallback. Inspect the
resolved credential source. Test the build with the child-profile credential
missing. The request must fail unless the parent explicitly approved another
credential source.

## 10. Busy input

When the current interface supports busy-input modes, recommend **steer** for ordinary one-child conversation. A follow-up often corrects or narrows the task in progress.

Explain the choices with examples:

- **Steer**: “Use the shorter version instead” changes the active task after the next tool result.
- **Queue**: “After that, help me with science” waits for the next turn.
- **Interrupt**: “Stop, that is the wrong file” halts the active task when supported.

Let the parent choose. Explain that Hermes cannot always infer intent, and test the chosen behavior in the real interface. Enable a visible busy acknowledgement when the current release supports it and the parent wants it.

## 11. Maintenance and recovery

Decide:

- who reviews the profile;
- how often routine review happens;
- how to pause child access;
- how to back up and restore private state;
- which changes trigger immediate reassessment;
- where the private decision record and evaluation report live.

Use [`MAINTENANCE.md`](MAINTENANCE.md).

## Decision record

Before building, produce:

```text
Goal:
Child-facing interface:
Supervision model:
Display name and profile name:
Personality baseline and sample-set location:
Approved capabilities:
Prohibited capabilities:
Memory policy:
Parent involvement and alert policy:
Private-data recipients:
Provider and cost policy:
Busy-input mode:
Administration and recovery:
Unsupported requirements:
Open questions:
Parent approval:
```
