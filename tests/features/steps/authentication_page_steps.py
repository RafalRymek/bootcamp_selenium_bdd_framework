from behave import *
import time


@step("I input unique email address in registration field")
def step_impl(context):
    context.authentication_page.input_email_for_registration(user_email="test" + str(time.time() * 1000) + "@test.com")


@then("successful registration information is presented")
def step_impl(context):
    context.authentication_page.confirmation_user_successful_registration()
