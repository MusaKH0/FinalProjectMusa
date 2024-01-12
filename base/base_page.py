from base.custom_driver import CustomDriver


class BasePage(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SHOPPING_CART_CLASS_NAME = "shopping_cart_link"
    SHOPPING_CART_BADGE_CLASS_NAME = "shopping_cart_badge"
    BURGER_MENU_BUTTON_ID = "react-burger-menu-btn"
    LOGOUT_SIDEBAR_LINK_ID = "logout_sidebar_link"

    def logout(self):
        self.click_element_after_wait("id", self.BURGER_MENU_BUTTON_ID)
        self.click_element_after_wait("id", self.LOGOUT_SIDEBAR_LINK_ID)

