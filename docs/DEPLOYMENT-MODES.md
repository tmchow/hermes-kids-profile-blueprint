# Deployment modes

Select the deployment mode before you select a personality or model.

## Separate operating-system account

Use this mode when a child needs local access.

The child account limits access to files and credentials in the parent account. Configure the Hermes profile inside the child account. Use a dedicated provider credential.

A separate account is the recommended local boundary. It still needs Hermes tool restrictions, provider controls, and testing.

## Parent-controlled messaging gateway

Use this mode when the child will chat through a supported messaging platform.

Configure:

- an explicit child sender allowlist;
- a verified parent administrative identity;
- the smallest supported child command set;
- separate child and parent tests through the real platform.

A gateway can limit who talks to the profile. It does not create an operating-system sandbox for the gateway process.

## Standalone Hermes home

A standalone Hermes home separates configuration, credentials, sessions, memory, and logs from the adult Hermes home.

Use a scrubbed process environment and a synthetic `HOME` when the deployment requires credential separation from user-level command-line tools. Verify that no global Hermes authentication fallback remains.

A standalone Hermes home runs with the permissions of its operating-system user. Combine it with a separate account, container, sandbox, or host when you need a hard user boundary.

## Parent-account supervised mode

Use this mode only when an adult directly supervises each session.

The process can have the same operating-system access as the parent. A launcher and tool restrictions reduce accidental use. They do not stop a determined user who can access the parent account.

The readiness report must use `PASS WITH ACKNOWLEDGED LIMITATIONS` and list the shared-account risks.

## Selection guide

- Choose a separate account for local independent use.
- Choose a parent-controlled gateway for messaging access.
- Add a standalone Hermes home when Hermes state and credentials must remain separate.
- Use the parent account only for supervised sessions.
