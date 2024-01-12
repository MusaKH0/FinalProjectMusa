import time
import pytest

from base.base_page import BasePage
from pages.login_page import LoginPage
from utilities.read_csv import read_data


@pytest.mark.usefixtures("browser_setup_and_teardown")
class TestLogin:

    driver = None
    @classmethod
    def setup_method(cls):
        cls.login_page = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)

    @pytest.mark.smoke
    @pytest.mark.parametrize('username, password', read_data('login_test_data.csv'))
    def test_valid_credentials(self, username, password):
        print("### STARTED - test_valid_credentials")
        self.login_page.login(username, password)
        result = self.login_page.verify_login_is_successful()
        assert result
        self.base_page.logout()

    @pytest.mark.smoke
    @pytest.mark.parametrize('false_username, false_password', read_data('false_login_test_data.csv'))
    def test_invalid_username_and_password(self, false_username, false_password):
        print("### STARTED - test_invalid_username_and_password")
        self.login_page.login(false_username, false_password)
        result = self.login_page.verify_invalid_credentials()
        assert result
