from behave import given, then, when
from helper_functions import *

'''
TEST_DATA_PROJECT_CATEGORY = {
    "title": "Test Project Category Title",
    "description": "Test Project Category description",
}
'''

@given("The valid input for the body of a category instance")
def step_valid_project_category_relationship_to_create(context):    
    context.response = sendRequest("POST", "projects", data=TEST_DATA_PROJECT, return_response_if_error=True) # create valid project instance
    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/categories"
    
    context.data = TEST_DATA_PROJECT_CATEGORY

@given("A valid title field only for the body of a category instance")
def step_project_category_relationship_with_only_description(context):
    context.response = sendRequest("POST", "projects", data=TEST_DATA_PROJECT, return_response_if_error=True) # create valid project instance
    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/categories"

    context.data = {
        "title": "Project Instance with only Category Title and No Description"
    }

@given("An empty body for the instance of the project")
def step_project_category_relationship_with_empty_body(context):
    context.response = sendRequest("POST", "projects", data=TEST_DATA_PROJECT, return_response_if_error=True) # create valid project instance
    context.id = context.response.json()["id"]
    context.URL = f"projects/{context.id}/categories"

    context.data = {} 

@given("The id of a project instance that doesn't exist but valid category body message")
def step_project_category_relationship_with_only_description(context):
    context.id = len(projectsGetEntries("projects"))+1
    context.URL = f"projects/{context.id}/categories"

    context.data = {
        "title": "Test Project Category Title",
        "description": "Test Project Category description"
    }    
    
@when("I create a relationship for a given project instance id to the category instance")
def step_create_project_category_relationship(context):
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)
    context.id = context.response.json()["id"]

@when("I try to create a relationship between a project instance id to an invalid category instance")
def step_invalid_project_category_relationship1(context):
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

@when("I try to create a relationship between a project instance id that doesn't exist to the category instance")
def step_invalid_project_category_relationship2(context):
    context.response = sendRequest("POST", context.URL, data=context.data, return_response_if_error=True)

@then("The new entry is created in the database with the correct relationship")
def step_verify_relationship_created(context):
    assert projectsGetEntries("projects")[0].get("categories")[0].get("id") == context.id
    assert projectsCategoriesGetEntries(context.URL)[0].get("title") == "Test Project Category Title"
    assert projectsCategoriesGetEntries(context.URL)[0].get("description") == "Test Project Category description"
    assert context.response.status_code == 201

@then("The new entry is created with the correct title field and empty description field of the category instance")
def step_verify_category_created_with_empty_category_description(context):
    assert projectsGetEntries("projects")[0].get("categories")[0].get("id") == context.id
    assert projectsCategoriesGetEntries(context.URL)[0].get("title") == "Project Instance with only Category Title and No Description"
    assert projectsCategoriesGetEntries(context.URL)[0].get("description") == ""
    assert context.response.status_code == 201

@then("I get an error code 400 because the title field is necessary")
def step_verify_relationship_failed(context):
    print(context.response.status_code)
    assert context.response.status_code == 400

@then("I get an error code 404 because the parent relationship isn't found")
def step_verify_relationship_failed2(context):
    assert context.response.status_code == 404