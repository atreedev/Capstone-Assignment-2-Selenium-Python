import pytest
from pathlib import Path
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_runtest_makereport(item, call):
    """Capture a screenshot automatically whenever a test fails."""
    if call.when != "call" or call.excinfo is None:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    filename = screenshot_dir / f"{item.name}.png"
    driver.save_screenshot(str(filename))
    print(f"\nFailure screenshot saved to: {filename}")
