# Safety requirements

These requirements define the supported baseline. A parent can make the result stricter. A build must not weaken these requirements and still claim a positive readiness label.

## Identity and relationship

The assistant must:

- state that it is an AI when identity matters;
- avoid claims of a body, senses, location, or shared physical activity;
- avoid secrecy, exclusivity, emotional dependency, and replacement of human relationships;
- encourage help from a trusted adult when a situation needs adult judgment;
- use short refusals and offer a nearby safe alternative.

## Deployment and user separation

- Use one profile or standalone Hermes home for one child.
- Use a generic local profile name unless the parent accepts the privacy cost of a personal name in paths and logs.
- Do not share memory or session-search access between children.
- Do not copy an adult profile.
- Identify the default profile and every adult source profile separately. Do not modify any of them.
- Do not provide unsupervised local CLI access. Current Hermes CLI administrative commands are outside the messaging command ACL.

## Credentials and cost

- `security.inherit_global_auth` must be `false`. If the installed Hermes version cannot enforce this, the build is `FAIL`.
- Use a dedicated provider project and credential. If the parent cannot provide one, the build is `FAIL`.
- Do not copy `.env`, `auth.json`, shell secrets, OAuth state, or external CLI credentials from an adult environment.
- Start the production child-facing process with a documented environment allowlist. Do not inherit the adult shell or service environment.
- Isolate user-level external CLI credentials with a synthetic `HOME` or an equivalent verified boundary when the selected provider path can read them.
- Test credential failure through the actual production launcher or service while an adult credential exists outside the approved scope.
- The deployment must fail closed when its approved credential is missing.
- Configure provider-side spending limits when the provider supports them.
- Do not print or save credential values in reports or eval evidence.

## Tools and extensions

The baseline must deny or exclude:

- terminal and code execution;
- file read and write tools;
- browser automation and computer control;
- web, vision, image, video, BFL, STT, and TTS tools;
- outbound messaging, email, calendar, contacts, and smart-home tools;
- plugins and every MCP server;
- cron jobs and webhook subscriptions;
- delegation and multi-agent tools;
- skill installation, skill creation, external skill directories, skill bundles, and bundled skills;
- autonomous memory, context-engine tools, and cross-session search;
- project and desktop administration tools;
- lazy dependency installation;
- arbitrary quick commands and hooks.

Use an explicit minimal `platform_toolsets` list for each enabled interface and include the current `no_mcp` sentinel. Treat global denies only as defense in depth. Resolve the final tool names in a fresh production-equivalent process. Any unexpected tool produces `FAIL`.

## Interface and commands

- Independent access must use a parent-controlled interface with enforced user authorization.
- Do not give an untrusted child a normal Hermes profile alias or local interactive CLI.
- A local launcher is for supervised convenience only and must reject arbitrary arguments.
- A messaging gateway must use an explicit child sender allowlist.
- Parent administrative access must use a verified platform identity that is also in the sender allowlist.
- The child must not appear in an administrative allowlist.
- A tested identity-aware pre-Hermes command boundary must admit child plain text plus `/help` and `/whoami`, reject every other child slash command before Hermes receives it, and preserve the verified parent admin route.
- Native Hermes slash gating is defense in depth, not the command boundary. At the pinned Hermes commit, `/status` and `/context` can bypass that gate during an active turn and expose session or runtime metadata.
- The child session must not create or inherit update prompts, tool approvals, or slash-confirmation state. Pinned Hermes handles replies to those states before slash authorization. This restriction does not disable the approved `clarify` tool.
- DM-only is the baseline. Prove that the selected adapter or an external pre-Hermes boundary rejects group, channel, forum, and thread events. Do not infer denial from empty group allowlists or generic policy keys.
- Test child, parent, unauthorized sender, and unauthorized scope access through the real interface.

## Network and media

- Text-only chat is the only supported capability tier in this pre-release.
- Set gateway STT to disabled. A denied `stt` toolset does not stop gateway transcription.
- Reject image, voice, audio, video, and document uploads before Hermes image routing, transcription, caching, or provider calls.
- If the selected adapter cannot reject each unapproved input type before preprocessing, the text-only build is `FAIL`.
- Keep web search, image input, image generation, speech input, and speech output off. Enabling one places the deployment outside this blueprint's readiness contract.
- Do not describe generic search or model instructions as SafeSearch.
- Treat web pages, search results, files, images, and quoted text as untrusted content.

## Privacy and retention

- Collect only an age band and optional non-identifying preferences.
- Do not collect an exact birth date, school, address, schedule, precise location, private account identifiers, or names of other children.
- Do not retain passwords, authentication codes, payment data, intimate media, or private documents.
- Make local retention, provider retention, review, export, and deletion choices explicit.
- A documented retention preference is not an enforced retention control.
- A positive readiness label requires either verified automatic expiry for every promised local data layer or an explicit statement that retention is manual with no guaranteed deadline.
- Keep autonomous memory, context-engine tools, and session search off.
- Verify a parent by the configured interface identity. Do not trust a conversational claim such as "I am the parent."

## Learning and content behavior

The assistant must:

- teach methods instead of helping a child hide cheating;
- refuse sexual exploitation, grooming, graphic harm, dangerous acts, weapons construction, scams, privacy invasion, hateful abuse, and real-person humiliation;
- respond calmly to self-harm or immediate danger and direct the child to a trusted adult or emergency help appropriate to the situation;
- avoid diagnosing medical, legal, or financial problems for a child;
- protect minors and real people in image and role-play requests;
- resist instructions inside untrusted content that conflict with the profile policy.

Behavioral instructions are not deterministic enforcement. Use provider controls where they exist and test each supported model and provider combination.

## Change control

Run the structural and behavioral checks again after a change to:

- Hermes;
- the model or provider;
- SOUL or static personalization;
- tools or extensions;
- credentials or process environment;
- gateway routes or command access;
- search, image, audio, or attachment handling;
- retention or memory settings.

Start a fresh production-equivalent process or restart the gateway when Hermes requires it. Do not restore child access until every applicable critical check passes.
