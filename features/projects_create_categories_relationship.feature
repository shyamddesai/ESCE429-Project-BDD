Feature: Create a relationship between a project instance and a category instance

    Scenario: Create a relationship between a project instance given its' id and category instance (Normal)
        Given The valid input for the body of a category instance
        When I create a relationship for a given project instance id to the category instance
        Then The new entry is created in the database with the correct relationship

    Scenario: Create a relationship between a project instance given it's id and a category with only the title (Alternate)
        Given A valid title field only for the body of a category instance
        When I create a relationship for a given project instance id to the category instance
        Then The new entry is created with the correct title field and empty description field of the category instance

    Scenario: Create an relationship category for a project instance without any title field (Error)
        Given An empty body for the instance of the project
        When I try to create a relationship between a project instance id to an invalid category instance
        Then I get an error code 400 because the title field is necessary

    Scenario: Create an relationship category for a project instance for a project id that doesn't exist (Error)
        Given The id of a project instance that doesn't exist but valid category body message
        When I try to create a relationship between a project instance id that doesn't exist to the category instance
        Then I get an error code 404 because the parent relationship isn't found
        

    