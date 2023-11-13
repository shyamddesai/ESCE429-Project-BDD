from behave import given, then, when
from helper_functions import *


@given("The input is valid and complete")
def step_input_valid_complete(context):
    context.data = TEST_DATA_ID
    context.URL = "todos"


@given("The input is invalid")
def step_input_invalid(context):
    context.data = {"invalid": "invalid"}
    context.URL = "todos"


@given("The input is valid but incomplete")
def step_input_valid_incomplete(context):
    context.data = {"title": "title"}
    context.URL = "todos"


@when("I add a new entry to the todo list")
def step_add_entry(context):
    context.response = sendRequest(
        "POST", context.URL, data=context.data, return_response_if_error=True,)


@then("A new entry is added to the todo list")
def step_check_entry_added(context):
    assert len(todosGetEntries(context.URL)) == 1


@then("An error code is returned")
def step_check_error_code(context):
    assert context.response.status_code in ERROR_CODES
