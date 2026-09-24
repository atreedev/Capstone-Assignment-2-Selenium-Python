from __future__ import annotations

import configparser
import os
from pathlib import Path
from typing import Optional


class ConfigManager:
    """Reads project configuration with environment-variable overrides."""

    ENV_MAP = {
        "base_url": "BASE_URL",
        "browser": "BROWSER",
        "headless": "HEADLESS",
        "timeout": "SELENIUM_TIMEOUT",
        "page_load_timeout": "PAGE_LOAD_TIMEOUT",
        "test_email": "TEST_EMAIL",
        "test_password": "TEST_PASSWORD",
        "report_dir": "REPORT_DIR",
        "html_report": "HTML_REPORT",
        "screenshot_dir": "SCREENSHOT_DIR",
        "screenshot_on_failure": "SCREENSHOT_ON_FAILURE",
    }

    def __init__(self, path: Optional[str] = None) -> None:
        project_root = Path(__file__).resolve().parents[1]
        self.path = Path(path) if path else project_root / "config" / "config.ini"
        self.parser = configparser.ConfigParser()
        if not self.path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.path}")
        self.parser.read(self.path, encoding="utf-8")

    def _read(self, section: str, option: str, default: str = "") -> str:
        env_name = self.ENV_MAP.get(option)
        if env_name:
            env_value = os.getenv(env_name)
            if env_value is not None and env_value != "":
                return env_value
        return self.parser.get(section, option, fallback=default)

    def get_base_url(self) -> str:
        return self._read("application", "base_url").rstrip("/") + "/"

    def get_browser(self) -> str:
        return self._read("application", "browser", "chrome").lower().strip()

    def is_headless(self) -> bool:
        return self._read("application", "headless", "false").lower() in {"1", "true", "yes", "y"}

    def get_timeout(self) -> int:
        return int(self._read("application", "timeout", "15"))

    def get_page_load_timeout(self) -> int:
        return int(self._read("application", "page_load_timeout", "30"))

    def get_test_email(self) -> str:
        return self._read("credentials", "test_email").strip()

    def get_test_password(self) -> str:
        return self._read("credentials", "test_password").strip()

    def get_report_dir(self) -> Path:
        return Path(self._read("reporting", "report_dir", "reports"))

    def get_html_report(self) -> Path:
        return Path(self._read("reporting", "html_report", "reports/html/report.html"))

    def get_screenshot_dir(self) -> Path:
        return Path(self._read("reporting", "screenshot_dir", "reports/screenshots"))

    def screenshot_on_failure(self) -> bool:
        return self._read("application", "screenshot_on_failure", "true").lower() in {"1", "true", "yes", "y"}
