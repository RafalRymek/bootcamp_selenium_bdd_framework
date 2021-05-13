from behave import *


@when("I click in search field and input specific text")
def step_impl(context):
    context.main_page.input_data_into_search_field(input_value="Printed dress")


@when("I click [Sign in] button on the header of the page")
def step_impl(context):
    context.main_page.click_on_sign_in_button()


@when("I click in search field and input specific 'Dress' text")
def step_impl(context):
    context.main_page.input_data_into_search_field(input_value="Dress")
