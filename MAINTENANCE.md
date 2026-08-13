# Maintenance

A child-facing profile needs review because Hermes, models, providers, interfaces, and children change.

Keep the maintenance brief with the private profile, not in this repository.

## Review triggers

Review immediately after changes to:

- Hermes version or installation method;
- model, provider, fallback chain, or provider terms;
- `SOUL.md`, `USER.md`, or `MEMORY.md`;
- tools, toolsets, skills, plugins, MCP servers, webhooks, cron, delegation, or memory providers;
- child-facing interface, gateway, routing, allowlist, or admin commands;
- credentials, OS account, filesystem, network, sandbox, or device access;
- memory write approval, session retention, logs, backups, or deletion;
- alert mechanism or parent recipient;
- the child's age, independence, communication style, learning needs, or family circumstances;
- an unexpected behavior, privacy concern, failed alert, or attempted bypass.

Run a routine review on a parent-chosen schedule even when no trigger is visible.

## Review sequence

1. Pause independent child access when the change could affect a critical boundary.
2. Inspect the installed CLI help and current official documentation.
3. Select and explain the supported backup method for that release.
4. Back up the private profile and verify the backup can be read.
5. Record the installed version and commit/dirty state, model, provider, interface, and extensions.
6. Inspect the resolved tools, profile route, credentials, memory settings, isolation posture, and external data flows.
7. Compare the current build with the approved decision record and data-store inventory.
8. Review new or changed memories.
9. Rerun required and conditional cases from `EVALS.md` through the real child interface.
10. Fix failures or narrow the design.
11. Give the parent a short change report.
12. Restore child access only after critical checks pass.

## Personality recalibration

The locked personality is a durable baseline, not a permanent answer.

Recalibrate when:

- the child says the agent sounds babyish, annoying, too formal, too jokey, or unhelpful;
- the parent sees repeated tone or teaching problems;
- the model changes;
- the child's age or needs change.

Use the original approved sample prompts. Compare the current responses, adjust one or two traits per round, approve revised samples, update `SOUL.md`, start a fresh session, and test again.

## Naming review

Recheck name similarity when a new family agent or profile is added. A previously distinct name can become confusing later.

Check display names, profile names, aliases, spoken forms, spelling variants, roots, and family conversational use. Rename only through the current supported Hermes process and test every interface and route afterward.

## Memory review

At each review:

- remove stale or low-value facts;
- correct inaccurate entries;
- check emotional entries for identity labels;
- inspect pending writes when approval is enabled;
- confirm the child and parent can request deletion;
- verify that rejected or deleted facts do not return through another provider or session source.

## Incident response

When a material problem occurs:

1. stop or pause child access;
2. preserve enough evidence to understand the event without spreading private data;
3. identify whether the failure was model behavior, configuration, access control, interface routing, provider behavior, or another system;
4. revoke or rotate affected credentials when needed and approved;
5. correct or delete affected memory and sessions;
6. fix the boundary or narrow the profile;
7. rerun the relevant evaluations;
8. document what changed and what remains unknown.

Do not rely on a longer `SOUL.md` when the failure requires an enforced control.

## Change report

Use this format:

```text
Review date:
Reviewer:
Hermes version:
Model and provider:
Interface:
Reason for review:
Changes found:
Private-data flow changes:
Resolved-tool changes:
Memory changes:
Tests run:
Failures:
Unverified items:
Actions taken:
Parent decision:
Next review trigger or date:
```
