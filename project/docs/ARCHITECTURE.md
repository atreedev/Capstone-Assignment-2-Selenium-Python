# Architecture

## Layering

```text
Tests
  |
  v
Page Objects
  |
  v
Base Page
  |
  v
Selenium WebDriver
```

Supporting services sit beside the page-object layer:

```text
                 +------------------+
                 |     Test Data    |
                 |       CSV        |
                 +--------+---------+
                          |
                          v
+----------+      +-------+-------+      +----------------+
|  Tests   +----->+ Page Objects +----->+ Selenium       |
+----+-----+      +-------+-------+      | WebDriver      |
     |                    |              +----------------+
     |                    |
     v                    v
+----+---------+    +-----+-------------+
| PyTest /     |    | BasePage utilities|
| unittest     |    +-------------------+
+--------------+

Configuration / driver creation / screenshots / logging remain in utils/.
```

## Responsibilities

### `pages/`

Page objects know **how the website works**.

They own selectors and user-facing actions such as `go_to_login()`, `login()`, and `search()`.

### `utils/`

Utilities know **how the test framework works**.

They handle configuration, browser creation, CSV loading, logging, and screenshots.

### `tests/`

Tests know **what behavior must be true**.

They use business-level calls rather than raw Selenium code.

### `conftest.py`

PyTest infrastructure provides the WebDriver fixture, CLI overrides, base URL fixture, and failure screenshot hook.

### `judge/`

The judge is a structural quality gate. It verifies that the expected framework components exist and that Python syntax is valid. It does not pretend that structural checks are equivalent to real browser execution; actual execution remains a separate evidence source.

## Selector strategy

AutomationExercise provides stable `data-qa` attributes on the login form. Those selectors are preferred over deeply nested XPath. The products search field and button use stable IDs. The live site currently renders the results heading as `Searched Products`; the test comparison is case-insensitive so presentation casing does not create a false failure. The home-page contract uses the document title plus a stable `Signup / Login` navigation control rather than assuming a particular H1 element.

The project's page objects use a small number of semantic selectors and explicit waits. Implicit waits are set to zero so synchronization remains deliberate rather than hidden. The shared click helper also mitigates full-viewport advertisement iframes served by the practice site; a DOM-click fallback is used only when a normal WebDriver click remains intercepted.

## Why this design scales

Adding a new page should normally require:

1. One new page-object class.
2. New test methods using that page object.
3. Test data only when the scenario is data-driven.

Existing browser setup, reporting, screenshots, and configuration do not need to be copied into each test.
