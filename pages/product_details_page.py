from base.base_page import BasePage
from base.custom_driver import CustomDriver
from utilities.utils import Utils


class ProductDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    SAUCE_LABS_BACKPACK_ADD_TO_CART_ID = "add-to-cart-sauce-labs-backpack"

    def from_product_details_page_add_product_to_cart(self):
        self.click_element_after_wait("id", self.SAUCE_LABS_BACKPACK_ADD_TO_CART_ID)

    def click_on_cart_in_product_details(self):
        self.click_element_after_wait("class_name", self.SHOPPING_CART_CLASS_NAME)
