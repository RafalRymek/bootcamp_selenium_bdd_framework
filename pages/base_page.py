from behave.runner import Context
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, context: Context):
        self.driver = context.driver
        self.explicity_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, by_locator):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.explicity_wait.until(EC.element_to_be_clickable(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator).send_keys(value)

    def hover_over_on_element(self, by_locator):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def clear(self, by_locator):
        self.explicity_wait.until(EC.element_to_be_clickable(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator).clear()

    def quit_driver(self):
        self.driver.quit()
