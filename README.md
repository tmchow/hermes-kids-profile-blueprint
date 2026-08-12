# Hermes Kids Profile Blueprint

A reference kit for parents who want to build a restricted, child-facing [Hermes Agent](https://hermes-agent.nousresearch.com/docs) profile.

This repository is a blueprint. It is not an installable Hermes profile, a content filter, or an operating-system sandbox. Your trusted adult Hermes agent reads the blueprint, asks you a short set of questions, and builds a private profile for your environment.

## Read this first

A Hermes profile separates Hermes configuration, sessions, and memory. It does not limit the operating-system permissions of the user who runs it.

Use one of these deployment modes:

1. **Separate operating-system account:** Recommended for local child access.
2. **Parent-controlled messaging gateway:** Recommended when the child uses a messaging app. Use sender allowlists and parent-only command access.
3. **Standalone Hermes home:** Isolates Hermes state and credentials. Combine it with a separate operating-system account when you need a hard user boundary.
4. **Parent account:** Suitable only for direct adult supervision.

Read [Deployment modes](docs/DEPLOYMENT-MODES.md) before you build.

## What is in this repository

- A mandatory safety baseline
- A parent decision guide
- A build runbook for a trusted Hermes agent
- Sanitized SOUL, user-profile, config, and launcher templates
- Structural, runtime, privacy, and behavioral evaluation cases
- Readiness rules that distinguish verified controls from assumptions
- Operating, update, retention, and deletion guidance

The repository contains no active `SOUL.md`, `config.yaml`, credentials, child data, or profile distribution manifest. The build agent creates the profile outside this repository.

## Who should use it

This first release is for a parent or guardian who:

- already uses Hermes Agent;
- can review file changes and terminal commands;
- can create separate provider credentials and spending limits;
- will test the result before a child uses it.

This is not a consumer parental-control product.

## Agent-assisted build

Review this repository before you give it to an agent. Use a tagged release or a reviewed commit when possible.

Open a trusted adult Hermes session in this repository. Then paste this prompt:

```text
Read BUILD.md in this repository. Use it as the build contract for a new
restricted child-facing Hermes profile.

Before you change anything:
- inspect my Hermes version and the current official Hermes documentation;
- explain the deployment modes and their limits;
- ask me the required parent questions one at a time;
- do not ask for secrets or unnecessary identifying information about a child.

Build the profile outside this repository. Do not modify my default profile.
Do not copy credentials, memory, sessions, or personal files from another
profile. Use the baseline requirements, templates, and eval cases in this
repository. Do not say the profile is ready until all critical checks pass.
Report failed and unverified checks separately.
```

The agent must show you its plan and target path before it writes files. You must approve credential setup, gateway changes, service installation, or any action that affects another user or external system.

## Manual build

Follow [BUILD.md](BUILD.md). The manual and agent-assisted paths use the same requirements and readiness criteria.

## Validate this blueprint

The repository validator checks the blueprint itself. It does not prove that a generated profile is safe.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_blueprint.py
python3 -m unittest discover -s tests -v
```

Use the eval cases in [`evals/`](evals/) to test the generated profile through its real child-facing interface.

## Safety model

The mandatory requirements are in [baseline/SAFETY-REQUIREMENTS.md](baseline/SAFETY-REQUIREMENTS.md). The main rules are:

- Use one profile or Hermes home for one child.
- Do not inherit the adult profile's credentials.
- Do not expose terminal, files, browser control, messaging, plugins, MCP, cron, delegation, skills, or cross-session search.
- Keep optional web and media capabilities off until the parent tests the actual provider path.
- Treat SOUL instructions and behavioral evals as guardrails, not enforcement.
- Use a fresh session and rerun the audit after any relevant change.

## Project status

Version `0.1.0` is a reference blueprint. It documents a conservative macOS and Linux starting point. Other platforms and provider combinations can work, but they remain unverified until someone tests and documents them.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [STYLE.md](STYLE.md). Security-sensitive changes need evidence and review.

## License

MIT. See [LICENSE](LICENSE).
