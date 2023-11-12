Feature: Response code for API endpoint

    Scenario Outline: GET todos API endpoint
        Given The API endpoint is turned on
        When I send GET request
        Then I should receive valid HTTP response code 200