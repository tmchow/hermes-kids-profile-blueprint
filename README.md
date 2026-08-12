# Hermes Kids Profile Blueprint

> **Pre-release:** This repository is under security review. Do not treat the current branch as ready for child use.

A reference kit for parents who want to assess and build a restricted, child-facing [Hermes Agent](https://hermes-agent.nousresearch.com/docs) deployment.

This repository is a blueprint. It is not an installable Hermes profile, a content filter, an operating-system sandbox, or a safety certificate. A trusted adult must build a private deployment, verify the effective runtime, and keep control of the child interface.

This repository does not ship the required pre-Hermes command, scope, and media boundary. The templates alone cannot produce an independent-access deployment with a positive readiness label.

## Read this first

A Hermes profile separates Hermes configuration, sessions, and memory. It does not limit the operating-system permissions of the user who runs it. A child who controls a normal local Hermes CLI can use administrative slash commands or start another Hermes entrypoint. This blueprint does not support unsupervised local CLI access.

Supported access modes are:

1. **Parent-controlled messaging gateway:** For independent child access. The parent must control the process, sender allowlists, command intake, credentials, and media intake. This pre-release supports text chat only. A tested identity-aware pre-Hermes boundary must admit child plain text plus `/help` and `/whoami`, reject other child slash commands, preserve the verified parent admin route, reject non-DM scopes, and reject media before Hermes receives it. Current Telegram needs this separate boundary because its main sender allowlist also covers groups and forums.
2. **Parent-account supervised session:** For direct adult supervision only. It cannot receive `PASS`; use `PASS WITH ACKNOWLEDGED LIMITATIONS` only when every applicable critical check passes.

A separate operating-system account, container, sandbox, or host can protect parent resources. It does not by itself stop a child who controls that environment from changing a local Hermes configuration. A standalone Hermes home is an additional state-separation control, not an access mode.

Read [Deployment modes](docs/DEPLOYMENT-MODES.md) before you build.

## What is in this repository

- A mandatory safety baseline
- A parent decision guide
- An expert build contract for a trusted Hermes agent
- Sanitized SOUL, static personalization, config, and launcher templates
- Structural, runtime, privacy, and behavioral evaluation cases
- Readiness rules that distinguish verified controls from assumptions
- Operating, update, retention, and deletion guidance

The repository contains no active `SOUL.md`, `config.yaml`, credentials, child data, or profile distribution manifest. The build agent creates the private deployment outside this repository.

## Who should use it

This pre-release is for a parent or guardian who:

- already administers Hermes Agent;
- can inspect configuration and runtime behavior;
- can create separate provider credentials and spending limits;
- can operate a parent-controlled child interface;
- will test the complete production path before a child uses it.

This is not a consumer parental-control product. `BUILD.md` is an expert implementation contract, not a turnkey manual installer.

## Agent-assisted build

Review a specific commit before you give it to an agent. Do not use an unreviewed branch for a child deployment.

Open a trusted adult Hermes session in this repository. Then paste this prompt:

```text
Read BUILD.md in this repository. Use it as the build contract for a new
restricted child-facing Hermes deployment.

Before you change anything:
- inspect my Hermes version and the current official Hermes documentation;
- explain the supported access modes and their limits;
- ask me the required parent questions one at a time;
- do not ask for secrets or unnecessary identifying information about a child.

Build the deployment outside this repository. Do not modify my default or
adult profiles. Do not copy credentials, memory, sessions, or personal files
from another profile. Use the baseline requirements, templates, and eval cases
in this repository. Do not say the deployment is ready until every applicable
critical check passes. Report failed and unverified checks separately.
```

The agent must show the plan and target path before it writes files. The parent must approve credential setup, gateway changes, service installation, or any action that affects another user or external system.

## Validate this blueprint

The repository validator checks the blueprint itself. It does not prove that a generated deployment is safe.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_blueprint.py
python3 -m unittest discover -s tests -v
```

Use the eval cases in [`evals/`](evals/) to test the generated deployment through its real child-facing interface.

## Safety model

The mandatory requirements are in [baseline/SAFETY-REQUIREMENTS.md](baseline/SAFETY-REQUIREMENTS.md). The main rules are:

- Use one private deployment for one child.
- Run the production process with an explicit environment allowlist.
- Do not inherit adult credentials.
- Expose only an exact verified tool allowlist.
- Keep plugins, MCP, cron, webhooks, delegation, skills, autonomous memory, and cross-session search absent.
- Reject unapproved image, audio, video, and document input before Hermes processes it.
- Treat SOUL instructions and behavioral evals as guardrails, not enforcement.
- Use a fresh production-equivalent process and rerun the audit after any relevant change.

## Project status

The repository remains pre-release. No tag is ready for adoption. No included reference build can pass the independent-access readiness contract because the required pre-Hermes intake boundary is not included. The current macOS and Linux material is reference work while runtime-aware security checks are added.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [STYLE.md](STYLE.md). Security-sensitive changes need evidence and review.

## License

MIT. See [LICENSE](LICENSE).
