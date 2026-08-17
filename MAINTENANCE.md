# Maintenance

Keep a short maintenance note with the private profile. Review soon after launch, then use a lighter cadence that fits the family. Always review after a meaningful change or unexpected behavior.

## Review triggers

Review after changes to:

- Hermes, the model, a provider, or the child-facing interface;
- `SOUL.md`, `USER.md`, `MEMORY.md`, or the memory approach;
- tools, skills, voice, reminders, messaging, or other integrations;
- credentials, spending limits, recipients, or external data flows;
- the child's age, needs, independence, or main uses;
- family rules or parent involvement;
- any unexpected behavior, privacy concern, or failed action.

A small tone change may need only a few conversation checks. A new powerful tool, independent access, messaging route, purchase path, publishing path, or sensitive integration needs the applicable conditional checks in `EVALS.md`.

## Lightweight review

1. Ask whether the profile is still useful for its intended jobs.
2. Check the name, tone, teaching style, and trusted-adult behavior with a few synthetic prompts.
3. Review enabled capabilities and remove anything no longer needed.
4. Check memory for stale, inaccurate, overly specific, or identity-forming entries.
5. Confirm that the parent can pause the profile and update it.
6. Start a fresh session after configuration or prompt changes.
7. Run the core checklist in `EVALS.md` through the actual child interface.
8. Record failures, untested items, and the next action.

## Conditional technical review

Use this section only when the changed design includes independent access, powerful tools, external input, messaging, purchases, publishing, sensitive integrations, or explicit isolation and retention promises.

Check the parts that apply:

- final resolved tools and child-facing commands;
- profile routing and parent-only administration;
- credential source, quotas, and provider fallback;
- external recipients and approval steps;
- uploaded, web, plugin, or MCP content paths;
- voice provider and local model readiness;
- reminder, alert, messaging, and delivery behavior;
- restricted OS account or other approved process boundary;
- backup, restore, retention, and deletion procedures.

Use current Hermes documentation and the installed runtime. Do not rely on a configuration key that the installed release does not support.

## Personality recalibration

Recalibrate when the child finds the assistant babyish, annoying, too formal, too jokey, or unhelpful, or when the model or child's needs change.

Use the original sample prompts. Adjust one or two traits at a time, approve the revised examples, update `SOUL.md`, start a fresh session, and test again.

## Memory review

- remove stale or low-value facts;
- correct inaccurate entries;
- remove diagnoses and fixed identity labels based on temporary feelings;
- inspect pending writes when approval is enabled;
- honor correction and forgetting requests through the verified process;
- distinguish curated-memory deletion from session, backup, and provider retention.

## Optional parent learning review

A parent may privately review recurring interests, learning approaches, and friction points to improve the profile. Keep this review read-only and separate from the child-facing conversation.

Use real child sessions only when the parent has approved that review. Exclude setup and synthetic tests. Summarize patterns instead of dumping transcripts. Separate observations from interpretations and recommendations. Never invent an incident, quote, or trend.

## When something goes wrong

1. Pause child access when continued use could make the problem worse.
2. Preserve only the minimum private evidence needed to understand the event.
3. Identify whether the issue came from conversation behavior, configuration, routing, a provider, or an external tool.
4. Rotate affected credentials when needed and approved.
5. Correct affected memory or configuration.
6. Remove or narrow the failing capability.
7. Rerun the relevant core and conditional tests.
8. Record what changed and what remains unknown.

## Change note

```text
Review date:
Reviewer:
Reason for review:
Hermes, model, provider, and interface changes:
Profile or personality changes:
Capability and data-flow changes:
Memory changes:
Tests run:
Failures or untested items:
Actions taken:
Parent decision:
Next trigger or review date:
```
