# Assignment 12 - Selenium + POM + Behave

## Objective

Combine Selenium WebDriver, Page Object Model (POM), and Behave BDD.

## Structure

```text
assignment_12_selenium_pom_behave/
├── features/
│   ├── login.feature
│   ├── environment.py
│   └── steps/
│       └── login_steps.py
├── pages/
│   └── login_page.py
├── requirements.txt
└── README.md
```

## Demonstrated

- Gherkin feature file
- Behave step definitions
- Selenium WebDriver
- Page Object Model
- Centralized locators and page actions
- Scenario setup and teardown
- Assertions in step definitions

## Run

```bash
pip install -r requirements.txt
behave
```

Expected result:

```text
2 scenarios passed
```
