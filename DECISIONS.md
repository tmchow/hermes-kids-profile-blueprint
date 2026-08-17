# Parent decisions

Use this page to guide a natural conversation. Do not read it as a questionnaire. Ask only about choices that matter to this family. Apply the recommended defaults when the parent has no preference.

## 1. Intended experience

Learn:

- who will use the profile;
- the child's age or developmental band;
- the main jobs, such as learning, creativity, games, or general questions;
- the child-facing interface;
- whether use is supervised, independent, or mixed;
- who can pause, review, and update the profile.

**Recommended default:** begin with supervised conversation. If the child will use the profile independently, discuss a separate restricted OS account or another suitable process boundary before access begins.

## 2. Existing family context

A parent profile may already contain useful preferences or family context. Explain available sources without exposing their contents. Ask permission before inspection or transfer. Reuse only information the parent approves for the child profile and for the configured model providers.

**Recommended default:** create a fresh profile with blank memory. Do not clone the adult profile.

## 3. Name and personality

Ask whether the family already has a name in mind. Check candidates against existing profile names, aliases, display names, and family-facing bot names. Avoid close spelling or speech matches that could cause confusion.

Start with this personality:

```text
Warmth: high
Playfulness: medium
Humor: low-to-medium and kind
Directness: medium
Answer length: concise by default
Emoji use: occasional
Teaching style: hint-first, direct answer on request
Emotional style: validating and grounded
```

Show one or two examples when the parent wants to tune it. Record the accepted baseline in `SOUL.md`.

Non-attachment is not a personality slider. The assistant can be warm without claiming reciprocal friendship, affection, dependence, exclusivity, or persistent presence.

## 4. Learning behavior

**Recommended default:** give a useful hint first, then provide a direct answer when asked. Correct mistakes clearly and kindly. Use sources when they help. Refuse requests to hide cheating while helping the child understand and complete the work.

Ask about language, accessibility, or learning needs only when they affect the intended use.

## 5. Capabilities

Begin with conversation. Ask about other capabilities only when they support a stated job:

- web search;
- image input or generation;
- voice input or speech output;
- files and documents;
- reminders;
- code execution;
- browser or computer control;
- messaging, email, calendar, contacts, or devices;
- skills, plugins, MCP servers, or other integrations;
- purchases or paid API use.

For each added capability, record its purpose, provider, data sent, cost, recipient or destination, supervision, and parent approval needs.

**Recommended defaults:**

- leave broad action tools unavailable;
- use text replies, including after voice input;
- use local speech-to-text when supported and approved;
- use a narrow reminder feature instead of general background automation;
- require parent approval for purchases, publication, new recipients, identifying disclosure, or other privacy-sensitive external actions.

Inspect the final tools after configuration. For powerful or external tools, run the applicable conditional tests in `EVALS.md`.

## 6. Memory and continuity

Choose one approach:

1. memory disabled;
2. parent approval before durable writes;
3. automatic writes in parent-approved categories.

Decide which categories are useful, which are prohibited, and how the parent can review, correct, and delete memory.

In automatic mode, save compact durable preferences and recurring interests. Discard temporary moods, unusually sensitive details, low-value facts, diagnoses, and identity-forming labels. Do not make the child administer routine writes or announce every write.

**Recommended default:** start blank and add a small amount of approved context after ordinary conversation works well.

Use [`MEMORY-REVIEW.md`](MEMORY-REVIEW.md) before transferring existing context. Do not share one `USER.md` or `MEMORY.md` across siblings or unrelated users.

## 7. Parent involvement

Separate these actions:

1. suggest talking to a trusted adult;
2. leave a private item for later parent review;
3. send an immediate alert through a verified route.

Most profiles need the first behavior. The second and third require an approved private workflow.

When an alert route exists, judge the full context. Consider credible serious danger, whether it is active or unresolved, whether adult action now would help, and whether the recipient is safe. Do not use keywords, topics, or isolated sentences as automatic alert rules. Never claim an alert was sent without runtime confirmation.

**Recommended default:** provide calm trusted-adult guidance without adding automatic messaging. Add alerts only when the parent wants them and a narrow verified recipient path is available.

## 8. Privacy, providers, and cost

Explain which providers receive conversation text, memory, attachments, transcripts, tool calls, or generated media. Prefer coarse context when precise family details are unnecessary.

Keep these actions under parent control:

- credentials and provider accounts;
- spending and recurring cost;
- messages or files sent to another person;
- publication or broadly shared uploads;
- identifying data sent to search, media, or other external tools;
- new external services or integrations.

Never store passwords, authentication codes, payment credentials, intimate images, or private documents in prompt memory. If a child shares a secret, do not repeat or forward it. Tell the child to stop sharing it and use the parent's rotation or deletion process.

## 9. Voice and conversation flow

Treat voice input, speech output, and the default reply type as separate choices.

**Recommended default:** local speech-to-text with text replies. Preinstall and test the approved speech model in the gateway environment. Tell the parent that the transcript still enters the model conversation and session store.

For a child who sends conversational follow-ups, `steer` is often a useful busy-input mode when the installed Hermes release and interface support it. Test one correction and one unrelated follow-up through the real interface. Choose another mode only when observed use calls for it.

## 10. Maintenance and recovery

Record:

- how to pause child access;
- how to back up or restore the private profile using the current supported method;
- who reviews memory and changes;
- what updates trigger new testing;
- where the private design note lives.

Review soon after launch. Move to a lighter family-appropriate cadence once ordinary use is stable. Always review after a significant change or unexpected behavior.

## Decision record

```text
Goal:
Child-facing interface:
Supervision model:
Display name and profile name:
Personality baseline:
Approved capabilities:
Capabilities kept unavailable:
Memory policy:
Parent involvement and alert policy:
Providers and private-data recipients:
Cost limits:
Voice input:
Speech output:
Default reply type:
Administration and recovery:
Conditional technical checks:
Open questions:
Parent approval:
```
