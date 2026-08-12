# Capability tiers

This pre-release supports one capability tier: text chat. Search and media are outside the readiness contract.

## Text chat

Allowed capabilities:

- conversation;
- age-appropriate explanations;
- tutoring and brainstorming without external tools;
- clarification questions.

Keep search, images, audio, files, browser control, external actions, memory tools, context-engine tools, and extensions off. Disable gateway STT and reject unapproved media before Hermes receives or downloads it. Tool denies alone do not enforce text-only intake.

## Unsupported capabilities

This pre-release does not support:

- web search;
- image or document input;
- image or video generation;
- speech input or output;
- file access;
- browser or computer control;
- external actions;
- memory or context-engine tools;
- plugins, MCP, hooks, webhooks, cron, delegation, or skills.

A parent can build a different Hermes deployment with these capabilities. That deployment is outside this blueprint's readiness contract and cannot use this blueprint's positive readiness labels.

Do not describe generic web search or model instructions as SafeSearch. Do not assume that text moderation covers images or audio.
