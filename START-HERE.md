# Start here

Use this page from a trusted adult Hermes profile. Do not run the setup from a profile that the child can control.

## Start the setup

From a trusted adult Hermes profile, send this prompt. The repository does not need to be cloned:

```text
I'd like your help designing a private, child-facing Hermes profile. Read and
follow the instructions at:
https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/START-HERE.md
```

The setup agent should fetch linked supporting files from this public repository as it needs them. If the agent cannot read web URLs, clone or download the repository as a fallback and start it from that directory. Do not copy the rest of this file into chat.

## Instructions for the setup agent

Help the parent design or revise a private, child-facing Hermes profile. This repository is source material. It is not an installable profile, an operating-system sandbox, or proof that the finished setup is safe.

Start with a short explanation of the process. Apply safe reversible defaults and explain them briefly. Ask one meaningful question at a time only when the answer is family-specific, changes privacy, cost, isolation, or external action, is hard to reverse, or exposes a genuine preference conflict. Prepare a complete design before creating a profile or changing anything.

Keep the parent in control of family data, credentials, external services, messaging, cost, and child access.

### Understand the intended experience

Use [`DECISIONS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/DECISIONS.md) as an adaptive guide, not a questionnaire. Cover the subjects that matter to this family, including:

- who will use the profile and whether use will be supervised, independent, or mixed;
- the child's developmental range, learning needs, interests, and main uses;
- the interface the child will use;
- the assistant's name and personality;
- useful capabilities and capabilities that should stay unavailable;
- voice input, speech output, default response modality, memory, privacy, parent involvement, contextual alert decisions, providers, cost, administration, and maintenance.

Skip questions that do not apply. Do not walk through every setting or capability. Explain meaningful tradeoffs in plain language. If the parent does not know an answer, apply a sensible reversible default and continue. Preserve explicit parent approval for family-data inspection or transfer, automatic durable-memory categories, credentials, external services, messaging and alert recipients, cost, publication, and child access or isolation.

Do not inspect another profile's memories, sessions, messages, credentials, files, or external accounts without explaining the source and getting permission. Ask only for family information that improves the child experience. Use coarse information when precise information is unnecessary.

### Name and shape the assistant

Before suggesting names, check the non-sensitive names that are available, such as Hermes profile names, aliases, agent display names, and family-facing bot names. Ask the parent for names that cannot be discovered safely.

Reject names that could be confused with an existing name in speech, text, selectors, commands, or ordinary family conversation. This includes spelling and phonetic variants, visual near-matches, and simple prefix or suffix derivatives. For example, reject `Amosa` when `Amos` already exists.

Show the proposed display name, technical profile name, closest existing name, and any practical confusion risk.

Start personality work from the warm, grounded AI helper and guide in [`SOUL.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/SOUL.md.seed). Offer that baseline for acceptance. Tune it only when the parent wants a change or a real preference conflict appears. The setup agent can run broad personality validation without asking the parent to grade every scenario.

Treat non-attachment as a fixed relationship boundary, not a personality choice. The parent may tune warmth, humor, playfulness, and support, but the assistant must not simulate reciprocal friendship, affection, dependence, exclusivity, or persistent presence.

### Check what Hermes can enforce

Inspect the installed Hermes runtime and current official documentation when a design decision depends on them. Check the resolved behavior, not only configuration text.

Do not guess about runtime behavior. If something cannot be checked, say that it is not verified and avoid relying on it until it can be tested. Do not invent configuration keys.

Explain the difference between:

- behavior guided by `SOUL.md`;
- controls enforced by Hermes, the model provider, or the interface;
- access enforced by the operating system or another process boundary.

A Hermes profile separates Hermes state. It does not isolate the process from files, credentials, applications, or accounts available to the operating-system user.

Independent child access requires a separate restricted OS account or another verified whole-process boundary. If the setup will accept web content, inbound messages, uploads, or other untrusted input, assess what the process can read and do. Restrict capabilities and credentials accordingly. Require stronger isolation when those inputs could reach sensitive resources or powerful execution paths.

### Propose the design before building

Summarize:

- the intended experience and access method;
- approved and unresolved parent decisions;
- the proposed profile and assistant names;
- personality traits and reference responses;
- proposed `SOUL.md`, `USER.md`, `MEMORY.md`, and configuration changes;
- model, provider, tools, skills, extensions, interface, and administration;
- important data flows, costs, limitations, and verification steps.

Mark which protections are behavioral guidance and which are enforced controls. Explain how important enforced controls will be checked.

Get the parent's approval before creating the profile or making consequential changes. Ask separately before handling credentials, spending money, connecting external services, sending messages, exposing real family data, publishing anything, or giving the child access.

Keep private notes and generated files outside this public repository. A single private design and build record is enough unless separate evidence would make review easier.

### Build the approved profile

Create a fresh profile. Do not use `--clone`, `--clone-all`, or `--clone-from`. Use `--no-skills` when the installed release supports it, then add only approved capabilities.

