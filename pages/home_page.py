from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the AutomationExercise home page."""

    # The live site uses the document title "Automation Exercise". The previous
    # implementation looked for a non-existent/unstable H1 and caused false
    # negatives even when the home page had loaded successfully.
    HOME_TITLE = "Automation Exercise"
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    CART_LINK = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 15) -> None:
        super().__init__(driver, timeout)
        self.base_url = base_url

    def open_home_page(self) -> None:
        self.open(self.base_url)

    def is_loaded(self) -> bool:
        """Confirm the page title and a stable header navigation control are present."""
        try:
            self.wait.until(lambda driver: driver.title.strip() == self.HOME_TITLE)
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))
            return True
        except Exception:
            return False

    def go_to_login(self) -> None:
        self.click(self.LOGIN_LINK)

    def go_to_products(self) -> None:
        self.click(self.PRODUCTS_LINK)

    def go_to_cart(self) -> None:
        self.click(self.CART_LINK)
