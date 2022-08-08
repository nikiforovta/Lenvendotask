import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    locators = None

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 30
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step('Scroll to element')
    def scroll_to(self, locator):
        element = self.find(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step('Send keys')
    def send_keys(self, locator, keys, timeout=None, clear=True):
        element = self.click(locator, timeout=timeout) if clear else self.find(locator, timeout=timeout)
        if clear:
            element.clear()
        element.send_keys(keys)

    @allure.step('Login using {0}')
    def login(self, credentials):
        self.driver.get(f"http://{credentials[0]}:{credentials[1]}@qa.digift.ru/")
