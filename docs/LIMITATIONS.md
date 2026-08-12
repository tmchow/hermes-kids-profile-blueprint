# Limitations

This blueprint cannot guarantee safe output.

Known limits include:

- A Hermes profile is not an operating-system sandbox.
- A separate operating-system account does not enforce Hermes policy against a
  child who controls that account.
- A normal local Hermes CLI exposes administrative commands and is not supported
  for unsupervised child access.
- SOUL instructions can fail.
- Model behavior can change after a provider update.
- Provider moderation can differ across text, images, audio, and search.
- Generic web search can return unsafe snippets or pages.
- Behavioral evals sample behavior. They do not prove all future behavior.
- A repository-owned validator cannot protect against a compromised repository.
- A parent can misconfigure the generated profile.
- Shared devices and accounts can expose data outside Hermes.
- Current gateway media handling can occur before the model tool loop. Text-only
  mode needs a separate tested intake boundary.
- At the pinned Hermes commit, `/status` and `/context` can bypass native slash
  gating during an active turn and expose session or runtime metadata. The
  baseline therefore needs a separate tested command-intake boundary.
- Replies to pending update prompts, tool approvals, and slash confirmations can
  be handled before slash authorization. A child session must not create or
  inherit that state.
- Messaging authorization keys are platform-specific. Current Telegram
  `allow_from` entries cover DMs, groups, and forums, so a separate tested
  boundary is required for DM-only Telegram access.
- A manual retention process has no guaranteed deletion deadline.
- Local deletion does not remove provider or messaging-platform copies.
- The blueprint does not replace parental judgment, platform parental controls, or emergency services.

The project documents evidence and residual risk. It does not certify a profile as universally safe.
