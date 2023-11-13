from behave import given, then, when
from helper_functions import *

"""    Scenario: Add a new taskof to an id (Normal)
        Given I have an entry
        When I add a new taskof to an id
        Then That id should have a new taskof

    Scenario: Add a new taskof to an id (Error)
        Given I have an entry
        When I add a new taskof to an invalid id
        Then I should get an error code

    Scenario: Add the same taskof to 2 ids (Alternate)
        Given I have two entries
        When I add the same taskof to 2 ids
        Then Both ids should have the same taskof
"""


@given("I have an entry")
def step_have_entry(context):
    context.response = sendRequest(
        "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True)
    context.id = context.response.json()["id"]
    context.URL = f"todos/{context.id}/tasksof"


@when("I add a new taskof to an id")
def step_add_taskof(context):
    sendRequest(
        "POST", context.URL, data=TEST_DATA_TASKOF, return_response_if_error=True)


@when("I add a new taskof to an invalid id")
def step_add_taskof(context):
    context.response = sendRequest(
        "POST", "todos/invalid/tasksof", data=TEST_DATA_TASKOF, return_response_if_error=True)


@then("That id should have a new taskof")
def step_check_taskof(context):
    assert len(todosGetEntries()[0].get("tasksof")) == 1


@given("I have two entries")
def step_add_2_entries(context):
    context.response = sendRequest(
        "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True)
    context.id1 = context.response.json()["id"]
    context.response = sendRequest(
        "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True)
    context.id2 = context.response.json()["id"]
    context.URL1 = f"todos/{context.id1}/tasksof"
    context.URL2 = f"todos/{context.id2}/tasksof"


@when("I add the same taskof to 2 ids")
def step_add_taskof(context):
    sendRequest(
        "POST", context.URL1, data=TEST_DATA_TASKOF, return_response_if_error=True)
    tasksof_id = todosTaskofGetEntries()[0].get("id")
    # associate the same taskof with another id
    sendRequest(
        "POST", context.URL2, data={"id": tasksof_id}, return_response_if_error=True)


@then(u'Both ids should have the same taskof')
def step_check_taskof(context):
    # check if the taskof is associated with both ids
    assert todosGetEntries()[0].get(
        "tasksof") == todosGetEntries()[1].get("tasksof")
