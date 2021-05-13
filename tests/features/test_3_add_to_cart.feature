# Created by rafal.rymek at 13/05/2021
Feature: Adding product to basket
  As a user I want to add product to basket

  Scenario: Add product to basket
    When I click in search field and input specific 'Dress' text
    And hover over mouse on first result
    Then [Add to cart] button is presented and user click on it
    When I move mouse to shopping cart on the header of the page
    And click [Order cart] button
    Then expected amount of products in basket is presented on the page