from selenium.webdriver.common.by import By


class MainPageLocators:
    VALUES_LOCATOR = (
        By.CSS_SELECTOR,
        'div.par'
    )

    VALUE_LOCATOR = lambda self, value: (
        By.CSS_SELECTOR,
        f'li[data-value="{value}"]'
    )

    ACTIVE_BUTTON = (
        By.CSS_SELECTOR,
        'button.par-options__button--active'
    )

    VALUE_INPUT = (
        By.CSS_SELECTOR,
        'input#range-value-input'
    )
