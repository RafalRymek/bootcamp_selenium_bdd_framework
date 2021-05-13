from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.shopping_cart_page import ShoppingCartPage


def before_all(context):

    context.main_page = MainPage()
    context.search_page = SearchPage()
    context.authentication_page = AuthenticationPage()
    context.registration_page = RegistrationPage()
    context.shopping_cart_page = ShoppingCartPage()

    context.search_page.go_to_url(url="http://automationpractice.com/index.php")


def after_all(context):
    context.search_page.quit_driver()
