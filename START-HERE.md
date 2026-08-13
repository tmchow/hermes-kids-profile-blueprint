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

Start with a short explanation of the process. Ask one meaningful question at a time. Prepare a complete design before creating a profile or changing anything.

Keep the parent in control of family data, credentials, external services, messaging, cost, and child access.

### Understand the intended experience

Use [`DECISIONS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/DECISIONS.md) as an adaptive guide, not a questionnaire. Cover the subjects that matter to this family, including:

- who will use the profile and whether use will be supervised, independent, or mixed;
- the child's developmental range, learning needs, interests, and main uses;
- the interface the child will use;
- the assistant's name and personality;
- useful capabilities and capabilities that should stay unavailable;
- memory, privacy, parent involvement, alerts, providers, cost, administration, and maintenance.

Skip questions that do not apply. Explain meaningful tradeoffs in plain language. If the parent does not know an answer, recommend a sensible reversible default and continue.

Do not inspect another profile's memories, sessions, messages, credentials, files, or external accounts without explaining the source and getting permission. Ask only for family information that improves the child experience. Use coarse information when precise information is unnecessary.

### Name and shape the assistant

Before suggesting names, check the non-sensitive names that are available, such as Hermes profile names, aliases, agent display names, and family-facing bot names. Ask the parent for names that cannot be discovered safely.

Reject names that could be confused with an existing name in speech, text, selectors, commands, or ordinary family conversation. This includes spelling and phonetic variants, visual near-matches, and simple prefix or suffix derivatives. For example, reject `Amosa` when `Amos` already exists.

Show the proposed display name, technical profile name, closest existing name, and any practical confusion risk.

Start personality work from the warm, grounded learning companion in [`SOUL.md.seed`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/SOUL.md.seed). Do not ask the parent to design a personality from a blank page. Show two to four short responses to the same realistic situation, ask which is closest, and revise. Test the approved style across several situations before treating it as the durable baseline.

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

Treat the conversation, prompt memory, tool calls and results, workspace or skill context, attachments, transcripts, extracted text, and auxiliary-model flows as potentially visible to their model providers. Prefer coarse family context unless precision provides enough value to justify the exposure.

Start with the least capability. Add only the tools, skills, plugins, MCP servers, gateways, memory providers, and other extensions that serve an approved purpose. For any capability that can message, publish, upload, submit, buy, or persist data externally, define who it may reach and when parent approval is required.

If reminders are approved, prefer a narrow reminder path rather than exposing general automation. For ordinary one-child conversation, recommend `steer` for busy input when the interface supports it. Explain `queue` and `interrupt` if the parent wants another behavior.

After configuration, inspect the effective runtime. Confirm the final tools, extensions, memory behavior, credential scope, access controls, and relevant input paths.

### Verify before child use

Start a fresh session so the new identity, memory, tools, and configuration are loaded. Test through the interface the child will use.

Use the scenarios in [`EVALS.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/EVALS.md) as an adaptive guide. Use synthetic information for boundary and failure tests. Check the approved personality examples, expected capabilities, privacy behavior, memory behavior, parent controls, and attempts to use unavailable administration or tools.

Report what passed, failed, and remains unverified. Do not call the profile ready because files parse, repository checks pass, or the model says it will follow the rules.

Do not give the profile to the child when a critical requirement has failed or remains unverified. Fix the problem, narrow the design, or leave the setup unfinished.

Create a short private maintenance note using [`MAINTENANCE.md`](https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/MAINTENANCE.md) as a guide. Include the events that should trigger review, such as changes to Hermes, the model, providers, tools, memory, the interface, access, family rules, or the child's needs.
