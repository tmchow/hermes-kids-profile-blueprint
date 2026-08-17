# Documentation style

Use clear technical English that a parent can understand.

## Required style

- Use short, direct sentences.
- Use active voice.
- Put one main instruction in each sentence.
- Use the same term for the same item.
- Define a technical term before you use it.
- Put conditions before actions when that order prevents mistakes.
- Give exact commands and expected results when commands are stable.
- Separate facts, requirements, examples, and recommendations.
- Use `must` and `must not` only for mandatory rules.
- Use `can` for capability and `may` for permission.
- Do not use vague pronouns when the reader can misread the subject.

This style is inspired by ASD-STE100. The project does not claim formal ASD-STE100 conformance.

## Make the text approachable

- Explain the consequence of a security rule.
- Prefer plain words over security jargon.
- Do not scare the reader with abstract threats.
- Do not hide a real limitation behind friendly language.
- Use examples when an example prevents a likely mistake.

## Editing checks

Run two editing passes on every public document:

1. **No-AI-Slop pass:** Remove generic openings, fake contrasts, repeated summaries, puffery, decorative headings, robotic cadence, and unnecessary em dashes.
2. **Humanizer pass:** Make the text natural and readable without changing technical meaning.

After the humanizer pass, compare the result with the technical draft. Restore any requirement, command, configuration key, warning, or readiness result that remains part of the approved policy.

Do not let an editing tool weaken these terms:

- `must`
- `must not`
- `required`
- `unsupported`
- `verified`
- `unverified`
- `fail`

Do not rewrite code, commands, paths, configuration keys, placeholders, or expected output for style.
