@search
Feature: Search for product
  As a user I want to check presence of results when I input some test into search engine

  @search_1
  Scenario: Get results after input some specific text
    When I search for "Printed Dress" in the searching field
    Then specific number of results is presented