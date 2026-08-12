# Parent decisions

Ask these questions one at a time. Explain the consequence of each answer. Every optional preference can be skipped.

## Required decisions

1. **Who will operate the profile?**
   - Use one profile for one child.
   - Record an age band, not a birth date.

2. **How will the child access Hermes?**
   - Parent-controlled messaging gateway
   - Parent-account session with direct supervision
   - Unsupervised local CLI access is not supported

3. **Which additional isolation controls do you need?**
   - Behavioral guardrails
   - Standalone Hermes home for Hermes-owned state separation
   - A hard user boundary with a separate account, container, sandbox, or host

4. **Does the text-chat-only capability tier meet your needs?**
   - Text chat is the only supported tier in this pre-release.
   - Search, image, audio, video, document, and external-action capabilities are outside this blueprint's readiness contract.
   - Stop the build if the parent requires an unsupported capability.

5. **Which provider and model will the profile use?**
   - Confirm that the provider terms and moderation are acceptable.
   - Confirm a dedicated credential and spending limit.

6. **How long should local conversations remain?**
   - Choose verified automatic expiry or manual deletion.
   - Do not promise a deadline for manual retention.
   - Record how the parent can review and delete local data.

7. **What is the approved parent administration route?**
   - Use a verified platform identity or local adult account.

8. **How will unapproved media be blocked?**
   - Identify the adapter, proxy, or platform boundary that rejects image,
     voice, audio, video, and document input before Hermes processes it.
   - Stop with `FAIL` when the selected interface cannot enforce this boundary.

## Optional personalization

- Assistant display name
- General age band
- Reading or explanation level
- Tone, such as calm, playful, or direct
- Broad interests, such as science, art, games, or cooking
- Hint-first or answer-first learning preference
- Topics that should always involve a trusted adult

Do not record details that identify a child, school, schedule, location, friend, teacher, or private account.

## Final confirmation

Before the build starts, show the parent:

- the chosen deployment mode;
- the text-chat-only capability boundary;
- the data that will be stored;
- the external providers that will receive data;
- the spending controls;
- the checks that can and cannot be verified.
