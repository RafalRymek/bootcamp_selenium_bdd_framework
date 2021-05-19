from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(browser: str, resolution: str):

    if browser.upper() == "CH":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'." f"Check your behave.ini file for available variables")
    if resolution == "1200x800":
        driver.set_window_size(1200, 800)
    elif resolution != "1200x800":
        resolution = resolution.split("x")
        driver.set_window_size(width=resolution[0], height=resolution[1])
    else:
        print(f"Unexpected resolution format: {resolution}")
    return driver
