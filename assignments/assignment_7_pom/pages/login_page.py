from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
