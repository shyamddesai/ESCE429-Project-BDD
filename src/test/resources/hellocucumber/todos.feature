Feature: Test CRUD methods in TodoManager REST API testing

  Scenario Outline: View todo instances
    Given I setup the GET todos API endpoint
    When I send GET request
    Then I should receive valid HTTP response code 200