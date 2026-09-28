# Assignment 9 - PyTest + HTML Reporting

## Objective
Create a Selenium PyTest automation framework with:
- Browser setup and teardown using a fixture.
- Multiple automated tests.
- HTML execution reports.
- Automatic screenshots whenever a test fails.

## Structure

```text
assignment_9_pytest_reporting/
├── tests/
│   └── test_saucedemo.py
├── reports/
├── conftest.py
├── requirements.txt
└── README.md
```

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Expected result:

```text
2 passed
```

## Failure Screenshot

If a test fails, `conftest.py` automatically saves a screenshot in:

```text
reports/screenshots/
```

This demonstrates failure evidence capture for the automation framework.
