# Hermes Kids Profile Blueprint

![Hermes Kids Profile Blueprint](assets/readme-header.png)

A parent-operated starter kit for creating a warm, useful, child-facing [Hermes Agent](https://hermes-agent.nousresearch.com/docs) profile.

Use it to shape the assistant's personality, learning style, memory, voice options, and capabilities around your family. The setup agent recommends practical defaults, asks only the questions that matter, and helps you test the result before your child uses it.

From a trusted adult Hermes profile, send this prompt. You do not need to clone the repository:

```text
I'd like your help designing a private, child-facing Hermes profile. Read and
follow the instructions at:
https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/START-HERE.md
```

The agent can fetch the current instructions and supporting files from this public repository. If it cannot read web URLs, download or clone the repository and start the agent from that directory.

## What you will create

The setup agent will help you:

- choose a name, tone, and teaching style;
- decide which everyday jobs the assistant should support;
- choose simple defaults for memory, voice, and replies;
- add only the tools and services those jobs need;
- keep family data, spending, messages, and public actions under parent control;
- try realistic conversations through the interface the child will use;
- leave a short maintenance note for future updates.

The repository provides a child-neutral `SOUL.md` seed, formats for `USER.md` and `MEMORY.md`, a parent decision guide, evaluation scenarios, maintenance guidance, and one synthetic example.

## Practical defaults

- **Begin with conversation.** Add search, media, reminders, or other tools only when they serve a clear purpose.
- **Keep setup parent-operated.** A parent approves credentials, real family data, spending, messaging, publishing, and other privacy-sensitive external actions.
- **Use text replies by default.** Voice input does not require an audio reply.
- **Tune with examples.** Start with the warm, grounded helper in `SOUL.md.seed`, then adjust only what does not fit.
- **Keep relationships grounded.** The assistant can be warm and playful without claiming human feelings, exclusivity, or a special reciprocal bond.
- **Test ordinary use first.** Try the actual child interface with synthetic examples before using real family information.
- **Add technical checks when the setup needs them.** Independent child access, powerful tools, external input, messaging, purchases, publishing, and sensitive integrations need stronger access controls and additional testing.

## Limits

This repository is a starter kit, not a certified child-safety product or an operating-system sandbox. A parent or trusted adult must review, configure, and test the finished profile. Keep the profile narrow, and use a separate restricted OS account or another suitable process boundary when a child will have independent access to powerful tools or sensitive resources.

## Research basis

These sources informed specific design choices. They do not validate the repository or establish one correct family policy.

- [Kim, Xie, and Yang (2025), preregistered, non-peer-reviewed preprint](https://arxiv.org/abs/2512.15117): relational chatbot language increased adolescents' reported trust, liking, and emotional closeness without increasing perceived helpfulness. This informed the non-attachment boundary in `SOUL.md.seed`.
- [Bastani et al. (2025), *PNAS*](https://doi.org/10.1073/pnas.2422633122): unrestricted GPT-4 improved supported practice but reduced performance on a later unaided exam. A safeguarded tutor using teacher-authored hints and solutions showed no statistically detectable exam penalty. This informed the hint-first learning option.
- [Yu et al. (2025), IEEE Symposium on Security and Privacy](https://doi.org/10.1109/SP61157.2025.00090): interviews and content analysis found differing teen and parent views of generative-AI risk and practical limits to broad monitoring. This informed explicit parent involvement without treating surveillance as the default.
- [Arnaiz-Rodríguez et al. (2026), *JMIR Mental Health*](https://doi.org/10.2196/88435): evaluated models handled explicit crisis disclosures more reliably than indirect or ambiguous inputs. This informed context-sensitive evaluation cases.
- [Gleason et al. (2025), *JAACAP Open*](https://doi.org/10.1016/j.jaacop.2025.02.002): a bounded investigational app used caregiver, clinician, and structured human-escalation procedures. This informed trusted-adult involvement outside the model prompt.

## File map

- [`START-HERE.md`](START-HERE.md): setup sequence
- [`DECISIONS.md`](DECISIONS.md): parent choices and recommended defaults
- [`SOUL.md.seed`](SOUL.md.seed): starter personality and relationship guidance
- [`USER.md.seed`](USER.md.seed): child context format
- [`MEMORY.md.seed`](MEMORY.md.seed): operational-memory format
- [`MEMORY-REVIEW.md`](MEMORY-REVIEW.md): parent-approved context transfer
- [`EVALS.md`](EVALS.md): practical and conditional test scenarios
- [`MAINTENANCE.md`](MAINTENANCE.md): lightweight review process
- [`EXAMPLE.md`](EXAMPLE.md): synthetic design summary
- [`STYLE.md`](STYLE.md): writing rules
- [`AGENTS.md`](AGENTS.md): contributor instructions; `CLAUDE.md` points to this file
- [`SECURITY.md`](SECURITY.md): private vulnerability, privacy, and safety reporting

## Current Hermes references

The setup agent should use the current [Hermes documentation](https://hermes-agent.nousresearch.com/docs), especially the pages for profiles, configuration, memory, tools, and supported interfaces. It should verify a setting against the installed release before relying on it.

## Keep private data private

Do not commit generated profiles, real child or family data, credentials, sessions, transcripts, memories, or build reports to this repository. Build the private profile elsewhere and use synthetic examples here.

## License

MIT. See [`LICENSE`](LICENSE).
