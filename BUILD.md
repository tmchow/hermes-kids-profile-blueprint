# Build a restricted child-facing deployment

This is an expert implementation contract for a trusted adult Hermes agent or an adult operator. It is not a turnkey installer.

## Goal

Create one private deployment for one child. Give the model only the capabilities that the parent approves. Keep the process and interface under parent control. Verify the effective production runtime before the child uses it.

## Required inputs

Read these files first:

- `baseline/SAFETY-REQUIREMENTS.md`
- `baseline/PARENT-DECISIONS.md`
- `baseline/READINESS-CRITERIA.md`
- `docs/DEPLOYMENT-MODES.md`
- `docs/CAPABILITY-TIERS.md`
- `docs/PRIVACY-AND-RETENTION.md`

Use the current [Hermes documentation](https://hermes-agent.nousresearch.com/docs) as the source of truth for commands and configuration keys.

## Phase 1: Inspect

1. Record the Hermes version, operating system, and available interfaces.
2. Inspect current Hermes documentation and source behavior for profiles, authentication, tool resolution, gateway authorization, media preprocessing, webhooks, hooks, skills, memory, and retention.
3. Select a new generic profile name, such as `kids-1`.
4. Check that the target does not exist.
5. Identify the default profile and every adult profile or Hermes home that could be a source of state or credentials. Mark each one out of scope.
6. Explain the supported access modes and additional isolation controls to the parent.
7. Check current Hermes security advisories and known authorization bypasses against the installed version.
8. Stop if the selected mode, adapter, provider, or installed version cannot enforce every required control.

Do not print credential values. Report only credential source types and provider names.

## Phase 2: Interview the parent

Use the questions in `baseline/PARENT-DECISIONS.md`. Ask one question at a time.

Do not ask for:

- a legal name;
- an exact birth date;
- a school, address, schedule, or precise location;
- names of friends, teachers, or family members;
- account passwords, API keys, tokens, or payment details;
- private photos or documents.

Store approved choices in a private local policy file inside the new profile or standalone Hermes home. Use restrictive file permissions where the operating system supports them.

## Phase 3: Plan

Show the parent:

- the target path;
- the access mode and additional isolation controls;
- the text-chat-only capability boundary;
- the production process owner and environment allowlist;
- the dedicated credential plan;
- the inbound media rejection boundary;
- the files that you will create or modify;
- the commands that need approval;
- the checks that the environment cannot support.

Get explicit approval before you configure credentials, messaging routes, background services, or external accounts.

## Phase 4: Build

1. Create a new profile or standalone Hermes home. Do not clone another profile.
   For a named profile, current Hermes releases support
   `hermes profile create <name> --no-skills --no-alias`. Verify the command
   against the installed release before use.
2. Confirm that the `.no-bundled-skills` marker exists. Verify local skills,
   external skill directories, bundles, dynamic skill commands, and the resolved
   skill list. No skill can remain available.
3. Generate `SOUL.md` from `templates/SOUL.md.tmpl`.
4. Generate `memories/USER.md` from `templates/USER.md.tmpl` only if the parent enables static personalization.
5. Translate `baseline/baseline-policy.yaml` into the current Hermes configuration format.
6. Apply fragments from `templates/config/` only after you verify each key against the installed Hermes version.
7. Use explicit minimal `platform_toolsets` for every enabled interface. Include `no_mcp`. Treat global denies as defense in depth.
8. Keep plugins, MCP servers, hooks, hook auto-accept, quick commands, cron jobs, webhook subscriptions, skills, delegation, autonomous memory, context-engine tools, and session search absent.
9. Configure a dedicated provider project and credential. Do not inherit or copy adult credentials.
10. Start the production process with an explicit environment allowlist. Use a synthetic `HOME` when required to isolate external CLI credentials.
11. Set provider-side quotas or spending caps when the provider supports them.
12. Configure a parent-controlled interface. Add a tested identity-aware pre-Hermes command boundary. For the child identity, it must admit plain text plus `/help` and `/whoami`, and reject every other slash command before Hermes receives it. It must preserve the verified parent admin route. Native Hermes slash gating is defense in depth: at the pinned commit, `/status` and `/context` can bypass that gate during an active turn.
13. Prevent the child session from creating or inheriting any update prompt, tool approval, or slash-confirmation state. Pinned Hermes handles replies to those states before slash authorization. The approved `clarify` tool is separate and remains available for normal child questions.
14. Prove the interface's DM-only boundary using platform-specific runtime behavior. Empty group allowlists are not proof. Current Telegram requires a separate tested pre-Hermes DM-only boundary. Unsupervised local CLI access is unsupported.
15. Enforce text-only mode. Disable gateway STT and reject image, voice, audio, video, and document input before Hermes preprocessing. If the selected adapter cannot enforce this, stop with `FAIL`.
16. Keep the child entrypoint unavailable until verification is complete.

Templates are source material. They are not complete profiles and must not be copied without inspection.

## Phase 5: Verify structure and runtime

Use `baseline/READINESS-CRITERIA.md` and the cases in `evals/`.

At minimum, verify through the actual production launcher or service after restart:

- no unresolved Hermes security advisory invalidates a required control;
- the process environment contains only approved variables and credential sources;
- the deployment fails closed when its credential is absent while adult credentials remain outside the approved scope;
- the resolved model-tool list equals the approved list for each interface;
- no plugin, MCP server, cron job, webhook subscription, skill, unexpected hook, or quick command is available;
- autonomous memory, context-engine tools, and session search are absent;
- for the child identity, the pre-Hermes boundary rejects `/status`, `/context`, and every other command except `/help` and `/whoami`, both while idle and during an active turn;
- the same identity-aware boundary preserves the verified parent admin route;
- the child session has no update prompt, tool approval, or slash-confirmation state, and cannot create one;
- the child cannot use parent or administrative commands;
- the parent identity is authorized as a sender and administrator;
- unauthorized senders and non-DM scopes are denied;
- the parent can stop or disable the child interface;
- a real model request succeeds with the approved credential;
- every unapproved media type is rejected before download, transcription, routing, caching, or provider transmission;
- retention statements match automatic controls or explicitly state that retention is manual without a guaranteed deadline.

Configuration parsing is not runtime verification. Asking the model to describe its own tools is not runtime verification. A scrubbed test process that differs from production is not runtime verification.

## Phase 6: Run behavioral evals

Run all applicable cases in:

- `evals/behavioral.yaml`
- `evals/privacy.yaml`
- `evals/adversarial.yaml`

Run the cases through the interface that the child will use. Follow the repetition and failure rule in `evals/README.md`. Save only evidence that the parent approved. Remove identifying information.

Behavioral results can change when the model, provider, SOUL, or Hermes version changes. Run the evals again after those changes.

## Phase 7: Report and hand off

Create a private build report that contains:

- profile name and path;
- Hermes version and reviewed commit;
- access mode, isolation controls, and interface;
- model and provider names, without credentials;
- production process owner and environment source types;
- the enforced text-chat-only capability boundary;
- local and provider retention choices;
- every critical check, its check result, and sanitized evidence type;
- failed and unverified checks;
- residual risks;
- the exact command or action that stops child access;
- the next review date.

Use one overall readiness label:

- `PASS`: Every applicable critical check passed for a parent-controlled interface.
- `PASS WITH ACKNOWLEDGED LIMITATIONS`: Every applicable critical check passed, but each session requires direct adult supervision under the parent account. State the shared-account limitation.
- `FAIL`: A critical check failed or remains unverified, a required control is unsupported, or the child can access a normal local CLI. Do not give the deployment to a child.

## Phase 8: Operate and update

Follow `docs/OPERATIONS.md`. Stop access before changes. Start a new production-equivalent process after changes that affect prompt, tools, credentials, process environment, command access, media intake, webhooks, or retention. Run the audit again before access resumes.
