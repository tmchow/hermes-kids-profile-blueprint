# Contributing

Contributions should make the blueprint easier to understand, safer to apply, or easier to verify.

## Before you change a requirement

1. Read `SECURITY.md` and `STYLE.md`.
2. State the failure mode that the change addresses.
3. Check current Hermes documentation and runtime behavior.
4. Keep examples free of names, schools, locations, account identifiers, and credentials.
5. Add or update an eval case when behavior changes.
6. Add or update a deterministic test when structure changes.

## Local checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_blueprint.py
python3 -m unittest discover -s tests -v
```

Run a No-AI-Slop pass and a humanizer pass on changed prose. Compare the edited text with the technical draft before you commit.

## Pull requests

Keep each pull request focused. Explain:

- what can fail today;
- what the pull request changes;
- how you tested it;
- which facts remain unverified.

Do not include real child data, family data, credentials, private transcripts, or local absolute paths.
