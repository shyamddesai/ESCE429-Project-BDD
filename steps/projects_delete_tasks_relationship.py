from behave import given, then, when
from helper_functions import *

@given("A valid project instance with id with a task relationship to todo with id")
def step_valid_project_id_with_task_id(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/tasks"
    context.data = TEST_DATA_PROJECT_TASKS
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    
    project_id = context.id
    tasks_id = context.response.json()["id"]

    # keep creating tasks relationships until project_id = tasks_id
    while(project_id != tasks_id):
        context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
        tasks_id = context.response.json()["id"]
    
    context.URL = f"projects/{project_id}/tasks/{tasks_id}"

@given("A valid project instance with some_id with a task relationship to todo with id")
def step_project_id_with_different_task_id(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/tasks"
    project_id = context.id
    
    context.data = TEST_DATA_PROJECT_TASKS
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    tasks_id = context.response.json()["id"] # create two task relationships to ensure project id != task id

    context.URL = f"projects/{tasks_id}/tasks/{tasks_id}"

@given("The id of a project instance and tasks relationship that doesn't exist")
def step_project_and_task_does_not_exist(context):
    context.id = len(projectsGetEntries("projects"))+1
    context.URL = f"projects/{context.id}/tasks/{context.id}"

@when("I delete the task relationship of id")
def step_delete_task_relationship_given_id(context):
    context.response = sendRequest("DELETE", context.URL, return_response_if_error=True)

@then("I should not see the task relationship of id for the project instance of id in the database")
def step_verify_task_relationship_deleted(context):
    # if the tasks "id" doesn't exist in projects "id", then it was successfully deleted
    for i in projectsGetEntries("projects")[0].get("tasks"): # we created only one project, so we always access the correct index
        if i.get("id") == context.id:
            assert False
        assert True

@then("I should get error code 200")
def step_verify_error_code_200(context):
    assert context.response.status_code == 200

@then("I should get error code 400 when deleting the relationship")
def step_verify_error_code_400(context):
    assert context.response.status_code == 400

@then("I should get an error code 404 for the relationship not being found")
def step_verify_error_code_404(context):
    assert context.response.status_code == 404