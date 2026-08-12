# Changelog

## Unreleased

- Marked the repository pre-release after runtime-aware security review.
- Removed unsupervised local CLI from the supported contract.
- Required production credential isolation, exact tool resolution, DM-only
  authorization, pre-Hermes media rejection, webhook absence, and honest
  retention reporting.
- Narrowed the pre-release readiness contract to text chat only.
- Documented that DM-only authorization is platform-specific and that current
  Telegram needs a separate pre-Hermes scope boundary.
- Required an identity-aware pre-Hermes command boundary because `/status` and
  `/context` bypass native slash gating during active turns at the pinned commit.
- Required child sessions to exclude update-prompt, tool-approval, and
  slash-confirmation state that pinned Hermes handles before slash authorization.
- Stated that the repository does not yet ship the required intake boundary, so
  its templates alone cannot produce a positive independent-access result.

## 0.1.0 - withdrawn

- Added the first public blueprint draft. This version was not tagged and is not ready for adoption.
- Added the safety baseline and parent decision guide.
- Added sanitized templates for SOUL, static personalization, configuration, and a restricted launcher.
- Added structural, runtime, privacy, behavioral, and adversarial eval cases.
- Added repository validation and continuous integration.
