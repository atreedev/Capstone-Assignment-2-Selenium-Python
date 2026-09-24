from __future__ import annotations

from typing import Tuple

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import get_logger

Locator = Tuple[str, str]
LOGGER = get_logger(__name__)


class BasePage:
    """Common Selenium operations shared by all page objects."""

    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        self.driver = driver
        self.timeout = timeout

    @property
    def wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, self.timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: Locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def _deactivate_known_ad_overlays(self) -> None:
        """Prevent full-viewport Google ad iframes from intercepting test clicks.

        AutomationExercise serves third-party advertisement iframes. On some
        sessions these can temporarily cover a control and produce Selenium's
        ElementClickInterceptedException. We do not remove page content; we only
        disable pointer events on the known advertisement iframes.
        """
        script = """
        document.querySelectorAll("iframe[title='Advertisement'], iframe[id^='aswift_']")
            .forEach(function(frame) {
                frame.style.pointerEvents = 'none';
            });
        """
        try:
            self.driver.execute_script(script)
        except Exception as exc:
            LOGGER.debug("Unable to deactivate ad overlays: %s", exc)

    def click(self, locator: Locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element,
        )

        try:
            element.click()
            return
        except ElementClickInterceptedException:
            LOGGER.warning("Click intercepted for %s; retrying after ad-overlay mitigation", locator)

        self._deactivate_known_ad_overlays()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element,
        )

        try:
            element.click()
        except ElementClickInterceptedException:
            # Final fallback for a full-viewport overlay that remains in the
            # compositor even after pointer events were disabled.
            LOGGER.warning("Normal retry still intercepted for %s; using DOM click fallback", locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator: Locator, value: str, clear_first: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            element.clear()
        element.send_keys(value)

    def get_text(self, locator: Locator) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def is_visible(self, locator: Locator) -> bool:
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def wait_for_url_contains(self, fragment: str) -> None:
        self.wait.until(EC.url_contains(fragment))

    def get_current_url(self) -> str:
        return self.driver.current_url

    def page_title(self) -> str:
        return self.driver.title

    def refresh(self) -> None:
        self.driver.refresh()
