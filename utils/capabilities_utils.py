from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import assert_that, is_, greater_than_or_equal_to, less_than_or_equal_to


def get_driver(browser: str, resolution: str):

    if browser.upper() == "CH":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'." f"Check your behave.ini file for available variables")
    if resolution != "1200x800":
        resolution = resolution.split("x")
        screen_width = resolution[0]
        screen_height = resolution[1]
        assert_that(int(screen_width), is_(greater_than_or_equal_to(800)), reason='Width should be greater than 800')
        assert_that(int(screen_width), is_(less_than_or_equal_to(2000)), reason='Width should be lower than 2000')
        assert_that(int(screen_height), is_(greater_than_or_equal_to(600)), reason='Height should be greater than 600')
        assert_that(int(screen_height), is_(less_than_or_equal_to(2000)), reason='Height should be lower than 2000')
        driver.set_window_size(width=screen_width, height=screen_height)
    return driver
