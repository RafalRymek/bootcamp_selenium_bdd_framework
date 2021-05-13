from behave import *


@then("specific number of results is presented")
def step_impl(context):
    context.search_page.check_amount_of_search_results()


@step("hover over mouse on first result")
def step_impl(context):
    context.search_page.hover_over_on_first_result()


@then("[Add to cart] button is presented and user click on it")
def step_impl(context):
    context.search_page.add_product_to_basket()


@when("I move mouse to shopping cart on the header of the page")
def step_impl(context):
    context.search_page.move_to_shopping_cart()


@step("click [Order cart] button")
def step_impl(context):
    context.search_page.click_button_order_cart()
