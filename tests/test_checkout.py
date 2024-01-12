import time
import pytest
from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from base.base_page import BasePage
from selenium import webdriver
from utilities.read_csv import read_data
from utilities.logger_config import logger_setup


@pytest.mark.usefixtures("browser_setup_and_teardown")
class TestCheckout:

    driver = None

    @classmethod
    def setup_method(cls):
        cls.login_page = LoginPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.checkout_page = CheckoutPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.log = logger_setup(__name__)

    @pytest.mark.regression
    @pytest.mark.parametrize('username, password', read_data('login_test_data.csv'))
    @pytest.mark.parametrize('first_name, last_name, postal_code', read_data('checkout_info_test_data.csv'))
    def test_multiple_products_can_be_purchased(self, username, password, first_name, last_name, postal_code):
        self.log.info("### STARTED - test_multiple_products_can_be_purchased")
        self.login_page.login(username, password)
        self.home_page.add_all_products_to_cart_on_home_page()
        self.home_page.click_on_cart()
        self.checkout_page.click_checkout_button()
        self.checkout_page.enter_checkout_info(first_name, last_name, postal_code)
        self.checkout_page.click_continue_button_in_checkout()
        verify_items_in_checkout = self.checkout_page.verify_items_are_in_checkout_overview()
        assert verify_items_in_checkout
        self.checkout_page.click_finish_button()
        checkout_completed = self.checkout_page.verify_checkout_completed()
        assert checkout_completed
        self.base_page.logout()
