# Created by rafal.rymek at 12/05/2021
Feature: Search for product
  As a user I want to check presence of results when I input some test into search engine

  Scenario: Get results after input some specific text
    When I click in search field and input specific text
    Then specific number of results is presented