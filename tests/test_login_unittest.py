from __future__ import annotations

import unittest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory


class TestLoginPageWithUnittest(unittest.TestCase):
    """Small unittest layer proving the framework can also run with unittest."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.config = ConfigManager()
        cls.driver = DriverFactory.create_driver(
            browser=cls.config.get_browser(),
            headless=cls.config.is_headless(),
        )
        cls.driver.implicitly_wait(0)
        cls.driver.set_page_load_timeout(cls.config.get_page_load_timeout())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_login_page_contract(self) -> None:
        home = HomePage(self.driver, self.config.get_base_url(), self.config.get_timeout())
        login = LoginPage(self.driver, self.config.get_timeout())

        home.open_home_page()
        self.assertTrue(home.is_loaded())

        home.go_to_login()
        self.assertIn("/login", login.get_current_url())
        self.assertTrue(login.is_loaded())
        self.assertTrue(login.is_signup_section_visible())


if __name__ == "__main__":
    unittest.main(verbosity=2)
