# Assignment 10 - Behave BDD with Selenium

## Objective
Demonstrate Browser automation using Selenium with the Behave BDD framework.

## Demonstrated
- Gherkin Feature file
- Given / When / Then steps
- Selenium browser automation
- Behave step definitions
- Scenario setup and teardown
- Assertions

## Structure

```text
assignment_10_behave_selenium/
├── features/
│   ├── login.feature
│   ├── environment.py
│   └── steps/
│       └── login_steps.py
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
behave
```

Expected result:

```text
2 features passed / 2 scenarios passed / all steps passed
```

The exact Behave summary formatting may vary by Behave version.
