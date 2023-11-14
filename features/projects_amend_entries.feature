Feature: Amend an entry in the projects list

    Scenario: Replace the description, completed, and active status of a project instance given an id (Normal)
        Given The valid input for the id of a project
        When I amend the body of the instance of the project with a PUT request
        Then The existing project instance with the id will be replaced with the amended instance

    Scenario: Amend the description of a project instance given an id (Alternate)
        Given The valid input for the id of a project
        When I amend only the description of the instance of the project with a POST request
        Then The description field of the existing project is updated with all other fields remaining unchanged

    Scenario: Amend an instance of a project given an id that doesn't exist (Error)
        Given The id of a project instance that doesn't exist
        When I amend the body of the instance of the project with a PUT request
        Then I get an error code 404
        