import time
import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from utilities.logger_config import logger_setup
from utilities.read_csv import read_data


@pytest.mark.usefixtures("browser_setup_and_teardown")
class TestProductDetails:

    driver = None

    @classmethod
    def setup_method(cls):
        cls.login_page = LoginPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.products_details_page = ProductDetailsPage(cls.driver)
        cls.cart_page = CartPage(cls.driver)
        cls.log = logger_setup(__name__)

    @pytest.mark.regression
    @pytest.mark.parametrize("username, password", read_data("login_test_data.csv"))
    def test_successfully_adding_a_product_to_cart_from_product_details_page(self, username, password):
        self.log.info("### STARTED - test_successfully_adding_a_product_to_cart_from_product_details_page")
        self.login_page.login(username, password)
        self.home_page.click_on_product("Sauce Labs Backpack")
        self.products_details_page.from_product_details_page_add_product_to_cart()
        self.products_details_page.click_on_cart_in_product_details()
        result = self.cart_page.verify_a_product_is_successfully_added_to_cart("Sauce Labs Backpack")
        assert result

