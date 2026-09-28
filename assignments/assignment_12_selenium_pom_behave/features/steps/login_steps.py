from behave import given, when, then
from selenium import webdriver

from pages.login_page import LoginPage


@given("I open the SauceDemo login page")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@then("I should see the inventory page")
def step_inventory(context):
    assert context.login_page.is_inventory_page()


@then("I should see a login error")
def step_error(context):
    assert context.login_page.has_error()
