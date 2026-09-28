from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # ==========================================
    # Part 1: Iframe
    # ==========================================
    driver.get("https://the-internet.herokuapp.com/iframe")

    # Switch into the iframe using its ID.
    iframe = wait.until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )
    driver.switch_to.frame(iframe)

    editor = wait.until(
        EC.visibility_of_element_located((By.ID, "tinymce"))
    )
    editor.clear()
    editor.send_keys("Selenium Iframe Test")

    assert editor.text == "Selenium Iframe Test"
    print("Iframe interaction PASSED")

    # Return to the main page.
    driver.switch_to.default_content()

    # ==========================================
    # Part 2: New Window / Tab
    # ==========================================
    driver.get("https://the-internet.herokuapp.com/windows")

    original_window = driver.current_window_handle

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Click Here"))
    ).click()

    wait.until(lambda d: len(d.window_handles) == 2)

    # Switch to the newly opened window.
    new_window = next(
        handle for handle in driver.window_handles
        if handle != original_window
    )
    driver.switch_to.window(new_window)

    new_title = driver.title
    assert "New Window" in new_title
    print("New window title:", new_title)

    # Close the new window and return to the original.
    driver.close()
    driver.switch_to.window(original_window)

    assert driver.title == "Opening a new window"
    print("Window switching PASSED")
    print("Assignment 6 PASSED")

finally:
    driver.quit()
