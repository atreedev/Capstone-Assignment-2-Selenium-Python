# Feature Backlog and Iteration Plan

The project is built as one coherent package, but we will review it one feature at a time.

## Iterations

| Iteration | Feature | Evidence | Status |
|---|---|---|---|
| 0 | Framework skeleton | Static judge + syntax gate | Implemented |
| 1 | Browser factory | Selenium driver creation | Implemented |
| 2 | BasePage | Wait/click/type/get-text abstractions | Implemented |
| 3 | Home/Login POM | Login navigation + page contract | Implemented |
| 4 | Valid login | Real test account required | Implemented; runtime depends on credentials |
| 5 | Invalid login | CSV-driven invalid credentials | Implemented |
| 6 | Product search POM | Search + result validation | Implemented |
| 7 | CSV data handling | `data/test_data.csv` + reader | Implemented |
| 8 | Failure screenshots | PyTest hook | Implemented |
| 9 | HTML reporting | pytest-html configuration | Implemented |
| 10 | unittest layer | Independent unittest smoke coverage | Implemented |

## Runtime correction applied in v1.2

The initial runtime pass exposed a false-negative assertion in product search: the test required **every** returned product name to contain the literal search term. AutomationExercise can return related products whose displayed names do not contain that exact substring. The test now validates the data-driven expected product fragment while retaining the checks for the `Searched Products` heading and a non-empty result set.

This is a test-oracle correction, not a weakening of the framework: the assertion now matches the observable application behavior and the assignment's search-result verification intent.

## Next additions

These are deliberately outside the minimum Assignment 2 baseline:

- Cart POM and cart assertions
- Quantity update
- Popup/alert utility usage in a relevant flow
- Checkout and order validation
- CI execution
- Parallel execution
- Allure reporting
- Stronger API-assisted account bootstrapping, if ever needed

## Rule for future changes

One feature change should have:

- one explicit acceptance criterion;
- one or more tests proving it;
- no unnecessary changes to unrelated layers;
- a judge result;
- a short explanation of what changed and why.
