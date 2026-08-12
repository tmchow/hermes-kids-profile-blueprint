# Security policy

## Scope

This repository contains documentation, templates, policy intent, and evaluation cases. It does not provide an operating-system sandbox or a guarantee of age-appropriate model output.

A generated deployment is only as strong as its local controls, credentials, provider controls, interface authorization, and current Hermes configuration.

## Security boundary

A Hermes profile separates Hermes state. It does not remove the permissions of the operating-system user who runs Hermes.

Use a separate operating-system account, container, sandbox, or host when the child must not access files and credentials available to the parent account. A prompt and a tool allowlist are not substitutes for that boundary.

## Report a problem

Use a private GitHub security advisory for a vulnerability that could weaken the baseline, expose private information, or cause unsafe setup behavior. Do not include real child data, credentials, private transcripts, or exploitable production details in a public issue.

Use a public issue for documentation errors that do not expose private or security-sensitive information.

## Review requirements

A security-sensitive change must include:

- the requirement that changes;
- the threat or failure mode;
- the affected deployment modes;
- a test that fails before the change and passes after it;
- the effect on existing local builds;
- any required rebuild, restart, or reevaluation step.

The repository's validator is not an independent security audit. A compromised repository can change both a template and its test. Parents must review releases and verify the generated deployment in their own environment.
