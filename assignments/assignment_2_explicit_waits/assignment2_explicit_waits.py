from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    ).click()

    result = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    assert result.text == "Hello World!"
    print("Assignment 2 PASSED")
    print("Result:", result.text)

finally:
    driver.quit()
