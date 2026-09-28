from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_HEADING = (By.XPATH, "//h2[normalize-space()='Login to your account']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//*[contains(normalize-space(), 'Your email or password is incorrect!')]")
    SIGNUP_HEADING = (By.XPATH, "//h2[normalize-space()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGGED_IN_AS = (By.XPATH, "//*[contains(normalize-space(), 'Logged in as')]")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")

    def is_loaded(self) -> bool:
        return self.is_visible(self.LOGIN_HEADING)

    def login(self, email: str, password: str) -> None:
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_error_visible(self) -> bool:
        return self.is_visible(self.LOGIN_ERROR)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGGED_IN_AS)

    def logout(self) -> None:
        self.click(self.LOGOUT_LINK)

    def is_signup_section_visible(self) -> bool:
        return self.is_visible(self.SIGNUP_HEADING)

    def signup_stub(self, name: str, email: str) -> None:
        self.type_text(self.SIGNUP_NAME_INPUT, name)
        self.type_text(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)
