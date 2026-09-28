from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # https://the-internet.herokuapp.com/javascript_alerts
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # 1. JavaScript Alert -> Accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert"
    alert.accept()

    # 2. JavaScript Confirm -> Dismiss
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()

    # 3. JavaScript Prompt -> Enter text and accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Selenium Assignment")
    alert.accept()

    print("Alert handling PASSED")
    print("Confirm handling PASSED")
    print("Prompt handling PASSED")
    print("Assignment 4 PASSED")

finally:
    driver.quit()
