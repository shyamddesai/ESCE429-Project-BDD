Feature: Delete the instance of the relationship named tasks between project and todo given an id

    Scenario: Delete the tasks relationship of id for a project instance of id (Normal)
        Given A valid project instance with id with a task relationship to todo with id
        When I delete the task relationship of id
        Then I should not see the task relationship of id for the project instance of id in the database
            And I should get error code 200

    Scenario: Delete the tasks relationship of id for a project instance of an unique id (Alternate)
        Given A valid project instance with some_id with a task relationship to todo with id
        When I delete the task relationship of id
        Then I should get error code 400 when deleting the relationship

    Scenario: Delete a tasks relationship that doesn't exist for a project instance (Error)
        Given The id of a project instance and tasks relationship that doesn't exist
        When I delete the task relationship of id
        Then I should get an error code 404 for the relationship not being found
