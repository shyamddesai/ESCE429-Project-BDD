Feature: delete an entries from the database

    Scenario: delete a tasksof by deleting the tasksof (Normal)
        Given I have an id and a tasksof
        When I delete the tasksof
        Then I should not see the tasksof in the database

    Scenario: delete a tasks of by deleting the id (Alternate)
        Given I have an id and a tasksof
        When I delete the id
        Then I should not see the tasksof in the database

    Scenario: deleting a non-existing taskof (Error)
        Given I have an id and a tasksof
        When I delete the tasksof using a non-existing id
        Then I should get an error code
