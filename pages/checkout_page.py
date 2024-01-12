from base.base_page import BasePage
from utilities.utils import Utils


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    CHECKOUT_BUTTON_ID = "checkout"
    FIRST_NAME_CHECKOUT_ID = "first-name"
    LAST_NAME_CHECKOUT_ID = "last-name"
    POSTAL_CODE_CHECKOUT_ID = "postal-code"
    CONTINUE_BUTTON_PAGE_ONE_CHECKOUT_ID = "continue"
    CART_ITEMS_CLASS_NAME = "cart_item"
    FINISH_BUTTON_PAGE_TWO_CHECKOUT_ID = "finish"
    THANK_YOU_ORDER_COMPLETE_MESSAGE_CLASS_NAME = "complete-header"

    def click_checkout_button(self):
        self.click_element_after_wait("id", self.CHECKOUT_BUTTON_ID)

    def enter_first_name(self, first_name):
        self.send_keys_to_element_after_wait(first_name, "id", self.FIRST_NAME_CHECKOUT_ID)

    def enter_last_name(self, last_name):
        self.send_keys_to_element_after_wait(last_name, "id", self.LAST_NAME_CHECKOUT_ID)

    def enter_postal_code(self, postal_code):
        self.send_keys_to_element_after_wait(postal_code, "id", self.POSTAL_CODE_CHECKOUT_ID)

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue_button_in_checkout(self):
        self.click_element_after_wait("id", self.CONTINUE_BUTTON_PAGE_ONE_CHECKOUT_ID)

    def verify_items_are_in_checkout_overview(self):
        cart_items = self.wait_for_presence_of_all_elements_to_be_located("class_name", self.CART_ITEMS_CLASS_NAME)
        if len(cart_items) <= 6:
            print("Items are successfully showing in Checkout Review page and are purchasable")
            return True
        else:
            return False

    def click_finish_button(self):
        self.click_element_after_wait("id", self.FINISH_BUTTON_PAGE_TWO_CHECKOUT_ID)

    def verify_checkout_completed(self):
        actual_checkout_message = self.wait_for_element_to_be_visible("class_name", self.THANK_YOU_ORDER_COMPLETE_MESSAGE_CLASS_NAME).text
        expected_checkout_message = "Thank you for your order!"
        return self.utils.verify_text_contains(actual_checkout_message, expected_checkout_message)


