from behave import given, then, when
from helper_functions import *


@given("The API endpoint is turned on")
def step_API_turned_on(context):
    context.URL = "todos"
    assert isAPIRunning(context.URL)


@when("I send a GET request to the todo endpoint")
def step_send_GET_request(context):
    context.response = sendRequest("GET", context.URL)


@when("I send a GET request to an invalid endpoint")
def step_send_GET_request(context):
    context.response = sendRequest(
        "GET", "error", return_response_if_error=True)


@when("I send a POST request to the todo endpoint")
def step_send_POST_request(context):
    context.response = sendRequest("POST", context.URL, data=TEST_DATA_ID)


@then("The response code should be 200")
def step_check_response_code(context):
    assert context.response.status_code == 200


@then("The response code should be 404")
def step_check_response_code(context):
    assert context.response.status_code == 404


@then("The response code should be 201")
def step_check_response_code(context):
    assert context.response.status_code == 201
