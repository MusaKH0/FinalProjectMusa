import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utilities.utils import Utils


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    CART_TITLE_CLASS_NAME = "title"
    CONTINUE_SHOPPING_BUTTON_ID = "continue-shopping"
    REMOVE_PRODUCT_BUTTON_FROM_CART_LIST_XPATH = "//div[@class='item_pricebar']//button"
    REMOVED_ITEM_CLASS_NAME = "removed_cart_item"
    INVENTORY_ITEM_NAME_CLASS_NAME = "inventory_item_name"
    CART_LIST_CLASS_NAME = "cart_list"

    def click_continue_shopping_button(self):
        self.click_element_after_wait("id", self.CONTINUE_SHOPPING_BUTTON_ID)

    def verify_a_product_is_successfully_added_to_cart(self, product_name):
        actual_cart_page_name = self.wait_for_element_to_be_visible("class_name", self.CART_TITLE_CLASS_NAME).text
        expected_cart_page_name = "Your Cart"
        actual_product_name = self.wait_for_element_to_be_visible("class_name", self.INVENTORY_ITEM_NAME_CLASS_NAME).text
        expected_product_name = f"{product_name}"
        verify_cart_page_title = self.utils.verify_text_contains(actual_cart_page_name, expected_cart_page_name)
        verify_product_in_cart_page = self.utils.verify_text_contains(actual_product_name, expected_product_name)
        return verify_cart_page_title and verify_product_in_cart_page

    # """
    # for below method to work, following steps need to be completed:
    # 1 - store an empty dictionary in a variable
    # 2 - get the label names of each item in the cart
    # 3 - create a loop to iterate each one into a key
    # 4 - get the 'add to cart / remove' button of each item
    # 5 - iterate the class attribute as the values for each corresponding key
    # 5 - if the item matches the label name and class attribute from the dictionary, then remove that item from the cart
    # """
    def remove_a_product_from_cart_on_cart_page(self, product_name):
        CART_PRICEBAR_XPATH = f"//div[text()='{product_name}']//parent::a//following-sibling::div[@class='item_pricebar']//button[@class='btn btn_secondary btn_small cart_button']"
        for i in self.CART_LIST_CLASS_NAME:
            if self.wait_for_presence_of_element_to_be_located("class_name", self.CART_LIST_CLASS_NAME).text.__contains__(product_name):
                self.click_element_after_wait("xpath", CART_PRICEBAR_XPATH)
                time.sleep(3)
                break

    def remove_all_products_from_cart_on_cart_page(self):
        products = self.wait_for_presence_of_all_elements_to_be_located("xpath", self.REMOVE_PRODUCT_BUTTON_FROM_CART_LIST_XPATH)
        for button in products:
            if button.get_attribute("class") == "btn btn_secondary btn_small cart_button":
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(button.find_element(By.XPATH, self.REMOVE_PRODUCT_BUTTON_FROM_CART_LIST_XPATH)).click().perform()

    def verify_product_on_cart_page_is_removed_from_cart(self):
        if self.wait_for_presence_of_element_to_be_located("class_name", self.REMOVED_ITEM_CLASS_NAME):
            print("Product was successfully removed from the cart!")
            return True
        else:
            print("Item was NOT removed from the cart")
            return False




