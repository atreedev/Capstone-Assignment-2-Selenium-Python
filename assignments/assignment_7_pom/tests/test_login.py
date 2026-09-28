import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Assertions stay in the test, not inside the Page Object.
    assert "/inventory.html" in inventory_page.get_url()
    assert inventory_page.is_loaded()
