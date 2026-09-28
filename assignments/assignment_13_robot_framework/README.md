# Assignment 13 - Robot Framework

## Objective
Demonstrate basic Robot Framework automation with Selenium, API testing,
variables, data-driven values, custom Python keywords, assertions,
setup/teardown, tags, and generated reports.

## Structure

```text
assignment_13_robot_framework/
├── tests/
│   └── automation.robot
├── libraries/
│   └── CustomKeywords.py
├── requirements.txt
└── README.md
```

## Requirements Demonstrated

### Browser automation
Uses SeleniumLibrary to:
- Open Chrome
- Navigate to SauceDemo
- Enter username/password
- Click Login
- Verify the Products page

### Variables / test data
Credentials, browser, URL and API ID are stored as Robot variables.

### Custom Python keyword
`Add Numbers` is implemented in `libraries/CustomKeywords.py`.

### Assertions
Uses:
- `Title Should Be`
- `Page Should Contain`
- `Should Be Equal As Integers`
- `Should Be Equal As Strings`

### Setup / Teardown
Every test opens the browser and logs in before execution, then closes browsers afterward.

### Tags
Tests use tags such as:
- `smoke`
- `ui`
- `python`
- `api`

Examples:

```bash
robot --include smoke tests/
robot --include api tests/
robot --exclude api tests/
```

### Reports and logs
Robot Framework automatically creates:

```text
report.html
log.html
output.xml
```

### Parallel execution
Install Pabot:

```bash
pip install pabot
```

Run tests in parallel:

```bash
pabot --processes 2 tests/
```

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
robot tests/
```

Expected: all 3 test cases pass.

Note: ChromeDriver/browser compatibility is handled by Selenium Manager in modern Selenium versions.
