from behave import fixture, use_fixture

from steps.helper_functions import projectsSetUp, todosSetUp

# def before_all(context):
#     print("before all")
#     todosSetUp()
#     projectsSetUp()


def before_scenario(context, scenario):
    # print("before scenario")
    todosSetUp()
    projectsSetUp()
    use_fixture(todosSetUp, context)
    use_fixture(projectsSetUp, context)
