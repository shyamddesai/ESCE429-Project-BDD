from behave import given, then, when
from helper_functions import *


@given("I add an entry to the database")
def step_add_entry(context):
    context.response = sendRequest(
        "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True)


@when("I request the entry for JSON payload")
def step_request_entry_JSON(context):
    context.response = sendRequest(
        "GET", f"todos/{context.response.json()['id']}", payload_type="json")


@when("I request the entry for XML payload")
def step_request_entry_XML(context):
    context.response = sendRequest(
        "GET", f"todos/{context.response.json()['id']}", payload_type="xml")


@when("I request the entry for unsupported payload")
def step_request_entry_XML(context):
    context.response = sendRequest(
        "GET", f"todos/{context.response.json()['id']}", payload_type="invalid", return_response_if_error=True)


@then("I should get a JSON payload")
def step_check_JSON_payload(context):
    assert isJSON(context.response)


@then("I should get a XML payload")
def step_check_XML_payload(context):
    assert isXML(context.response)


@then("I should get an error code")
def step_check_error_code(context):
    assert context.response.status_code in ERROR_CODES
