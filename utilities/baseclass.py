import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from page_objects import home_page


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('log_file.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s ")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

