Feature: SauceDemo login

  Scenario: Successful login with valid credentials
    Given I open the SauceDemo login page
    When I enter the username "standard_user"
    And I enter the password "secret_sauce"
    And I click the login button
    Then I should be on the inventory page

  Scenario: Unsuccessful login with invalid credentials
    Given I open the SauceDemo login page
    When I enter the username "wrong_user"
    And I enter the password "wrong_password"
    And I click the login button
    Then I should see a login error
