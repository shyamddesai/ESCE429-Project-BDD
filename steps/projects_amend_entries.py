from behave import given, then, when
from helper_functions import *

'''
TEST_DATA_PROJECT = {
    "title": "Test Project Title",
    "completed": False,
    "active": True,
    "description": "Test Project description",
}
'''

@given("The valid input for the id of a project")
def step_valid_project_id_to_amend(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"

    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    
    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}"

@given("The id of a project instance that doesn't exist")
def step_invalid_project_id_to_amend(context):
    context.id = len(projectsGetEntries("projects"))+1
    context.URL = f"projects/{context.id}"

@when("I amend the body of the instance of the project with a PUT request")
def step_amend_project_with_put(context):
    projects_data_with_completed_and_active_status_and_description_amended = {
        "title": "New Project Title",
        "completed": True,
        "active": False,
        "description": "This is the description of a completed Test Project replaced with a PUT request",
    }

    context.response = sendRequest("PUT", context.URL, data=projects_data_with_completed_and_active_status_and_description_amended, return_response_if_error=True)

@when("I amend only the description of the instance of the project with a POST request")
def step_amend_project_with_post(context):
    new_description_data = {
        "description": "This is the final description of the Test Project with a POST request"
    }

    context.response = sendRequest("POST", context.URL, data=new_description_data, return_response_if_error=True)

@then("The existing project instance with the id will be replaced with the amended instance")
def step_verify_project_replaced(context):
    assert projectsGetEntries()[0].get("title") == "New Project Title"
    assert projectsGetEntries()[0].get("completed") == "true"
    assert projectsGetEntries()[0].get("active") == "false"
    assert projectsGetEntries()[0].get("description") == "This is the description of a completed Test Project replaced with a PUT request"

'''
The way PUT and POST requests are handled in the API is unexpected. 
We expected PUT to amend the body of the project instance the way that POST actually does,
and we expected POST to create and/or replace a project instance the way that PUT actually does.
However, we found that we cannot make POST requests for any id for which a project instance doesn't exist.
'''
@then("The description field of the existing project is updated with all other fields remaining unchanged")
def step_verify_project_amended(context):
    assert projectsGetEntries()[0].get("title") == "Test Project Title"
    assert projectsGetEntries()[0].get("completed") == "false"
    assert projectsGetEntries()[0].get("active") == "true"
    assert projectsGetEntries()[0].get("description") == "This is the final description of the Test Project with a POST request"

@then("I get an error code 404")
def step_verify_project_failed_to_amend(context):
    assert context.response.status_code == 404