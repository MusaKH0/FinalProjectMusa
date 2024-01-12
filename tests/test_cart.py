import time
import pytest
from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from base.base_page import BasePage
from selenium import webdriver

from utilities.logger_config import logger_setup
from utilities.read_csv import read_data


@pytest.mark.usefixtures("browser_setup_and_teardown")
class TestCart:

    driver = None

    @classmethod
    def setup_method(cls):
        cls.login_page = LoginPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.cart_page = CartPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.log = logger_setup(__name__)

    @pytest.mark.regression
    @pytest.mark.parametrize('username, password', read_data('login_test_data.csv'))
    def test_return_to_home_page_from_cart_page(self, username, password):
        self.log.info("### STARTED - test_return_to_home_page_from_cart_page")
        self.login_page.login(username, password)
        self.home_page.click_on_cart()
        self.cart_page.click_continue_shopping_button()
        result = self.home_page.verify_home_page_title()
        assert result
        self.base_page.logout()

    @pytest.mark.smoke
    @pytest.mark.parametrize('username, password', read_data('login_test_data.csv'))
    def test_removing_a_product_from_cart_on_cart_page(self, username, password):
        print("### STARTED - test_removing_a_product_from_cart_on_cart_page")
        self.login_page.login(username, password)
        self.home_page.from_home_page_add_product_to_cart("Sauce Labs Fleece Jacket")
        self.home_page.click_on_cart()
        self.cart_page.verify_a_product_is_successfully_added_to_cart("Sauce Labs Fleece Jacket")
        self.cart_page.remove_all_products_from_cart_on_cart_page()
        removed_product = self.cart_page.verify_product_on_cart_page_is_removed_from_cart()
        assert removed_product
        self.base_page.logout()
