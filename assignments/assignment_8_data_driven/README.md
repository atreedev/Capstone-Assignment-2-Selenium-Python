# Assignment 8 - Data-Driven Automation

## Objective
Run the same Selenium login test with multiple test cases stored in an external CSV file.

## Demonstrated
- External CSV test data
- `csv.DictReader`
- PyTest parameterization
- Valid and invalid login scenarios
- Reuse of a Page Object

## Structure

```text
assignment_8_data_driven/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_login_data_driven.py
├── test_data.csv
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
pytest -v
```

Expected result:

```text
4 passed
```
