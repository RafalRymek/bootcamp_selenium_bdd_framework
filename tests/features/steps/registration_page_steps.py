from behave import *


@step("I fulfil all mandatory fields in registration form")
def step_impl(context):
    context.registration_page.user_registration()
