import pytest

from base import BaseCase


@pytest.mark.usefixtures("login")
class TestMainPage(BaseCase):
    """Tests for main page"""

    @pytest.mark.parametrize('value', ["500", "1000", "2000", "3000", "5000", "10000"])
    def test_values(self, value):
        """Test for different values"""
        self.main_page.select_value(value)
        assert self.main_page.find(self.main_page.locators.ACTIVE_BUTTON).text == value
        assert self.main_page.find(self.main_page.locators.VALUE_INPUT).get_attribute("value") == value
