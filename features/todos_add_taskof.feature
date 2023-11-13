Feature: Adding taskof to an id

    Scenario: Add a new taskof to an id (Normal)
        Given I have an entry
        When I add a new taskof to an id
        Then That id should have a new taskof

    Scenario: Add a new taskof to an id (Error)
        Given I have an entry
        When I add a new taskof to an invalid id
        Then I should get an error code

    Scenario: Add the same taskof to 2 ids (Alternate)
        Given I have two entries
        When I add the same taskof to 2 ids
        Then Both ids should have the same taskof