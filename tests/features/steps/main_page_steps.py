from behave import *


@when('I search for "{keyword_to_search}" in the searching field')
def step_impl(context, keyword_to_search: str):
    context.main_page.input_data_into_search_field(input_value=keyword_to_search)


@when("I click [Sign in] button on the header of the page")
def step_impl(context):
    context.main_page.click_on_sign_in_button()
