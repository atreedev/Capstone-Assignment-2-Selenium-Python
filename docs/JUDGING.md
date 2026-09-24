# Judge Protocol

## Purpose

The judge is meant to prevent the project from turning into a pile of code that merely happens to execute.

We will evaluate every iteration on:

1. Correctness
2. Architecture
3. Maintainability
4. Test quality
5. Requirement coverage
6. Evidence

## Scoring model

The included structural judge uses 100 points:

- Structure/separation: 10
- WebDriver factory: 10
- POM: 15
- Configuration: 10
- CSV data: 10
- PyTest login/search: 15
- unittest: 10
- Failure screenshots: 10
- HTML reporting: 5
- Documentation/maintainability: 5

This is **not** the final runtime quality score. A feature can be structurally present but still fail against the live website. Browser execution evidence supersedes static assumptions.

## Iteration review format

For each feature we will record:

```text
Feature:
Acceptance criterion:
Files involved:
What the code does:
Why it is designed this way:
Test executed:
Observed result:
Defect(s):
Fix:
Judge score:
What you should understand before moving on:
```

## Runtime defect policy

A failed test is not automatically a framework defect. During runtime review, distinguish:

- **Framework defect:** the automation cannot perform or observe the intended interaction correctly.
- **Test-oracle defect:** the automation performs the interaction correctly, but the assertion encodes an assumption the application does not guarantee.
- **Environment/site defect:** browser, network, third-party advertisements, or the public demo site interferes with execution.

The v1.2 product-search correction is a test-oracle fix: the browser successfully searched and returned products, but the original assertion incorrectly required every returned name to contain the literal search string.

## Zero-error interpretation

No software system can truthfully guarantee that an external website will never change or that a remote browser session will never experience an infrastructure failure. The engineering standard here is therefore:

- deterministic code where possible;
- explicit waits instead of arbitrary sleeps;
- stable selectors;
- configuration isolation;
- failure artifacts;
- repeatable commands;
- validation before declaring completion.
