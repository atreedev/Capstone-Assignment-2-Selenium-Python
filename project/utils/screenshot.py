from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


def capture_screenshot(driver: WebDriver, directory: Path, test_name: str) -> Optional[Path]:
    directory.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(char if char.isalnum() or char in "-_" else "_" for char in test_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    output = directory / f"{safe_name}_{timestamp}.png"
    if driver.get_screenshot_as_file(str(output)):
        return output
    return None
