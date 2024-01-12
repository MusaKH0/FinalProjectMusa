import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger_config import logger_setup
from utilities.utils import Utils


class CustomDriver:

    def __init__(self, driver):
        self.driver = driver
        self.log = logger_setup(__name__)
        self.utils = Utils()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        else:
            self.log.error(f"Locator Type: {locator_type} is not correct/supported")
        return False

    def wait_for_element_to_be_visible(self, locator_type, locator, timeout=15, poll_frequency=.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info(f"waiting for maximum :: {str(timeout)} :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            self.log.info(f"Element appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except:
            self.log.error(f"Element did NOT appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        self.driver.implicitly_wait(3)
        return element

    def wait_for_presence_of_element_to_be_located(self, locator_type, locator, timeout=15, poll_frequency=.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info(f"waiting for maximum :: {str(timeout)} :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = wait.until(EC.presence_of_element_located((by_type, locator)))
            self.log.info(f"Element appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except:
            self.log.error(f"Element did NOT appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        self.driver.implicitly_wait(3)
        return element

    def wait_for_all_elements_to_be_visible(self, locator_type, locator, timeout=15, poll_frequency=.5):
        elements = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info(f"waiting for maximum :: {str(timeout)} :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            elements = wait.until(EC.visibility_of_all_elements_located((by_type, locator)))
            self.log.info(f"Element appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except:
            self.log.error(f"Element did NOT appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        self.driver.implicitly_wait(3)
        return elements

    def wait_for_presence_of_all_elements_to_be_located(self, locator_type, locator, timeout=15, poll_frequency=.5):
        elements = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info(f"waiting for maximum :: {str(timeout)} :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            elements = wait.until(EC.presence_of_all_elements_located((by_type, locator)))
            self.log.info(f"Element appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except:
            self.log.error(f"Element did NOT appeared on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        self.driver.implicitly_wait(3)
        return elements

    def wait_for_element_to_be_clickable(self, locator_type, locator, timeout=15, poll_frequency=.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info(f"Wait a maximum of :: {str(timeout)} :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotInteractableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info(f"Element is clickable on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except:
            self.log.error(f"Element is NOT clickable on the webpage, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        self.driver.implicitly_wait(3)
        return element

    def click_element_after_wait(self, locator_type, locator):
        try:
            element = self.wait_for_element_to_be_clickable(locator_type, locator)
            element.click()
            self.log.info(f"Clicked element on the webpage after wait, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")
        except NoSuchElementException:
            self.log.error(f"Did NOT clicked element on the webpage after wait, using Locator_Type -- {locator_type} -- and Locator -- {locator} --")

    def send_keys_to_element_after_wait(self, data, locator_type, locator, clear=True):
        try:
            element = self.wait_for_element_to_be_visible(locator_type, locator)
            if clear:
                element.click()
                element.clear()
                element.send_keys(data)
            self.log.info(f"Typed :: {data} :: into Element with locator type: -- {locator_type} -- and locator: -- {locator} --")
        except NoSuchElementException:
            self.log.error(f"Did NOT type :: {data} :: into Element with locator type: -- {locator_type} -- and locator: -- {locator} --")

    def take_screenshot(self):
        folder_name = "../screenshots/"
        destination_directory = self.utils.create_directory(folder_name)
        timestamp = time.strftime("%Y-%m-%d_%I-%M-%S-%p")
        filename = f"screenshot_{timestamp}.png"
        destination_file = os.path.join(destination_directory, filename)
        self.driver.save_screenshot(destination_file)
















