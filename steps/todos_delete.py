from behave import given, then, when
from helper_functions import *

"""
    Scenario: delete a tasksof by deleting the tasksof (Normal)
        Given I have an id and a tasksof
        When I delete the tasksof
        Then I should not see the tasksof in the database

    Scenario: delete a tasks of by deleting the id (Alternate)
        Given I have an id and a tasksof
        When I delete the id
        Then I should not see the tasksof in the database

    Scenario: deleting a non-existing taskof (Error)
        Given I have an id and a tasksof
        When I delete the tasksof using a non-existing id
        Then I should get an error code
"""


@given("I have an id and a tasksof")
def step_have_id_and_tasksof(context):
    context.response = sendRequest(
        "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True
    )
    context.id = context.response.json()["id"]
    context.URL = f"todos/{context.id}/tasksof"
    sendRequest(
        "POST", context.URL, data=TEST_DATA_TASKOF, return_response_if_error=True
    )
    context.tasksof_id = todosTaskofGetEntries()[0].get("id")


@when("I delete the tasksof")
def step_delete_tasksof(context):
    sendRequest(
        "DELETE", f"{context.URL}/{context.tasksof_id}", return_response_if_error=True
    )


@when("I delete the id")
def step_delete_id(context):
    sendRequest("DELETE", f"todos/{context.id}", return_response_if_error=True)


@when("I delete the tasksof using a non-existing id")
def step_delete_id(context):
    context.response = sendRequest(
        "DELETE",
        f"todos/invalid/tasksof/invalid",
        return_response_if_error=True,
    )


@then("I should not see the tasksof in the database")
def step_check_tasksof(context):
    assert not todosTaskofGetEntries()
