from behave import given, then, when
from helper_functions import *
import json as jsonObj

@given("A valid project instance with id")
def step_valid_project_with_id(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    
    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}"

@given("A valid project instance with id with a categories relationship with some_id")
def step_project_id_with_different_categories_id(context):
    context.data = TEST_DATA_PROJECT
    context.URL = "projects"
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/categories"
    context.data = TEST_DATA_PROJECT_CATEGORY
    
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    project_id = context.id
    categories_id = context.response.json()["id"]

    # if(jsonObj.get("categories_id").asInt() > jsonObj.get("project_id").asInt()):
    #     print(jsonObj.get("categories_id").asInt(), jsonObj.get("project_id").asInt())   
    #     while(project_id != categories_id):
    #         context.response = sendRequest("POST", "projects", data=TEST_DATA_PROJECT, return_response_if_error=True)
    #         project_id = context.response.json()["id"]
    #     context.response = sendRequest("POST", "projects", data=TEST_DATA_PROJECT, return_response_if_error=True)
    #     project_id = context.response.json()["id"]
            
    # while(project_id != categories_id):
    #     context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    #     categories_id = context.response.json()["id"]

    context.URL = f"projects/{categories_id}/categories/{categories_id}"

    print(projectsGetEntries("projects"))

@given("The id of a project instance that isn't valid")
def step_project_does_not_exist(context):
    context.id = len(projectsGetEntries("projects"))+1
    context.URL = f"projects/{context.id}"

@when("I delete the project instance")
def step_delete_project_given_id(context):
    context.response = sendRequest("DELETE", context.URL, return_response_if_error=True)

@when("I delete the categories relationship of project instance with id")
def step_delete_categories_relationship_given_id(context):
    context.response = sendRequest("DELETE", context.URL, return_response_if_error=True)

@then("I should not see the project instance of the id in the database")
def step_verify_project_deleted(context):
    assert len(projectsGetEntries("projects")) == 0

@then("I should not see the categories relationship of the project instance with id in the database")
def step_verify_project_categories_relationship_deleted(context):
    print(projectsGetEntries("projects")[0])
    # if the categories id doesn't exist inside the projects instance, then it was successfully deleted
    if projectsGetEntries("projects")[0].get("categories") is not None:
        for i in projectsGetEntries("projects")[0].get("categories"):
            if i.get("id") == context.id:
                assert False
            else: assert True
    print(projectsGetEntries("projects"))

@then("I should get an error code 404 for the project not being found")
def step_verify_error_code_404_not_found(context):
    assert context.response.status_code == 404
