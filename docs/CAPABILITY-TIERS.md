# Capability tiers

Start with the text-chat tier. Add one capability at a time. Test the complete provider and interface path after each change.

## Text chat

Allowed capabilities:

- conversation;
- age-appropriate explanations;
- tutoring and brainstorming without external tools;
- clarification questions.

Keep search, images, audio, files, browser control, external actions, memory tools, and extensions off.

## Creative media

This tier can add passive image understanding, moderated image generation, or speech.

Before you enable a media capability:

1. Check the provider's moderation and retention terms.
2. Use a dedicated credential and spending limit.
3. Test input and output moderation.
4. Test each attachment type through the real child interface.
5. Explain to the parent what leaves the device and what persists.

Do not assume that text moderation also covers images or audio.

## Supervised web

This tier can add narrow search under adult supervision.

Before you enable search:

1. Identify the exact search backend.
2. Check whether the backend enforces SafeSearch or supports an educational source allowlist.
3. Test explicit, violent, hateful, and prompt-injection queries.
4. Test snippets and linked pages separately.
5. Record the backend limits in the readiness report.

Generic web search is not child-safe by default. Model instructions do not enforce SafeSearch.

## Excluded capabilities

The blueprint does not support enabling terminal, code execution, files, browser automation, computer control, outbound messaging, email, calendar, contacts, smart-home control, plugins, MCP, cron, delegation, skill management, or cross-session search for the child-facing profile.

A parent can build a different profile with those capabilities. That profile is outside this blueprint's readiness contract.
