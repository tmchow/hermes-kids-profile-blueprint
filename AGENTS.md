# Repository instructions

## Purpose and boundaries

This repository is a public, parent-operated starter kit for creating a useful child-facing Hermes profile. Keep the default path approachable. Put advanced technical checks behind the capabilities or access patterns that require them.

Keep changes small, reviewable, and limited to this repository. Do not build a real child profile here.

## Sources of truth

Read the files that govern the change before editing:

- `README.md` defines the public scope, design principles, and file map.
- `START-HERE.md` defines the setup-agent sequence.
- `DECISIONS.md` defines parent decisions and tradeoffs.
- `SOUL.md.seed`, `USER.md.seed`, and `MEMORY.md.seed` define the starter formats.
- `EVALS.md` defines evaluation scenarios.
- `MAINTENANCE.md` and `MEMORY-REVIEW.md` define review processes.
- `STYLE.md` defines public writing rules.
- `scripts/check_repository.py` defines the allowed repository shape and automated hygiene contract.

When files disagree, fix the inconsistency. Preserve consequential parent controls without turning supervised conversational use into a security audit.

## Privacy and security

Never commit:

- real child or family names, identifiers, contact details, schedules, schools, locations, photos, or account data;
- credentials, tokens, private keys, cookies, provider secrets, or local configuration;
- generated profiles, private design or build reports, session exports, transcripts, messages, memories, or evaluation results based on real people.

Use synthetic examples. Keep examples clearly fictional and no more specific than the test requires.

A Hermes profile separates Hermes state. It does not isolate the process from the operating-system account. `SOUL.md` guides model behavior; it does not enforce filesystem, credential, tool, network, or account boundaries. Do not describe repository checks or model promises as runtime enforcement.

When a claim depends on Hermes behavior, inspect the current official documentation at `https://hermes-agent.nousresearch.com/docs` and, when available, the installed runtime. Do not invent configuration keys, commands, capabilities, or isolation guarantees. Mark anything that cannot be checked as unverified.

## Product invariants

Preserve these rules unless the repository explicitly changes its documented policy:

- A parent or trusted adult controls family data, credentials, external services, messaging, spending, publishing, and child access.
- Start from the least capability and add only approved tools, skills, extensions, providers, and data flows.
- Keep non-attachment as a fixed relationship boundary. Warmth and playfulness are tunable; reciprocal friendship, affection, dependence, exclusivity, and persistent-presence claims are not.
- Escalate situations that require a trusted adult. Do not position the assistant as a substitute for a parent, clinician, emergency service, or other qualified person.
- Test the profile through the interface the child will use. Fix important failures before child use.
- Require advanced runtime and isolation checks only when independent access, powerful tools, external input, messaging, purchases, publishing, sensitive integrations, or strong privacy promises make them relevant.

## Editing workflow

1. Inspect the affected source files, related links, CI workflow, and repository checker.
2. Make the smallest coherent change. Update every affected public document when terminology, commands, file names, or contracts change.
3. Keep `AGENTS.md` as the canonical agent-instruction file. `CLAUDE.md` must remain a relative symlink whose target is exactly `AGENTS.md`; never replace it with a copy.
4. If the public file set changes, update `EXPECTED_FILES` and any related checks in `scripts/check_repository.py`.
5. Follow `STYLE.md`. Use direct, plain language. Remove generic filler, repeated summaries, puffery, and unsupported claims without weakening requirements.
6. Add or update automated checks when changing a machine-verifiable contract.
7. Inspect the final diff for private data, secrets, broken links, unintended files, and claims that outrun the evidence.

Do not make unrelated cleanup changes. Do not commit generated caches, dependency directories, temporary reports, or tool output.

## Validation

Run these checks from the repository root before opening or updating a pull request:

```sh
python3 scripts/check_repository.py
python3 -m py_compile scripts/check_repository.py
npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' '**/*.seed' '#.git'
npx --yes cspell@10.0.1 README.md AGENTS.md SECURITY.md STYLE.md START-HERE.md DECISIONS.md MEMORY-REVIEW.md EVALS.md MAINTENANCE.md EXAMPLE.md SOUL.md.seed USER.md.seed MEMORY.md.seed scripts/check_repository.py --no-progress --config cspell.json
git diff --check
```

Also run these checks when their commands are available:

```sh
actionlint .github/workflows/hygiene.yml
gitleaks dir --no-banner --redact .
gitleaks git --no-banner --redact
```

A passing repository checker proves repository hygiene only. Test the finished profile through the child-facing interface.

## Pull requests

- Branch from current `origin/main` and keep one coherent concern per pull request.
- Explain the user-visible or contract change and why it is needed.
- List the exact validation commands run and report failures or skipped checks honestly.
- Call out privacy, security, runtime, and compatibility effects when they are relevant to the change.
- Do not merge unless the maintainer explicitly asks.
