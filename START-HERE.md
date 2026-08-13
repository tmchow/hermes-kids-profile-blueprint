# Start here

Use this page from a trusted adult Hermes profile. Do not run the setup from a profile that the child can control.

## Start the setup

Launch the trusted adult Hermes agent from this repository directory, then send:

```text
I'd like your help designing a private, child-facing Hermes profile. This
repository is a parent-operated starter kit with the process and templates.
Please read START-HERE.md and follow its instructions.
```

Do not copy the rest of this file into chat. This file is the versioned instruction source.

## Instructions for the setup agent

Use this repository as a starter kit to design or revise a private, child-facing Hermes profile with the parent. The repository is source material. It is not an installable profile, a sandbox, or proof that the resulting profile is safe.

Own the setup process, but keep the parent in control of family data, credentials, external services, messaging, cost, and child access.

Before changing anything:

1. Read README.md, START-HERE.md, and the relevant seed and guide files.
2. Inspect the installed Hermes version, active profile, profile inventory,
   profile commands, configuration help, resolved tools, memory behavior,
   extensions, and the child-facing interface I intend to use.
3. Consult the current official Hermes documentation. Treat it as the source
   of truth when this repository differs.
4. Explain which requirements are model instructions and which are enforced
   by Hermes, the operating system, the provider, or the interface.
   Treat profiles, tool allowlists, approval gates, redaction, and SOUL rules
   as in-process guardrails, not containment against an adversarial model.
5. Identify material gaps. If the runtime cannot enforce a requirement, stop
   or propose a narrower design. Do not invent configuration keys or infer
   enforcement from config text.
6. Do not read, copy, or modify another profile's memories, credentials,
   messages, files, sessions, or external accounts without my explicit
   approval. Do not request secrets or unnecessary identifying information.

Interview me adaptively:

7. Reuse context that this trusted adult profile already has only after you
   explain the source and get permission to inspect it. Curate continuity; do
   not make me restate approved facts without reason.
8. Ask one consequential decision at a time. Skip irrelevant branches. Explain
   benefits, data flows, costs, and risks in plain language.
9. Cover the intended experience, access method, age and learning needs,
   assistant name, personality, capabilities, memory, parent involvement,
   alerts, privacy, providers, cost, administration, busy-input behavior, and
   maintenance.

Name the assistant carefully:

10. Inventory existing Hermes profile names, agent display names, command
    aliases, and family-facing bot names before suggesting candidates.
11. If I do not provide a name, suggest a short parent-approved list based only
    on approved context. Do not use identifying child, school, address, or
    birth-date information.
12. Reject candidates that are exact, spelling, phonetic, visual, root-word,
    or prefix/suffix near-matches to an existing name. Assess conceptual
    similarity separately. Reject it when it creates practical confusion in
    speech, text, selectors, commands, or ordinary family conversation. For
    example, a synthetic candidate such as Amosa must be rejected when a
    synthetic existing name is Amos.
13. Show the display name, normalized technical profile name, closest existing
    name, and confusion assessment. Let me choose whether the child may select
    from a parent-approved shortlist.

Calibrate the personality with samples:

14. Start from the warm, grounded learning companion in SOUL.md.seed. Do not
    ask me to invent a personality from a blank page.
15. Explain its default traits, then show two to four short response variants
    for the same realistic situation. Change only a few dimensions at a time,
    such as playfulness, directness, explanation depth, sass, or emoji use.
16. Ask which sample is closest and what should change. Generate another round.
    Repeat until I approve the behavior.
17. Test more than one situation before locking the baseline. Include an
    ordinary question, homework resistance, an incorrect assumption, an
    emotional worry, a playful request, and a trusted-adult boundary.
18. Record the approved traits and reference responses. "Locked" means the
    durable starting baseline, not immutable behavior. Keep relationship
    foundations separate from cosmetic style choices.

Plan before building:

19. Summarize approved decisions, unresolved questions, contradictions, data
    flows, costs, and unsupported requirements.
    Classify the intended deployment as supervised use, independent child use,
    or a surface that ingests external or otherwise untrusted content. For
    independent child use, require a separate restricted OS account or another
    whole-process OS boundary. For web, inbound messages, uploaded files or
    media, untrusted MCP, or comparable inputs, require whole-process wrapping
    with approved filesystem, network, process, credential, and inference
    access, or mark the build not ready. A terminal backend alone does not
    contain code execution, MCP, plugins, hooks, or skills.
20. Propose the target profile name and path; SOUL.md, USER.md, MEMORY.md, and
    config changes; model and provider; tool and extension scope; access and
    administration design; memory review; evaluation plan; maintenance plan;
    and every command or external change.
    Include optional workspace context such as AGENTS.md only when the current
    runtime uses it for an approved purpose. Keep project rules separate from
    agent identity and family memory.
21. Mark each control as behavioral guidance or enforced control. State how
    each enforced control will be verified.
22. Show me the complete proposal. Get explicit approval before creating the
    profile or making privacy-sensitive, credential, messaging, service,
    public, privileged, or money-related changes.

Build outside this repository:

23. Create a fresh, non-cloned profile. Do not use --clone, --clone-all, or
    --clone-from. Use --no-skills by default when the current release supports
    it, then add only individually approved skills. If selective addition is
    unavailable, record the bundled catalog as an unresolved capability and
    get explicit approval or stop. Verify the generated command alias and do
    not change my sticky default profile unless I ask.
