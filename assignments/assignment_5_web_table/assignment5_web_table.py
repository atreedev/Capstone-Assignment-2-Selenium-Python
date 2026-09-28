from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")

    wait = WebDriverWait(driver, 10)
    table = wait.until(
        EC.visibility_of_element_located((By.ID, "table1"))
    )

    target_name = "Jason Doe"
    target_row = None

    # Iterate through every row in the table.
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        values = [cell.text.strip() for cell in cells]

        if target_name in values:
            target_row = values
            break

    assert target_row is not None, f"{target_name} was not found"

    # Table 1 columns:
    # Last Name, First Name, Email, Due, Web Site, Action
    due_amount = target_row[3]
    website = target_row[4]

    print("Target row:", target_row)
    print("Due amount:", due_amount)
    print("Website:", website)
    print("Assignment 5 PASSED")

finally:
    driver.quit()
