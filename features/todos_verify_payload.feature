Feature: Verify that the payloads are properly generated

    Scenario: Verify that the JSON payload is properly returned (Normal)
        Given I add an entry to the database
        When I request the entry for JSON payload
        Then I should get a JSON payload

    Scenario: Verify that the XML payload is properly returned (Alternate)
        Given I add an entry to the database
        When I request the entry for XML payload
        Then I should get a XML payload

    Scenario: Verify that other payload types are not supported (Error)
        Given I add an entry to the database
        When I request the entry for unsupported payload
        Then I should get an error code