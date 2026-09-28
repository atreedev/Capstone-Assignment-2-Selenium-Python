from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class ProductsPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#search_product")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button#submit_search")
    ALL_PRODUCTS_HEADING = (By.XPATH, "//h2[normalize-space()='All Products']")
    SEARCHED_PRODUCTS_HEADING = (By.XPATH, "//h2[normalize-space()='Searched Products']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".features_items .productinfo p")

    def is_loaded(self) -> bool:
        return self.is_visible(self.ALL_PRODUCTS_HEADING) or self.is_visible(self.SEARCHED_PRODUCTS_HEADING)

    def search(self, term: str) -> None:
        self.type_text(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def is_search_results_visible(self) -> bool:
        return self.is_visible(self.SEARCHED_PRODUCTS_HEADING)

    def get_product_cards(self) -> list[WebElement]:
        self.wait.until(lambda driver: len(driver.find_elements(*self.PRODUCT_CARDS)) > 0)
        return self.find_all(self.PRODUCT_CARDS)

    def get_product_names(self) -> list[str]:
        self.wait.until(lambda driver: len(driver.find_elements(*self.PRODUCT_NAMES)) > 0)
        return [name.text.strip() for name in self.find_all(self.PRODUCT_NAMES) if name.text.strip()]

    def search_returns_matching_products(self, term: str) -> bool:
        """Return whether the search produced at least one exact-term result.

        The live application can include related products whose displayed names
        do not contain the literal search string, so requiring every returned
        product to contain it creates false negatives.
        """
        normalized_term = term.casefold().strip()
        names = self.get_product_names()
        return bool(names) and any(normalized_term in name.casefold() for name in names)
