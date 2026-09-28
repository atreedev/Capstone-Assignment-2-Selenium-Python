# Capstone Assignment 2 — Selenium Python Automation Framework

Framework revision: 1.1

Target application: **https://automationexercise.com/**

This project implements the requirements from the Capstone Assignment 2 specification:

- Selenium WebDriver
- Python
- PyTest
- unittest
- Page Object Model (POM)
- Utility classes
- Configuration management
- CSV test data
- Screenshots on failure
- HTML reporting

The core business scenario automated here is:

1. Launch browser
2. Navigate to AutomationExercise
3. Verify the home page
4. Open Signup / Login
5. Verify the login page
6. Validate login behavior
7. Open Products
8. Search for a product
9. Verify `SEARCHED PRODUCTS`
10. Verify returned product names contain the search term

The framework is intentionally structured so that we can extend it later with cart, checkout, alerts, and other flows without rewriting the existing layers.

## Project structure

```text
Capstone_Assignment_2_AutomationExercise/
├── config/
│   └── config.ini
├── data/
│   └── test_data.csv
├── docs/
│   ├── ARCHITECTURE.md
│   ├── FEATURE_BACKLOG.md
│   ├── JUDGING.md
│   └── TROUBLESHOOTING.md
├── judge/
│   ├── __init__.py
│   └── judge.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── products_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login_pytest.py
│   ├── test_login_unittest.py
│   └── test_product_search_pytest.py
├── utils/
│   ├── __init__.py
│   ├── config_manager.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_tests.py
├── test_data_example.env
└── .gitignore
```

## 1. Requirements

Recommended local setup:

- Python 3.10+
- Google Chrome or Chromium
- Internet access to `automationexercise.com`

The framework uses Selenium Manager, so a manually downloaded ChromeDriver is normally not required.

## 2. Installation

From the project root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Then:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Configure login credentials

The valid-login test requires an account that exists on AutomationExercise. Do **not** commit a real password to Git.

Preferred method: environment variables.

PowerShell example:

```powershell
$env:TEST_EMAIL="your_test_email@example.com"
$env:TEST_PASSWORD="your_test_password"
```

CMD example:

```cmd
set TEST_EMAIL=your_test_email@example.com
set TEST_PASSWORD=your_test_password
```

Alternatively, put values in `config/config.ini` locally. The committed file intentionally leaves them blank.

The invalid-login test does not need a real account.

## 4. Run tests

Run all PyTest tests and generate the HTML report:

```bash
python run_tests.py
```

Or directly:

```bash
python -m pytest -v
```

The configured PyTest report is written to:

```text
reports/html/report.html
```

Failure screenshots are written to:

```text
reports/screenshots/
```

Run only search tests:

```bash
python -m pytest tests/test_product_search_pytest.py -v
```

Run only login tests:

```bash
python -m pytest tests/test_login_pytest.py -v
```

Run the unittest module directly:

```bash
python -m unittest tests.test_login_unittest -v
```

Run the project judge:

```bash
python judge/judge.py
```

## 5. Browser configuration

`config/config.ini` controls the defaults. CLI options override those defaults:

```bash
python -m pytest --browser=chrome --headless=true -v
```

Supported values are `chrome`, `firefox`, and `edge`, provided the corresponding browser is installed.

## 6. Design principles

The test files should read like business scenarios. They should not contain raw Selenium selectors or low-level WebDriver implementation details.

Selectors and UI behavior belong in page objects. The home-page load contract uses the live site title plus a stable navigation element, and the shared click utility contains a narrowly scoped mitigation for the site's advertisement iframes.

Browser setup belongs in `utils/driver_factory.py` and the PyTest fixtures.

Configuration belongs in `config/config.ini` plus environment-variable overrides.

Test data belongs in CSV and is loaded via `utils/csv_reader.py`.

Reporting and failure screenshots are infrastructure concerns, not test-case logic.

## 7. Important test-account note

AutomationExercise's official test cases expect the tester to supply a valid existing account for the successful-login scenario. The framework therefore does not invent a permanent credential. Instead, it reads `TEST_EMAIL` and `TEST_PASSWORD` from the environment/configuration.

If valid credentials are absent, the successful-login test is skipped with a clear message rather than failing for a configuration problem.

## 8. What this first complete version covers

### Assignment requirements

| Requirement | Status |
|---|---|
| Selenium WebDriver | Implemented |
| Python | Implemented |
| PyTest | Implemented |
| unittest | Implemented |
| Page Object Model | Implemented |
| Utility classes | Implemented |
| Configuration management | Implemented |
| CSV test data | Implemented |
| Screenshots on failure | Implemented |
| HTML reporting | Implemented |
| Login automation | Implemented |
| Product search automation | Implemented |

### Planned extension candidates

- Cart page and cart verification
- Quantity update
- Popup/alert helper usage
- Checkout flow
- Data-driven login matrix
- Parallel execution
- CI pipeline
- Allure reporting as an optional extension

The extension list is deliberately kept separate from the required Assignment 2 baseline.
