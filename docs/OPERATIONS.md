# Operate the profile

## Before each handoff

- Confirm the intended profile and interface.
- Confirm that the child cannot reach an adult profile.
- Confirm that the provider spending limit is active.
- Confirm that the parent knows how to stop access.

## Stop access

Document one exact stop action in the private build report. The action can stop a gateway service, disable a route, revoke a child sender, or remove local access.

Test the stop action before handoff.

## Review

Set a review schedule that matches the child's use and the enabled capabilities. Review sooner after a model, provider, Hermes, SOUL, tool, gateway, or retention change.

Check current Hermes security advisories before handoff and after each Hermes update. A runtime authorization defect can make a correct configuration ineffective.

Transcript review detects some failures after they occur. It is not the main safety control.

## Update

1. Stop child access.
2. Back up the local policy and generated profile files. Do not export child history unless the backup requires it and the parent approves it.
3. Review changes to Hermes and this blueprint.
4. Rebuild or reconcile the generated profile.
5. Start a fresh process.
6. Run all critical structural and runtime checks.
7. Run applicable behavioral evals.
8. Restore child access only after the readiness result permits it.

## Delete

Delete each data layer separately:

- the Hermes profile or standalone home;
- local backups and generated media;
- messaging-platform history;
- provider logs or stored data, where the provider permits deletion;
- dedicated credentials and tokens.

Verify deletion without printing private content.
