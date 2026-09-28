from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


class DriverFactory:
    """Creates a browser using Selenium Manager and consistent project settings."""

    @staticmethod
    def create_driver(browser: str = "chrome", headless: bool = False) -> WebDriver:
        browser = browser.lower().strip()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(options=options)

        if browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            return webdriver.Firefox(options=options)

        if browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            return webdriver.Edge(options=options)

        raise ValueError(f"Unsupported browser: {browser}. Use chrome, firefox, or edge.")
