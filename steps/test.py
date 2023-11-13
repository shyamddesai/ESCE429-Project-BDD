from helper_functions import *

if __name__ == "__main__":
    # todosSetUp()
    # projectsSetUp()

    # r = sendRequest("POST", "todos", data=TEST_DATA_ID)
    # id = r.json()["id"]
    # URL = f"todos/12/tasksof"
    # print(URL)
    # sendRequest("POST", URL, data=TEST_DATA_TASKOF, prettyprint=True)
    # print(todosTaskofGetEntries())

    # response = sendRequest(
    #     "POST", "todos", data=TEST_DATA_ID, return_response_if_error=True
    # )
    # id = response.json()["id"]
    # URL = f"todos/{id}/tasksof"
    # sendRequest(
    #     "POST", URL, data=TEST_DATA_TASKOF, return_response_if_error=True
    # )
    # tasksof_id = todosTaskofGetEntries()[0].get("id")
    # sendRequest("DELETE", f"todos/{188}/tasksof/56",
    #             return_response_if_error=True)
    print(todosTaskofGetEntries())
    print(len(todosTaskofGetEntries()))
