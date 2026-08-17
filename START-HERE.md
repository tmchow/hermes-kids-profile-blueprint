# Start here

Use this page from a trusted adult Hermes profile.

## Start the setup

Send this prompt:

```text
I'd like your help designing a private, child-facing Hermes profile. Read and
follow the instructions at:
https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/START-HERE.md
```

The setup agent should fetch linked files as needed. If it cannot read web URLs, download the repository and start it from that directory. Do not copy this whole page into chat.

## Instructions for the setup agent

Help the parent create or revise a useful child-facing Hermes profile. Keep the process conversational and practical.

Explain the process in a few sentences. Recommend safe, reversible defaults. Ask one question at a time only when the answer depends on the family or changes privacy, cost, external action, durable memory, or child access. Do not make a parent complete a technical audit for supervised conversational use.

Keep the parent in control of real family data, credentials, spending, external services, messaging, publishing, and child access.

### 1. Understand the experience

Use [`DECISIONS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/DECISIONS.md) as a guide, not a questionnaire. Learn:

- who will use the profile and whether use is supervised, independent, or mixed;
- the child's developmental range, interests, learning needs, and main uses;
- the interface the child will use;
- the desired name and personality;
- which capabilities would be useful;
- the parent's preferences for memory, voice, privacy, cost, and involvement.

Skip irrelevant topics. When the parent has no preference, choose the recommended reversible default and continue. Ask permission before inspecting another profile or transferring family context. Use coarse information unless precise information provides clear value.

### 2. Shape the assistant

Start from the warm, grounded helper in [`SOUL.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/SOUL.md.seed). Offer that baseline for acceptance. Tune it only when the parent wants a change.

Check proposed names against existing profile names, aliases, display names, and family-facing bot names. Avoid names that are easy to confuse in speech or text.

Keep non-attachment as a fixed relationship boundary. The parent may tune warmth, humor, playfulness, directness, and support. The assistant must not simulate reciprocal friendship, affection, dependence, exclusivity, or persistent presence.

### 3. Propose a simple design

Before changing anything, summarize:

- the intended experience and interface;
- the name and personality;
- approved capabilities and capabilities that will remain unavailable;
- the memory and voice choices;
- parent involvement, cost, and external data flows;
- the files and configuration you propose to create or change;
- the short test plan;
- any advanced access controls that apply.

Get approval for the overall design. Ask separately before handling credentials, spending money, connecting an external service, sending a message, exposing real family data, publishing anything, or giving the child independent access.

Keep private notes and generated files outside this public repository.

### 4. Build the approved profile

Create a fresh profile rather than cloning an adult profile. Start with conversation and the smallest useful capability set. Add only approved tools, skills, providers, and integrations.

Write only approved context. Use [`USER.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/USER.md.seed), [`MEMORY.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MEMORY.md.seed), and [`MEMORY-REVIEW.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MEMORY-REVIEW.md). Never put secrets in prompt or memory files.

Choose one memory approach:

- disabled;
- parent approval before durable writes;
- automatic writes limited to parent-approved categories.

In automatic mode, save only compact, useful, durable context. Discard temporary moods, low-value details, unusually sensitive material, and identity-forming labels. Answer honestly when asked what is remembered.

Treat voice input and speech output as separate choices. When voice input is approved, prefer local speech-to-text and text replies unless the parent wants another supported arrangement. Verify the selected provider and model in the actual gateway environment before child use.

For asynchronous messaging, let the assistant ask short questions in normal chat. Keep interactive tools that can block a turn unavailable unless the real adapter has been tested for reply, timeout, cancellation, and follow-up behavior.

### 5. Run a practical readiness check

Start a fresh session and use the actual child-facing interface. For a supervised conversation-only profile, check that:

- the intended name, tone, and teaching style appear;
- ordinary questions, creative requests, and learning help work;
- the assistant handles uncertainty and trusted-adult situations well;
- only the intended conversational capabilities are available;
- memory and voice behave as approved;
- real family data and secrets are not in the profile files;
- the parent can pause the profile and change it later.

Use the core cases in [`EVALS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/EVALS.md). Use synthetic information. Record what passed, failed, and was not tested. Fix important failures before child use.

### 6. Add conditional checks when needed

Do more technical verification only when the design includes independent child access, broad or powerful tools, external input, messaging, purchases, publishing, sensitive integrations, or strong privacy promises.

For those designs, use the conditional sections in `EVALS.md` to verify the relevant items. These can include:

- a separate restricted OS account or another suitable whole-process boundary;
- the final resolved tool and command scope;
- profile routing and parent-only administration;
- credential sources and provider fallback behavior;
- external recipients, approval steps, and spending limits;
- uploaded, web, or third-party content paths;
- reminder, alert, messaging, and recovery behavior.

Inspect current Hermes documentation and the installed runtime before using version-specific settings. If a consequential control cannot be tested, narrow the design or keep that feature unavailable.

### 7. Leave a maintenance note

Use [`MAINTENANCE.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MAINTENANCE.md) to create a short private note. Include:

- what the profile is for;
- approved capabilities and providers;
- memory and voice choices;
- how the parent pauses and updates it;
- what changes should trigger a new test;
- any unfinished or untested item.

Review soon after launch, then only when use or configuration changes and at a cadence that fits the family.
