# Deployment modes

Select the access mode before you select a personality or model.

## Parent-controlled messaging gateway

Use this mode for independent child access.

The parent must control:

- the operating-system user and Hermes process;
- the production environment and credential allowlist;
- an explicit child sender allowlist;
- a verified parent administrative identity that is also in the sender allowlist;
- a tested identity-aware pre-Hermes command boundary that admits child plain text plus `/help` and `/whoami`, rejects every other child slash command before Hermes receives it, and preserves the verified parent admin route;
- media and attachment rejection before Hermes preprocessing;
- the tested stop action.

Native Hermes slash gating is not sufficient for this baseline. At the pinned commit, `/status` and `/context` can bypass it during an active turn and expose session or runtime metadata. Test the external command boundary while the agent is idle and while it is responding.

Pinned Hermes also handles replies to pending update prompts, tool approvals, and slash confirmations before slash authorization. The child session must not create or inherit that state. This does not disable the approved `clarify` tool.

DM and group authorization differ by platform. The baseline supports DM-only access. Prove that the selected adapter or an external pre-Hermes boundary rejects groups, channels, forums, and threads. Empty group allowlists are not proof. An unverified scope produces `FAIL`.

Current Telegram `allow_from` entries authorize the same sender in DMs, groups, and forums. The generic fragment does not make Telegram DM-only. Use a tested external DM-only boundary or treat Telegram as unsupported for independent access under this blueprint.

A gateway can limit who talks to the profile. It does not create an operating-system sandbox for the gateway process.

## Parent-account supervised session

Use this mode only when an adult directly supervises each session and controls the terminal.

The process can have the same operating-system access as the parent. A launcher and tool restrictions reduce accidental use. They do not stop a user who can control the parent account or invoke another Hermes entrypoint.

Every applicable critical check must still pass. The overall readiness label must be `PASS WITH ACKNOWLEDGED LIMITATIONS`, and the report must list the shared-account risks.

## Additional isolation controls

### Separate operating-system account

A separate account can limit access to parent resources only when operating-system permissions, ACLs, shared folders, mounted volumes, browser data, and credential stores are verified.

This protects parent resources from the child account. It does not enforce the parent’s Hermes policy against a child who controls the child account. A normal local Hermes CLI remains unsupported for unsupervised use.

### Standalone Hermes home

A standalone Hermes home separates Hermes-owned configuration, authentication files, sessions, memory, and logs from the adult Hermes home.

It does not isolate shell credentials, external CLI credentials, or other process environment secrets. Use a parent-controlled production launcher or service with a scrubbed environment, a synthetic `HOME` where required, and an explicit variable allowlist.

A standalone Hermes home runs with the permissions of its operating-system user. Combine it with a separate account, container, sandbox, or host when the parent threat model needs a hard resource boundary.

## Selection guide

- Choose a parent-controlled messaging gateway for independent access.
- Choose a parent-account session only for direct adult supervision.
- Add a separate operating-system account to protect parent resources after you verify permissions.
- Add a standalone Hermes home to separate Hermes-owned state.
- Do not claim readiness for unsupervised local CLI access under this blueprint.
