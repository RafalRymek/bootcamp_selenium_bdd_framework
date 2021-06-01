from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.capabilities_utils import get_driver
from behave.runner import Context
from allure import attach, attachment_type


def before_all(context: Context):
    # setup global variables
    setup = context.config.userdata
    context.driver = get_driver(browser=setup["browser"], resolution=setup["resolution"])
    # setup page_objects
    context.main_page = MainPage(context=context)
    context.search_page = SearchPage(context=context)
    context.authentication_page = AuthenticationPage(context=context)
    context.registration_page = RegistrationPage(context=context)
    context.shopping_cart_page = ShoppingCartPage(context=context)
    # open application under test
    context.search_page.go_to_url(url="http://automationpractice.com/index.php")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        attach(context.driver.get.screenshot_as_png(), attachment_type=attachment_type.PNG)


def after_all(context: Context):
    context.search_page.quit_driver()
