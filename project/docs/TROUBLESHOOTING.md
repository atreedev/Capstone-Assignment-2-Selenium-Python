# Troubleshooting

## `ModuleNotFoundError: selenium`

Activate the virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

## Selenium cannot create the browser

Confirm that Chrome/Chromium, Firefox, or Edge is installed and that the selected browser matches `config/config.ini` or `--browser`.

Selenium Manager normally downloads/locates the driver automatically. Corporate proxy/firewall restrictions can prevent this.

## Valid login is skipped

That is intentional when no credentials are configured.

Set:

```text
TEST_EMAIL
TEST_PASSWORD
```

as environment variables and rerun.

## Screenshot missing after a failure

Failure screenshots require the failing test to use the `driver` fixture. The hook never masks the original assertion failure.

## HTML report not generated

Confirm `pytest-html` is installed:

```bash
python -m pip show pytest-html
```

Then run:

```bash
python run_tests.py
```

## `ElementClickInterceptedException` caused by an advertisement iframe

AutomationExercise can display full-viewport third-party advertisement iframes such as `iframe#aswift_*`. These can cover a button even though Selenium reports the button itself as clickable. The shared `BasePage.click()` method first attempts a normal WebDriver click, then disables pointer events on the known ad iframes and retries. A DOM-click fallback is used only when the browser compositor still reports the overlay.
