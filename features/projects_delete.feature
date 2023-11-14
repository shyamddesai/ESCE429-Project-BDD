Feature: Delete a project instance

    Scenario: Delete a project instance using its id (Normal)
        Given A valid project instance with id
        When I delete the project instance
        Then I should not see the project instance of the id in the database

    Scenario: Delete a project instance using its categories relationship (Alternate)
        Given A valid project instance with id with a categories relationship with some_id
        When I delete the categories relationship of project instance with id
        Then I should not see the categories relationship of the project instance with id in the database

    Scenario: Delete a project instance with id that doesn't exist (Error)
        Given The id of a project instance that isn't valid
        When I delete the project instance
        Then I should get an error code 404 for the project not being found
