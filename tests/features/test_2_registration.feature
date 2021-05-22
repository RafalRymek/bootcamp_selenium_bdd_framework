@registration
Feature: Registration of new user
  As a unregister user I want to register and create account on the page

  @registration_1
  Scenario: Successful register new user and create new account
    When I click [Sign in] button on the header of the page
    And I input unique email address in registration field
    And I fulfil all mandatory fields in registration form
    Then successful registration information is presented
