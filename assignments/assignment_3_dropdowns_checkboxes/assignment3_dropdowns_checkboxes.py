from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 10)

    # -----------------------------
    # Part 1: Dynamic Autocomplete
    # -----------------------------
    driver.get("https://formy-project.herokuapp.com/autocomplete")

    address = wait.until(
        EC.visibility_of_element_located((By.ID, "autocomplete"))
    )
    address.send_keys("1600 Amphitheatre Parkway")

    # Select the matching autocomplete suggestion
    suggestion = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".pac-item")
        )
    )
    suggestion.click()

    assert "1600 Amphitheatre Parkway" in address.get_attribute("value")
    print("Autocomplete selection PASSED")

    # -----------------------------
    # Part 2: Checkboxes
    # -----------------------------
    driver.get("https://formy-project.herokuapp.com/checkbox")

    checkbox1 = wait.until(
        EC.element_to_be_clickable((By.ID, "checkbox-1"))
    )
    checkbox2 = wait.until(
        EC.element_to_be_clickable((By.ID, "checkbox-2"))
    )

    if not checkbox1.is_selected():
        checkbox1.click()

    if not checkbox2.is_selected():
        checkbox2.click()

    assert checkbox1.is_selected()
    assert checkbox2.is_selected()

    print("Checkbox selection PASSED")
    print("Assignment 3 PASSED")

finally:
    driver.quit()
