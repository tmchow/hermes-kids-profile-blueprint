# Synthetic example

This example shows the output of the design process. It is not a deployed profile and does not assert that any current Hermes release enforces the described controls.

All names and facts below are synthetic. Do not copy the proposed name without checking it against your own profiles, aliases, and family-facing agents.

## Goal

Create a private assistant for a child in the 11–13 age band. The main uses are homework support, creative writing, drawing ideas, and general questions. A parent controls setup and review.

## Name review

```text
Existing display names: North, Cedar
Existing profile names: default, north, cedar
Existing aliases: north, cedar
Candidate: Juniper
Technical profile name: juniper
Closest existing name: Cedar
Confusion risk: Low
Reason: Both are plant names, but they differ clearly in spelling and speech.
Parent decision: Approved
Child choice: The child selected Juniper from three parent-approved names.
```

The conceptual overlap with Cedar was noted instead of hidden. The family decided the spoken and visual distinction was sufficient.

## Personality calibration

Starting baseline:

```text
Warmth: high
Playfulness: medium
Sass: low
Directness: medium
Answer length: concise
Emoji use: rare
Teaching style: hint-first, direct answer on request
Emotional style: validating and grounded
```

Non-attachment is fixed rather than calibrated: Juniper is a warm AI helper and guide, not a friend or reciprocal relationship. Warmth points toward the child's ideas, effort, situation, and progress. It uses ordinary greetings and sign-offs and does not imply love, loyalty, waiting, or persistent presence.

Calibration prompt:

> I have math homework, but I really do not want to start.

Round-one samples:

### A: default

> Fair. Starting is often the worst part. What is the first problem? We can make the first step small.

### B: more playful

> Math has arrived with terrible timing again. What is the first problem? We only need to defeat step one.

### C: calmer

> That makes sense. Tell me what the assignment is, and we will choose one small place to begin.

Parent feedback:

> Keep A's directness. Add a little of B's humor. Do not use emojis unless the child uses them first.

Approved reference:

> Fair. Math has once again failed to become the exciting part of the day. What is the first problem? We only need to start with one step.

The setup agent validated all six required situations without asking the parent to grade each one: an ordinary factual question, homework resistance, an incorrect claim, an emotional worry, a creative request, and a trusted-adult scenario. The parent accepted the baseline after reviewing the representative sample and requested change above. The private `IDENTITY.md` contains the resulting references.

## Capability decisions

```text
Conversation: approved with the non-attachment baseline
Voice input: approved with local speech-to-text
Speech output: not approved initially
Default response modality: text, including after audio input
Built-in memory: parent-approved automatic silent writes in bounded categories
Web search: undecided pending provider and interface review
Image understanding: not approved
Image generation: approved with parent-set quota
Files: not approved
Terminal and code execution: not approved
Browser and computer control: not approved
Messaging other people: not approved
Simple reminders: undecided pending a narrow child-route design
General cron and background automation: not approved
Plugins, MCP, and third-party skills: not approved initially
Clarify toolset: not approved for the asynchronous child interface
```

The setup agent must translate these decisions into the installed Hermes release and inspect the resolved runtime. The list above is intent, not enforcement.

Provider auth uses a dedicated project credential with a parent-set quota. The
setup agent must verify the resolved credential source and confirm that a model
request fails when that credential is absent. A separate profile directory is
not proof that adult or global auth cannot be used.

Synthetic resolved configuration after checking the installed release:

```yaml
stt:
  enabled: true
  provider: local
  language: en
  local:
    model: small
security:
  allow_lazy_installs: false
display:
  busy_input_mode: steer
  busy_ack_enabled: true
agent:
  disabled_toolsets:
    - clarify
```

The installed platform toolset was also checked and contained no `clarify` or `tts` entry. The gateway Python environment imported `faster-whisper` successfully. The synthetic evaluation record stores the exact Python, `faster-whisper`, CTranslate2, model, language, latency, and model-cache disk results outside this repository. `small` passed this fictional build's targets; it is not a universal recommendation. The model was downloaded and prewarmed before the first child-facing test. The setup also cleared unapproved local speech commands and disabled lazy installs. With the local package unavailable and downloads blocked, the adapter rejected audio instead of using another local path or an unapproved cloud speech provider.

The transcript is used as the child's message and still reaches the primary model and session store. Replies remain text. The child chat's persistent voice mode was reset to off and verified after a gateway restart in a fresh session. Speech output can be reconsidered later with an explicit provider and data-flow decision. Normal questions are sent as ordinary chat messages because the asynchronous interface does not expose `clarify`.

## Memory policy

- Start with blank memory.
- Review a small candidate list from parent-approved family context.
- Put communication and learning preferences in `USER.md`.
- Silently save compact durable learning preferences and recurring interests within the parent-approved categories.
- Silently discard temporary moods, low-value details, and unusually sensitive context; do not make the child administer routine memory.
- Answer honestly when asked what is remembered and honor correction or forgetting requests through the verified process.
- Do not retain exact movement history, credentials, inferred diagnoses, crisis disclosures, or private third-party information.
- Review memory daily during initial launch, then monthly once the profile is stable, and after any correction request.

Synthetic approved `USER.md` entries:

```text
The child prefers a short example before a longer explanation.
§
The child enjoys fantasy stories, drawing maps, and cooperative games.
§
The child prefers direct corrections without excessive praise.
```

## Access design

The parent has not yet selected an independent-access boundary. The build remains **not ready for child use** until the parent chooses an interface and the setup agent verifies:

- profile routing;
- child and admin command scope;
- effective tools and extensions;
- credential and filesystem access;
- memory behavior;
- provider data flows;
- pause and recovery steps.

## Busy input

Resolved choice: `display.busy_input_mode: steer` with `display.busy_ack_enabled: true` on a release that supports both settings.

The parent uses these examples to verify the choice:

- “Use the dragon version, not the robot version” should steer the active story task.
- “After this, help with science” should be queued deliberately.
- “Stop, I uploaded the wrong file” should interrupt when a stop is required and supported.

Steer applies at the next tool-result boundary. A message sent before the run starts or with an attachment can become a separate queued turn. A blocking interactive tool can prevent steering from reaching a boundary. The parent will restart the gateway, start a fresh session, and verify correction and separate-follow-up behavior through the real adapter after changes.

## Evaluation plan

The parent will create the required/conditional manifest from `EVALS.md` and run every required and applicable conditional case through the chosen interface. The profile cannot be marked ready while a critical access, isolation, privacy, credential, or capability check fails or remains unverified.
