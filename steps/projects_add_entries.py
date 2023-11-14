from behave import given, then, when
from helper_functions import *

@given("The valid body parameters as input for a project")
def step_valid_project_body_to_create(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"

@given("An empty body with no data fields")
def step_empty_project_body_to_create(context):
    context.data = {}
    context.URL = "projects"

@given("A body with an id as the parameter")
def step_create_project_with_bad_data(context):
    context.data = {
        "id": 1,
        "title": "Test Project Title",
        "completed": False,
        "active": True,
        "description": "Test Project description"
    }
    context.URL = "projects"

@when("I create a new project instance")
def step_create_project_with_body(context):
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

    if(context.response.status_code != 400):
        context.id = context.response.json()["id"]
        context.URL = f"projects/{context.id}"

@then("The new entry is added to the database with all the data fields")
def step_verify_project_created_successfully(context):
    assert projectsGetEntries()[0].get("title") == "Test Project Title"
    assert projectsGetEntries()[0].get("completed") == "false"
    assert projectsGetEntries()[0].get("active") == "true"
    assert projectsGetEntries()[0].get("description") == "Test Project description"

@then("I get a new project instance in the database with default values of an empty title and description, and both statuses set to false")
def step_verify_project_created_with_empty_fields(context):
    assert projectsGetEntries()[0].get("title") == ""
    assert projectsGetEntries()[0].get("completed") == "false"
    assert projectsGetEntries()[0].get("active") == "false"
    assert projectsGetEntries()[0].get("description") == ""

@then("I get an error code 400 for a bad request")
def step_verify_project_failed_to_create(context):
    assert context.response.status_code == 400