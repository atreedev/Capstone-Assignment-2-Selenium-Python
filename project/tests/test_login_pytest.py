from __future__ import annotations

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_reader import CSVReader


def _credentials(config):
    email = config.get_test_email()
    password = config.get_test_password()
    return email, password


@pytest.mark.login
@pytest.mark.smoke
def test_login_page_is_reachable(driver, base_url):
    """Verifies the navigation and login-page contract without requiring credentials."""
    home = HomePage(driver, base_url)
    login = LoginPage(driver)

    home.open_home_page()
    assert home.is_loaded(), "Home page should be visible"
    home.go_to_login()

    assert "/login" in login.get_current_url(), "User should be on the login URL"
    assert login.is_loaded(), "Login heading should be visible"
    assert login.is_signup_section_visible(), "New User Signup should be visible"


@pytest.mark.login
def test_login_with_invalid_credentials(driver, base_url, test_data_path):
    """Official negative-login scenario using invalid credentials from CSV."""
    row = CSVReader.find_row(test_data_path, "product_search")

    home = HomePage(driver, base_url)
    login = LoginPage(driver)

    home.open_home_page()
    home.go_to_login()
    login.login(row["invalid_email"], row["invalid_password"])

    assert login.is_login_error_visible(), "Invalid-login error message should be visible"


@pytest.mark.login
def test_login_with_valid_credentials(driver, base_url, config):
    """Official positive-login scenario; skipped until a real test account is configured."""
    email, password = _credentials(config)
    if not email or not password:
        pytest.skip("Configure TEST_EMAIL and TEST_PASSWORD before running the valid-login test")

    home = HomePage(driver, base_url)
    login = LoginPage(driver)

    home.open_home_page()
    home.go_to_login()
    login.login(email, password)

    assert login.is_logged_in(), "A successful login should show 'Logged in as'"

    # Keep the test account clean for repeated local execution.
    login.logout()
    assert "/login" in login.get_current_url(), "Logout should return the user to the login page"
