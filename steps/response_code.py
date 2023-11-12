from behave import given, then, when
from helper_functions import *


@given("The API endpoint is turned on")
def step_API_turned_on(context):
    context.URL = "todos"
    assert isAPIRunning(context.URL)


@when("I send a GET request to the endpoint")
def step_send_GET_request(context):
    context.response = sendRequest("GET", context.URL)


@then("The response code should be 200")
def step_check_response_code(context):
    assert context.response.status_code == 200
