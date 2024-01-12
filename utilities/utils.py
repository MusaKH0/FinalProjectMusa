import os
import random
import string

from utilities.logger_config import logger_setup


class Utils:

    def __init__(self):
        self.log = logger_setup(__name__)

    def verify_text_contains(self, actual_text, expected_text):
        if actual_text in expected_text:
            self.log.info(f"!!! Verification Contains !!! --> {actual_text}")
            return True
        else:
            self.log.error(f"!!! Verification does NOT contain !!! --> {actual_text}")
            return False

    def get_alpha_numeric(self, length=10, type="letters"):
        '''
        Get random string of characters
        :param length: Length of string, number of characters
        :param type: type of characters, letters/upper/lower/digits/mix
        :return: string
        '''

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def create_directory(self, directory_name):
        current_directory = os.path.dirname(__file__)
        destination_directory = os.path.join(current_directory, directory_name)
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        return destination_directory




































