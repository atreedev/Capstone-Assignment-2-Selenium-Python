Feature: API data-driven testing

  Scenario Outline: Verify Todo API response for different IDs
    When I send a GET request for todo "<todo_id>"
    Then the response status code should be <status_code>
    And the response ID should be <todo_id>

    Examples:
      | todo_id | status_code |
      | 1       | 200         |
      | 2       | 200         |
      | 5       | 200         |
      | 10      | 200         |
