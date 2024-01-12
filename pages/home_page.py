import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utilities.utils import Utils


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    HOME_PAGE_TITLE_CLASS_NAME = "title"
    SAUCE_LABS_BACKPACK_ID = "item_4_title_link"
    INVENTORY_ITEM_LABEL_XPATH = "//a//div[@class='inventory_item_name ']"
    ADD_PRODUCT_FROM_INVENTORY_LIST_XPATH = "//div[@class='inventory_item']//descendant::button[@class='btn btn_primary btn_small btn_inventory ']"
    REMOVE_PRODUCT_FROM_INVENTORY_LIST_XPATH = "//div[@class='inventory_item']//descendant::button[@class='btn btn_secondary btn_small btn_inventory ']"
    PRICE_BAR_BUTTON_XPATH = "//div[@class='pricebar']//button"
    INVENTORY_LIST_CLASS_NAME = "inventory_list"

    def click_on_product(self, product_name):
        PRODUCT_ITEM = f"//div[text()='{product_name}']"
        self.click_element_after_wait("xpath", PRODUCT_ITEM)

    def from_home_page_add_product_to_cart(self, product_name):
        ADD_TO_CART_PRICEBAR_XPATH = f"//div[text()='{product_name}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button[@class='btn btn_primary btn_small btn_inventory ']"
        for i in self.INVENTORY_LIST_CLASS_NAME:
            if self.wait_for_presence_of_element_to_be_located("class_name", self.INVENTORY_LIST_CLASS_NAME).text.__contains__(product_name):
                self.click_element_after_wait("xpath", ADD_TO_CART_PRICEBAR_XPATH)
                time.sleep(3)
                break

    def from_home_page_remove_product_from_cart(self, product_name):
        REMOVE_FROM_CART_PRICEBAR_XPATH = f"//div[text()='{product_name}']//ancestor::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button[@class='btn btn_secondary btn_small btn_inventory ']"
        for i in self.INVENTORY_LIST_CLASS_NAME:
            if self.wait_for_presence_of_element_to_be_located("class_name", self.INVENTORY_LIST_CLASS_NAME).text.__contains__(product_name):
                self.click_element_after_wait("xpath", REMOVE_FROM_CART_PRICEBAR_XPATH)
                time.sleep(3)
                break

    def click_on_cart(self):
        self.click_element_after_wait("class_name", self.SHOPPING_CART_CLASS_NAME)

    def verify_home_page_title(self):
        actual_text = self.wait_for_element_to_be_visible("class_name", self.HOME_PAGE_TITLE_CLASS_NAME).text
        expected_text = "Products"
        return self.utils.verify_text_contains(actual_text, expected_text)

    def add_all_products_to_cart_on_home_page(self):
        products = self.driver.find_elements(By.XPATH, self.PRICE_BAR_BUTTON_XPATH)
        for button in products:
            if button.get_attribute("class") == "btn btn_primary btn_small btn_inventory ":
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(button.find_element(By.XPATH, self.ADD_PRODUCT_FROM_INVENTORY_LIST_XPATH)).click().perform()

    def remove_all_products_from_cart_on_home_page(self):
        products = self.driver.find_elements(By.XPATH, self.PRICE_BAR_BUTTON_XPATH)
        for button in products:
            if button.get_attribute("class") == "btn btn_secondary btn_small btn_inventory ":
                actionChains = ActionChains(self.driver)
                actionChains.move_to_element(button.find_element(By.XPATH, self.REMOVE_PRODUCT_FROM_INVENTORY_LIST_XPATH)).click().perform()

    def verify_product_on_home_page_is_removed_from_cart(self):
        pricebar = self.wait_for_element_to_be_visible("xpath", self.PRICE_BAR_BUTTON_XPATH)
        shopping_cart = self.wait_for_element_to_be_visible("class_name", self.SHOPPING_CART_BADGE_CLASS_NAME)
        if pricebar.get_attribute("class") == "btn btn_primary btn_small btn_inventory " and shopping_cart is None:
            print("Product was successfully removed from the cart!")
            return True
        else:
            print("Item was NOT removed from the cart")
            return False

        # for product in self.INVENTORY_ITEM_LABEL_XPATH:
        #     if product is self.wait_for_element_to_be_visible("class_name", self.INVENTORY_ITEM_LABEL_XPATH).text == product_name:
        #         # Add this product to cart
        #         add_btn = product.self.wait_for_element_to_be_visible("class_name", "btn btn_primary btn_small btn_inventory ")
        #         add_btn.click()
        #         break
        #
        # for i in self.INVENTORY_ITEM_LABEL_XPATH:
        #     if i in self.wait_for_element_to_be_visible("xpath", self.INVENTORY_ITEM_LABEL_XPATH).text is product_name:
        #         self.click_element_after_wait("xpath", self.ADD_PRODUCT_FROM_INVENTORY_LIST_XPATH)
        #         break
