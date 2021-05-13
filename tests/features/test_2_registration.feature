# Created by rafal.rymek at 13/05/2021
Feature: Registration of new user
  As a unregister user I want to register and create account on the page

  Scenario: Successful register new user and create new account
    When I click [Sign in] button on the header of the page
    And I input unique email address in registration field
    And I fulfil all mandatory fields in registration form
    Then successful registration information is presented
