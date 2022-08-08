import json
import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class BaseCase:
    USERNAME = None
    PASSWORD = None

    driver = None
    logger = None

    main_page = None
    base_page = None

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, repo_root, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.logger = logger

        with open(os.path.join(repo_root, 'credentials.json')) as credentials:
            credentials_dict = json.load(credentials)
            self.USERNAME = credentials_dict['USERNAME']
            self.PASSWORD = credentials_dict['PASSWORD']

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))

    @pytest.fixture(scope='function')
    def login(self):
        self.base_page.login(credentials=(self.USERNAME, self.PASSWORD))
        return self.main_page
