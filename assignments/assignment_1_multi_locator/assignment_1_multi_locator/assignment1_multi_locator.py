from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Selenium 4 automatically manages the ChromeDriver through Selenium Manager.
    driver = webdriver.Chrome()

    try:
        # Open the SauceDemo login page.
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        # Assignment requirement 1: username using By.ID
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        # Assignment requirement 2: password using By.NAME
        password = driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")

        # Assignment requirement 3: login button using By.XPATH
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()

        # Assignment validation: URL should contain /inventory.html
        assert "/inventory.html" in driver.current_url, (
            f"Login failed. Current URL: {driver.current_url}"
        )

        print("Assignment 1 PASSED")
        print(f"Current URL: {driver.current_url}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
