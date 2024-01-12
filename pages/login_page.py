from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.utils import Utils


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utils = Utils()

    # Locators
    USERNAME_ID = "user-name"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_ID = "login-button"
    PRODUCT_PAGE_TITLE_XPATH = "//span[@class='title']"
    ERROR_MESSAGE_BOX_XPATH = "//div[@class='error-message-container error']"

    def enter_valid_username(self, username):
        self.send_keys_to_element_after_wait(username, "id", self.USERNAME_ID)

    def enter_valid_password(self, password):
        self.send_keys_to_element_after_wait(password, "id", self.PASSWORD_ID)

    def click_login_button(self):
        self.click_element_after_wait("id", self.LOGIN_BUTTON_ID)

    def login(self, username, password):
        self.enter_valid_username(username)
        self.enter_valid_password(password)
        self.click_login_button()

    def verify_login_is_successful(self):
        actual_message = self.driver.find_element(By.XPATH, self.PRODUCT_PAGE_TITLE_XPATH).text
        expected_message = "Products"
        result = self.utils.verify_text_contains(actual_message, expected_message)
        if result == True:
            print("### Successfully logged in with valid credentials")
            return True

    def verify_invalid_credentials(self):
        if self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text in "Epic sadface: Username and password do not match any user in this service":
            print("Invalid username and password")
            actual_message = self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text
            expected_message = "Epic sadface: Username and password do not match any user in this service"
            return self.utils.verify_text_contains(actual_message, expected_message)
        if self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text in "Epic sadface: Password is required":
            print("Invalid password")
            actual_message = self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text
            expected_message = "Epic sadface: Password is required"
            return self.utils.verify_text_contains(actual_message, expected_message)
        if self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text in "Epic sadface: Username is required":
            print("Invalid username")
            actual_message = self.driver.find_element(By.XPATH, self.ERROR_MESSAGE_BOX_XPATH).text
            expected_message = "Epic sadface: Username is required"
            return self.utils.verify_text_contains(actual_message, expected_message)
