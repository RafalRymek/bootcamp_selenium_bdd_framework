@add_to_cart
Feature: Adding product to basket
  As a user I want to add product to basket

  @add_to_cart_1
  Scenario: Add product to basket
    When I search for "Dress" in the searching field
    And hover over mouse on first result
    Then [Add to cart] button is presented and user click on it
    When I move mouse to shopping cart on the header of the page
    And click [Order cart] button
    Then expected amount of products in basket is presented on the page