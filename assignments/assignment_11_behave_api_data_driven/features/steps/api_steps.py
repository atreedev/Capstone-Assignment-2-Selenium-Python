import requests
from behave import when, then

BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

@when('I send a GET request for todo "{todo_id}"')
def step_send_get_request(context, todo_id):
    context.response = requests.get(BASE_URL + todo_id, timeout=10)

@then("the response status code should be {status_code:d}")
def step_check_status(context, status_code):
    assert context.response.status_code == status_code

@then("the response ID should be {todo_id:d}")
def step_check_id(context, todo_id):
    data = context.response.json()
    assert data["id"] == todo_id
