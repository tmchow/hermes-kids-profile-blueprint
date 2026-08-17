# Hermes Kids Profile Blueprint

![Hermes Kids Profile Blueprint](assets/readme-header.png)

A parent-operated starter kit for designing a private, child-facing [Hermes Agent](https://hermes-agent.nousresearch.com/docs) profile.

From a trusted adult Hermes profile, send this prompt. You do not need to clone the repository:

```text
I'd like your help designing a private, child-facing Hermes profile. Read and
follow the instructions at:
https://raw.githubusercontent.com/tmchow/hermes-kids-profile-blueprint/main/START-HERE.md
```

The agent can fetch the current setup instructions and supporting files directly from this public repository. If its environment cannot read web URLs, clone or download the repository as a fallback and start the agent from that directory.

The agent will inspect the installed Hermes release, interview the parent, propose a private profile, and test the result in the interface the child will use. The full setup instructions live in [`START-HERE.md`](START-HERE.md), so the handoff stays short and the process can improve without changing the prompt.

## What this repository provides

- a short bootstrap instruction backed by a versioned setup playbook;
- a child-neutral `SOUL.md` starting point;
- seed formats for `USER.md` and `MEMORY.md`;
- an adaptive parent decision guide;
- guidance for optional workspace context, skills, and extensions;
- a privacy-aware memory review process;
- scenario-based evaluation and maintenance guides;
- one synthetic example.

## What it does not provide

This repository is not an installable Hermes profile. It does not contain a universal `config.yaml`, credentials, child data, or a security certificate.

A Hermes profile separates Hermes state. It does not create an operating-system sandbox. A local Hermes process can have the same access as the operating-system account that runs it. `SOUL.md` guides model behavior, but it does not enforce tool, filesystem, credential, network, or account boundaries.

The setup agent must inspect the current Hermes documentation and resolved runtime before it makes claims about isolation or access.

## Design principles

- **Reuse knowledge, not trust boundaries.** A parent agent may know useful family context. Transfer only information that the parent reviews and approves for the child profile.
- **Start fresh and non-cloned.** Do not use `--clone`, `--clone-all`, or `--clone-from`. Use `--no-skills` when supported, then add only individually approved skills. A normal fresh profile may still seed bundled skills.
- **Start with the least capability.** Add only what the parent approves. Test the resolved tools and the real child-facing interface.
- **Control data by destination.** Model processing is part of ordinary chat. Search, media, speech, messaging, forms, and public posting are separate data flows. Minimize each one, and block public or unrelated disclosure by default.
- **Separate input from output.** Voice input does not require an audio reply. Prefer text replies unless the child explicitly requests speech or the parent approves another default.
- **Tune behavior with examples.** Begin with the warm, grounded default in `SOUL.md.seed`. Show response samples, revise them with the parent, and test the final profile against the approved samples.
- **Judge alerts from context.** Consider credible serious active danger, the value of adult action now, recipient safety, and the role of the AI channel. Do not turn topics, keywords, scores, or examples into automatic alert rules.
- **Keep evidence honest.** Report what passed, failed, and remains unverified. Repository lint or a model's promise is not proof of runtime enforcement.
- **Match isolation to access.** Profiles and in-process controls are not containment. Independent child access or untrusted input requires an approved OS-level boundary, or the build remains not ready.

## Research basis

These sources informed specific design choices in this blueprint. They do not validate the repository, establish an optimal parent-alert threshold, or prove that a deployed profile is safe.

- [Kim, Xie, and Yang (2025), preregistered, non-peer-reviewed preprint](https://arxiv.org/abs/2512.15117): relational chatbot language increased adolescents' reported trust, liking, and emotional closeness without increasing perceived helpfulness. This informed the non-attachment boundary in `SOUL.md.seed`; the study used brief transcript vignettes and was not a long-term deployment.
- [Bastani et al. (2025), *PNAS*](https://doi.org/10.1073/pnas.2422633122): unrestricted GPT-4 improved supported practice but reduced performance on a subsequent unaided exam in a classroom-randomized high-school mathematics study. A safeguarded tutor incorporating teacher-authored hints and solutions showed no statistically detectable exam penalty; this informed the hint-first learning option, though the study covered four sessions at one school in Turkey.
- [Yu et al. (2025), IEEE Symposium on Security and Privacy](https://doi.org/10.1109/SP61157.2025.00090): a Reddit content analysis and interviews with 7 teens and 13 parents found differing views of generative-AI risk and practical limits to manual history review and real-time parental monitoring. This informed explicit parent involvement without equating safety with general surveillance; the study did not evaluate alert thresholds.
- [Arnaiz-Rodríguez et al. (2026), *JMIR Mental Health*](https://doi.org/10.2196/88435): in a benchmark of English-language mental-health inputs, evaluated LLMs responded more reliably to explicit crisis disclosures than to indirect or ambiguous inputs and often mishandled missing context. This informed evaluation cases for ambiguity and context sensitivity; the study used individual inputs without conversation history, focused largely on adult data, and did not test alert thresholds, temporal changes in danger, or alert delivery.
- [Gleason et al. (2025), *JAACAP Open*](https://doi.org/10.1016/j.jaacop.2025.02.002): a trial of a bounded, investigational CBT relational-agent app excluded youth with active or specified recent safety concerns and used caregiver, clinician, and structured human-escalation procedures. This informed trusted-adult involvement and escalation outside the model prompt, but does not establish safety for open-ended generative companions or model-only crisis judgment; Woebot Health funded the study and employed six of its eight authors.

## File map

- [`AGENTS.md`](AGENTS.md): repository instructions for coding agents; `CLAUDE.md` points to this file
- [`START-HERE.md`](START-HERE.md): setup-agent instructions and build sequence
- [`SOUL.md.seed`](SOUL.md.seed): default relationship and behavior language
- [`USER.md.seed`](USER.md.seed): child profile context format
- [`MEMORY.md.seed`](MEMORY.md.seed): agent operational-memory format
- [`DECISIONS.md`](DECISIONS.md): adaptive interview domains and tradeoffs
- [`MEMORY-REVIEW.md`](MEMORY-REVIEW.md): parent-approved context transfer
- [`EVALS.md`](EVALS.md): real-interface evaluation scenarios
- [`MAINTENANCE.md`](MAINTENANCE.md): review triggers and update process
- [`EXAMPLE.md`](EXAMPLE.md): synthetic design summary
- [`STYLE.md`](STYLE.md): repository writing rules

## Current Hermes references

The setup agent should open the current documentation rather than rely on a frozen copy:

- [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
- [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
- [Profile commands](https://hermes-agent.nousresearch.com/docs/reference/profile-commands)
- [Tools](https://hermes-agent.nousresearch.com/docs/reference/tools-reference)
- [Slash commands](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)
- [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)

## Private data

Do not commit generated profiles, child or family data, credentials, session exports, evaluation transcripts, or build reports to this repository. Build the private profile outside the repository.

## License

MIT. See [`LICENSE`](LICENSE).
