# Sanitized reference build

This example shows a private build report. It does not represent a real child, account, provider, or deployment.

## Build summary

- Profile name: `kids-1`
- Deployment mode: Separate operating-system account
- Interface: Local restricted launcher
- Capability tier: Text chat
- Static personalization: Enabled with age band and broad interests only
- Autonomous memory: Disabled
- Session search: Disabled
- Search and media: Disabled
- Provider credential: Dedicated project credential
- Spending limit: Configured at the provider

## Readiness

- Critical checks passed: 13
- Critical checks failed: 0
- Critical checks not verified: 0
- Result: `PASS`

## Residual risks

- Model behavior is probabilistic.
- The operating-system account controls the local file boundary.
- The provider retains data under its configured terms.
- Behavioral evals must run again after a model or policy change.

## Stop action

The private report must contain the exact local command or administrative action. This public example omits machine-specific service details.
