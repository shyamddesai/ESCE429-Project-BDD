Feature: Add a project instance without an id

    Scenario: Create a new project with a title, description, completed status, and active status (Normal)
        Given The valid body parameters as input for a project
        When I create a new project instance
        Then The new entry is added to the database with all the data fields

    Scenario: Create a new project without any additional body parameters (Alternate)
        Given An empty body with no data fields
        When I create a new project instance
        Then I get a new project instance in the database with default values of an empty title and description, and both statuses set to false

    Scenario: Create a new project with an id as a body parameter (Error)
        Given A body with an id as the parameter
        When I create a new project instance
        Then I get an error code 400 for a bad request