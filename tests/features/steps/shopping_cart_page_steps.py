from behave import *


@then("expected amount of products in basket is presented on the page")
def step_impl(context):
    context.shopping_cart_page.check_order_summary_quantity()
