Feature: SauceDemo login using Page Object Model

  Scenario: Successful login
    Given I open the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the inventory page

  Scenario: Invalid login
    Given I open the SauceDemo login page
    When I login with username "wrong_user" and password "wrong_password"
    Then I should see a login error