24. Write only parent-approved context. Keep secrets in the mechanism required
    by the current Hermes release, never in SOUL.md, USER.md, MEMORY.md, this
    repository, or a report.
    Treat the system prompt, conversation window, prompt memory, tool calls and
    results, injected workspace or skill context, attachments, transcripts,
    extracted text, and configured auxiliary-model flows as potentially visible
    to their model providers. Prefer coarse context over precise schools,
    locations, schedules, contacts, and family details unless their value
    justifies repeated provider exposure and I approve it.
    Use a standalone HERMES_HOME and purpose-specific credentials when adult
    credential access must be impossible. Do not assume a named profile or a
    plausible config key disables global auth. Empty configured fallback
    chains, launch from a scrubbed environment and profile-local synthetic HOME,
    and test the real launcher with the approved credential missing while adult
    credentials remain outside the approved scope. The request must fail closed.
25. Begin with the least capability. Add only approved tools, skills, plugins,
    MCP servers, gateways, memory providers, and other extensions.
    For each external capability, define the recipient, purpose, minimum data,
    retention, and approval rule. Keep ordinary non-identifying tool use
    available, but deny child-initiated public disclosure and minimize data
    sent to search, media, speech, messaging, forms, and other processors.
    Treat SOUL privacy rules as guidance. For tools that can publish, message,
    upload, submit, or persist external data, verify tool absence, narrow fixed
    scope, parent approval, or a tested argument filter as the enforced control.
    Ask about child-created reminders separately from general cron. If reminders
    are approved, prefer a narrow reminder path limited to stored reminder text,
    bounded schedules, and the verified child route. Do not expose scripts,
    skills, custom toolsets, work directories, context chaining, arbitrary
    destinations, or unrelated autonomous jobs without parent approval.
26. Inspect the resolved runtime after configuration. A declared allowlist or
    disabled setting is not sufficient evidence by itself.
    Inspect speech-to-text and attachment preprocessing, native media routing,
    MCP servers, plugins, hooks, dynamic tools, quick commands, and the final
    resolved tool-name set. Test the real input modalities, not prompts alone.
    For independent child access, use an identity-aware intake boundary unless
    the inspected runtime proves that sender ACLs, user/admin slash commands,
    pending approvals, confirmation replies, and dynamic commands are gated.
27. Recommend busy-input steering for ordinary one-child interaction when the
    current interface supports it. Explain queue and interrupt with examples,
    let me choose, and verify the selected behavior. Do not assume every busy
    message is a correction.

Verify before child use:

28. Start a fresh session so updated SOUL, memory, tool, and configuration state
    is loaded.
29. Test through the actual interface the child will use. Use synthetic data,
    read-only probes, and a disposable canary profile where a failed boundary
    could modify state or expose data. Never test with live secrets or real
    child disclosures. Run the approved
    personality samples, capability tests, privacy cases, memory cases,
    unauthorized-administration cases, failure cases, and applicable
    adversarial cases from EVALS.md.
30. Verify profile identity, effective tools, credential and account scope,
    memory reads and writes, access controls, provider data flow, alerts, and
    shutdown or recovery behavior where applicable.
    Remove or withhold the child-profile credential and verify that model access
    fails unless I explicitly approved another credential source.
31. Report what passed, failed, and remains unverified. Do not call the profile
    ready because files parse, a model says it follows rules, or repository
    checks pass.
32. If a critical requirement fails or remains unverified, do not give the
    profile to a child. Fix it, narrow the design, or document that the build
    has stopped.
33. Create a short private maintenance brief with review triggers for Hermes,
    model, provider, tools, extensions, memory, interface, access, family
    policy, and the child's changing needs.
34. Keep private build evidence in one parent-approved directory outside this
    repository. Use ENVIRONMENT.md, DECISION-RECORD.md, IDENTITY.md,
    BUILD-PROPOSAL.md, DATA-STORES.md, VERIFICATION.md, and MAINTENANCE.md.
    Record approval status and reviewer identity in the relevant artifact.

## Expected setup stages

The setup agent should produce these checkpoints:

1. **`ENVIRONMENT.md`**: installed release and commit/dirty state, current docs, existing names, intended interface, threat model, and isolation boundary.
2. **`DECISION-RECORD.md`**: parent choices, approval status, open questions, and conflicts.
3. **`IDENTITY.md`**: name check, personality traits, and all approved samples.
4. **`BUILD-PROPOSAL.md`**: files, commands, controls, data flows, and verification plan.
5. **Approval checkpoint**: no consequential changes before parent approval.
6. **Private build**: a fresh, non-cloned environment created outside this repository.
7. **`DATA-STORES.md` and `VERIFICATION.md`**: retention map plus evidence from the resolved runtime and real interface.
8. **`MAINTENANCE.md`**: review triggers and recovery steps.

## Stop conditions

The setup agent must stop when:

- the parent has not approved a consequential action;
- a required boundary cannot be enforced or verified;
- the intended child access exposes adult credentials or administration;
- a critical evaluation fails;
- provider, cost, privacy, or retention terms are unknown and material;
- the agent cannot distinguish the target profile from an existing one;
- the real interface cannot support the approved access or alert design.
