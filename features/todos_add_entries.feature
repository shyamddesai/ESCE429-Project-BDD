Feature: Add a new entry to the todo list

    Scenario: Add a new entry to the todo list (Normal)
        Given The input is valid and complete
        When I add a new entry to the todo list
        Then A new entry is added to the todo list

    Scenario: Add an entry with invalid input to the todo list (Error)
        Given The input is invalid
        When I add a new entry to the todo list
        Then An error code is returned

    Scenario: Add an entry with only the title (Alternate)
        Given The input is valid but incomplete
        When I add a new entry to the todo list
        Then A new entry is added to the todo list