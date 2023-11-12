Feature: Calculator

    Scenario: Add two numbers
        Given the calculator is turned on
        When I add 5 and 7
        Then the result should be 12
