# Assignment 7 - Page Object Model (POM)

## Objective
Restructure Selenium automation using the Page Object Model.

## Structure

```text
assignment_7_pom/
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   └── test_login.py
├── requirements.txt
└── README.md
```

## POM Requirements Demonstrated

- Page classes contain locators and UI interaction methods.
- Test code uses the page objects.
- Assertions are kept in the test file.
- Browser setup/teardown uses a PyTest fixture.

## Run

```bash
pip install -r requirements.txt
pytest -v
```

Expected result:

```text
1 passed
```
