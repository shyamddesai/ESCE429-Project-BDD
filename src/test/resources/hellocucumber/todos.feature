Feature: Test CRUD methods in TodoManager REST API testing
  (Add some description here)

  Scenario Outline: View todo instances
    Given I setup the GET todos API endpoint
    When I send GET request
    Then I should receive valid HTTP response code 200

  For Later:
  Given I setup the GET todos API endpoint
  When I send GET request
  Then I should receive all the instances of todo
