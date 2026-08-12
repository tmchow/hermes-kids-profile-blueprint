# Provider checks

The model provider and each media or search provider form part of the safety boundary.

## Before setup

Check:

- provider terms for minors and family use;
- prompt, output, upload, and log retention;
- training and data-use settings;
- text and media moderation;
- project-scoped credentials;
- hard spending limits or quotas;
- regional or account restrictions.

Use a dedicated provider project and credential. If the parent cannot provide one, the build is `FAIL`.

## During verification

Test the selected model and provider combination. A successful test with another model does not verify this one.

Run separate tests for:

- text input and output;
- image upload;
- image generation;
- speech input;
- speech output;
- web search.

For a disabled media path, test rejection through the real interface before Hermes preprocessing. A denied model tool does not prove that inbound media stays local.

Mark a path `NOT APPLICABLE` when it is disabled. Mark it `NOT VERIFIED` when it is enabled but not tested.

## Cost controls

Set a hard provider-side limit when possible. Also limit turns and optional media generation in Hermes.

Do not rely on a prompt request such as "use less money." The provider or account must enforce the limit.
