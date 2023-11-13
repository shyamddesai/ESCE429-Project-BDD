Feature: Response code for API endpoint

    Scenario: GET todos API endpoint (Normal)
        Given The API endpoint is turned on
        When I send a GET request to the todo endpoint
        Then The response code should be 200

    Scenario: GET to invalid API endpoint (Error)
        Given The API endpoint is turned on
        When I send a GET request to an invalid endpoint
        Then The response code should be 404

    Scenario: POST to todos API endpoint (Alternate)
        Given The API endpoint is turned on
        When I send a POST request to the todo endpoint
        Then The response code should be 201