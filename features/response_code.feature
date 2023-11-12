Feature: Response code for API endpoint

    Scenario: GET todos API endpoint
        Given The API endpoint is turned on
        When I send a GET request to the endpoint
        Then The response code should be 200