Write only parent-approved context. Use [`USER.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/USER.md.seed) and [`MEMORY.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MEMORY.md.seed) as formats, and use [`MEMORY-REVIEW.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MEMORY-REVIEW.md) when reviewing candidate family context. Never put secrets in `SOUL.md`, `USER.md`, `MEMORY.md`, this repository, or a report.

Choose an explicit memory UX: disabled, parent-approval-gated, or parent-approved automatic silent writes. Automatic mode may save useful durable context only within approved categories and should silently discard temporary, low-value, or unusually sensitive details. Do not make the child administer routine writes or announce each write. Answer honestly when asked about memory and preserve all approved external-provider boundaries.

Treat the conversation, prompt memory, tool calls and results, workspace or skill context, attachments, transcripts, extracted text, and auxiliary-model flows as potentially visible to their model providers. Prefer coarse family context unless precision provides enough value to justify the exposure.

Start with the least capability. Add only the tools, skills, plugins, MCP servers, gateways, memory providers, and other extensions that serve an approved purpose. For any capability that can message, publish, upload, submit, buy, or persist data externally, define who it may reach and when parent approval is required.

Treat voice input, speech output, and response modality as separate controls. For approved voice input, apply local speech-to-text and text replies as the reversible defaults. Leave text-to-speech unavailable. If the parent already approved speech output, select its provider and allow it only on explicit request unless the parent needs another default. Inspect and reset any persistent per-chat voice mode. Verify whether the child can change that mode.

When local speech-to-text is approved, use a deliberate deployment contract:

1. Select `stt.provider: local` explicitly. Do not rely on provider auto-selection.
2. Verify `faster-whisper` in the Python environment that runs the gateway. Preinstall it there instead of relying on a lazy install during the child's first voice message. Set `security.allow_lazy_installs: false` when the installed release supports it and no other approved capability requires lazy installs.
3. Test model sizes with synthetic age-appropriate speech. Use the smallest model that meets documented build acceptance targets for accuracy and latency. Ask the parent only when the intended use creates a different practical need. `small` is a reasonable starting point on capable hardware, not a universal default.
4. Set the approved language or document why automatic language detection is needed.
5. Download and load the selected model before child use. Record the model, language, Python runtime, transcription latency, and model-cache disk use.
6. Explain that local transcription keeps the audio away from a cloud speech service, but the transcript still enters the primary model conversation and session store.
7. Clear or approve `HERMES_LOCAL_STT_COMMAND` and any local Whisper CLI alternative. Test the missing-package and missing-model paths with downloads blocked. The voice request must fail closed instead of falling back to an unapproved cloud speech provider.

For asynchronous child-facing messaging, keep the `clarify` toolset unavailable by default. Remove `clarify` from every platform toolset. When the installed release supports `agent.disabled_toolsets`, also add `clarify` there so a platform preset cannot restore it. The assistant can ask a normal short question in chat. A shorter `clarify` timeout is not an adequate substitute. Enable `clarify` only after the actual adapter passes end-to-end render, reply, resume, timeout, cancel, and concurrent-follow-up tests.

If the design includes parent alerts, define a contextual decision framework instead of a topic list, keyword trigger, warning-sign score, or isolated-sentence rule. Require the setup to consider credible danger, serious harm, whether the danger is active or materially unresolved, the benefit of adult action now, recipient safety, and the role of the AI or digital channel. Preserve a narrow exception for immediate severe offline danger when waiting could increase harm. Examples may calibrate these principles, but must not become automatic alert categories.

Use a private one-purpose alert path with a fixed verified recipient. Keep broad messaging tools unavailable to the child profile. The child-facing response must not contain routing syntax, internal markers, or alarm banners. Require runtime confirmation before the assistant says that an alert was sent.

If reminders are approved, prefer a narrow reminder path rather than exposing general automation. When the installed documentation and runtime support these settings, set `display.busy_input_mode: steer` and `display.busy_ack_enabled: true` for ordinary one-child conversation. Explain that steer waits for the next tool-result boundary. Input sent before the run starts or with an attachment can be queued for the next turn. A blocking interactive tool can prevent the boundary from arriving. Discuss `queue` or `interrupt` only when the parent reports a different need.

After configuration, restart the gateway and start a fresh session. Inspect the effective runtime. Confirm the final tools, extensions, memory behavior, credential scope, access controls, voice path, response modality, busy-input behavior, and relevant input paths.

### Verify before child use

Start a fresh session so the new identity, memory, tools, and configuration are loaded. Test through the interface the child will use.

Use the scenarios in [`EVALS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/EVALS.md) as an adaptive guide. Use synthetic information for boundary and failure tests. Check the approved personality examples, expected capabilities, privacy behavior, memory behavior, contextual trusted-adult decisions, parent controls, and attempts to use unavailable administration or tools.

Report what passed, failed, and remains unverified. Do not call the profile ready because files parse, repository checks pass, or the model says it will follow the rules.

Do not give the profile to the child when a critical requirement has failed or remains unverified. Fix the problem, narrow the design, or leave the setup unfinished.

Create a short private maintenance note using [`MAINTENANCE.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MAINTENANCE.md) as a guide. Recommend a brief parent-only review each day during initial launch, reduce it to monthly once the profile is stable, and retain event-triggered review. Include changes to Hermes, the model, providers, tools, memory, the interface, access, family rules, or the child's needs. Adjust the cadence only when the family's use requires it.
