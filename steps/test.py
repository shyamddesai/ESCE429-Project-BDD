from helper_functions import *

if __name__ == "__main__":
    # todosSetUp()
    # projectsSetUp()

    # r = sendRequest("POST", "todos", data=TEST_DATA_ID)
    # id = r.json()["id"]
    URL = f"todos/12/tasksof"
    print(URL)
    sendRequest("POST", URL, data=TEST_DATA_TASKOF, prettyprint=True)
    print(todosTaskofGetEntries())
