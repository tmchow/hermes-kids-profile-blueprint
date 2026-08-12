# Build a restricted child-facing profile

This runbook is for a trusted adult Hermes agent or a parent who will perform the steps manually.

## Goal

Create one private Hermes profile for one child. Give the profile only the capabilities that the parent approves. Verify the effective runtime before the child uses it.

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
2. Inspect the current Hermes documentation for profiles, authentication, toolsets, gateway authorization, and security.
3. Select a new generic profile name, such as `kids-1`.
4. Check that the target does not exist.
5. Identify the adult/default profile. Mark it as out of scope.
6. Explain the deployment modes to the parent.
7. Check current Hermes security advisories and known authorization bypasses
   against the installed version.
8. Stop if the selected mode or installed version cannot meet the parent's
   required boundary.

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
- the deployment mode;
- the proposed capability tier;
- the credential plan;
- the files that you will create or modify;
- the commands that need approval;
- the checks that the environment cannot support.

Get explicit approval before you configure credentials, messaging routes, background services, or external accounts.

## Phase 4: Build

1. Create a new profile or standalone Hermes home. Do not clone another profile.
   For a named profile, current Hermes releases support
   `hermes profile create <name> --no-skills --no-alias`. Verify the command
   against the installed release before use.
2. Confirm that the `.no-bundled-skills` marker exists. Do not rely on removing
   the initial bundled skills only. The marker also blocks later skill seeding.
3. Generate `SOUL.md` from `templates/SOUL.md.tmpl`.
4. Generate `memories/USER.md` from `templates/USER.md.tmpl` only if the parent enables static personalization.
5. Translate `baseline/baseline-policy.yaml` into the current Hermes configuration format.
6. Apply the appropriate fragments from `templates/config/` only after you verify each key against the installed Hermes version.
7. Keep plugins, MCP servers, hooks, quick commands, cron jobs, skills, delegation, autonomous memory, and session search off.
8. Set explicit toolsets for every enabled interface. Also add global denies for high-risk toolsets.
9. Configure a dedicated provider credential. Do not inherit or copy adult credentials.
10. Set provider-side quotas or spending caps when the provider supports them.
11. Configure the approved child interface.
12. Keep the child entrypoint unavailable until verification is complete.

Templates are source material. They are not complete profiles and must not be copied without inspection.

## Phase 5: Verify structure and runtime

Use `baseline/READINESS-CRITERIA.md` and the cases in `evals/`.

At minimum, verify in a fresh process:

- no unresolved Hermes security advisory invalidates a required control;
- the profile uses only its approved credential source;
- the profile fails closed when its credential is absent;
- the resolved tool list equals the approved list for each interface;
- the profile has no plugins, MCP servers, cron jobs, bundled skills, or unexpected hooks;
- memory and session-search behavior match the local policy;
- the child cannot use parent or administrative commands through the approved interface;
- the parent can stop or disable the child interface;
- a real model request succeeds with the approved credential;
- all enabled search, image, audio, and attachment paths pass separate tests.

Configuration parsing is not runtime verification. Asking the model to describe its own tools is not runtime verification.

## Phase 6: Run behavioral evals

Run all applicable cases in:

- `evals/behavioral.yaml`
- `evals/privacy.yaml`
- `evals/adversarial.yaml`

Run the cases through the interface that the child will use. Save only the evidence that the parent approved. Redact identifying information.

Behavioral results can change when the model, provider, SOUL, or Hermes version changes. Run the evals again after those changes.

## Phase 7: Report and hand off

Create a private build report that contains:

- profile name and path;
- Hermes version;
- deployment mode and interface;
- model and provider names, without credentials;
- enabled capabilities;
- local and provider retention choices;
- each check and its result;
- failed and unverified checks;
- residual risks;
- the command or action that stops child access;
- the next review date.

Use only these readiness results:

- `PASS`: All critical checks passed for the stated interface.
- `PASS WITH ACKNOWLEDGED LIMITATIONS`: The parent accepted a supervised-only mode. State each limitation.
- `FAIL`: One or more critical checks failed or remain unverified. Do not give the profile to a child.

## Phase 8: Operate and update

Follow `docs/OPERATIONS.md`. Start a new session or restart the gateway after changes that affect prompt, tools, credentials, or command access. Run the audit again before access resumes.
