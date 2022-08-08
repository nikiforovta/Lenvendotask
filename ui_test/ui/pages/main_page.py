import allure

from ui import locators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = locators.MainPageLocators()

    @allure.step("Select value {1}")
    def select_value(self, value):
        self.scroll_to(self.locators.VALUES_LOCATOR)
        self.click(self.locators.VALUE_LOCATOR(value))
