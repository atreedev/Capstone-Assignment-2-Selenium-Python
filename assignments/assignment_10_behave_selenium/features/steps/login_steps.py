from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I open the SauceDemo login page")
def step_open_login(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter the username "{username}"')
def step_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('I enter the password "{password}"')
def step_password(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)


@when("I click the login button")
def step_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("I should be on the inventory page")
def step_inventory(context):
    assert "/inventory.html" in context.driver.current_url


@then("I should see a login error")
def step_error(context):
    error = context.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error.is_displayed()
