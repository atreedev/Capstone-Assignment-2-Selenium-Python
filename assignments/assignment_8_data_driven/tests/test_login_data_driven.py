import csv
from pathlib import Path

import pytest
from selenium import webdriver

from pages.login_page import LoginPage


def load_test_data():
    csv_file = Path(__file__).resolve().parents[1] / "test_data.csv"
    with csv_file.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("data", load_test_data())
def test_login_data_driven(driver, data):
    page = LoginPage(driver)
    page.open()
    page.login(data["username"], data["password"])

    expected = data["expected"]

    if expected == "success":
        assert "/inventory.html" in driver.current_url
    else:
        assert page.has_login_error()
