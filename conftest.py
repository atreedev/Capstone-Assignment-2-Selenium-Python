from __future__ import annotations

from pathlib import Path
from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory
from utils.logger import get_logger
from utils.screenshot import capture_screenshot

LOGGER = get_logger(__name__)


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("automation")
    group.addoption("--browser", action="store", default=None, help="Browser override: chrome, firefox, edge")
    group.addoption("--headless", action="store", default=None, help="Headless override: true/false")
    group.addoption("--base-url", action="store", default=None, help="Application base URL override")


@pytest.fixture(scope="session")
def config(pytestconfig: pytest.Config) -> ConfigManager:
    return ConfigManager()


@pytest.fixture()
def driver(request: pytest.FixtureRequest, config: ConfigManager) -> Generator[WebDriver, None, None]:
    browser = request.config.getoption("--browser") or config.get_browser()
    headless_option = request.config.getoption("--headless")
    headless = config.is_headless() if headless_option is None else headless_option.lower() in {"1", "true", "yes", "y"}

    LOGGER.info("Starting browser=%s headless=%s", browser, headless)
    web_driver = DriverFactory.create_driver(browser=browser, headless=headless)
    web_driver.implicitly_wait(0)
    web_driver.set_page_load_timeout(config.get_page_load_timeout())
    yield web_driver
    LOGGER.info("Closing browser")
    web_driver.quit()


@pytest.fixture()
def base_url(request: pytest.FixtureRequest, config: ConfigManager) -> str:
    override = request.config.getoption("--base-url")
    return (override.rstrip("/") + "/") if override else config.get_base_url()


@pytest.fixture()
def test_data_path() -> Path:
    return Path(__file__).resolve().parent / "data" / "test_data.csv"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    config: ConfigManager | None = item.funcargs.get("config") if hasattr(item, "funcargs") else None
    if config is not None and not config.screenshot_on_failure():
        return

    web_driver = item.funcargs.get("driver") if hasattr(item, "funcargs") else None
    if web_driver is None:
        LOGGER.warning("No WebDriver fixture available; failure screenshot skipped for %s", item.nodeid)
        return

    try:
        directory = config.get_screenshot_dir() if config else Path("reports/screenshots")
        screenshot = capture_screenshot(web_driver, directory, item.name)
        if screenshot:
            LOGGER.info("Failure screenshot captured: %s", screenshot)
            report.user_properties.append(("failure_screenshot", str(screenshot)))
    except Exception as exc:  # reporting must never mask the original test failure
        LOGGER.exception("Unable to capture failure screenshot: %s", exc)
