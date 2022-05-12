import pytest
from selenium.webdriver.support.select import Select

from page_objects.home_page import HomePage
from test_data.home_page_data import HomePageData
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("Add first name " + get_data["firstname"])
        home_page.name_text_box().send_keys(get_data["firstname"])
        log.info("Add last name " + get_data["lastname"])
        home_page.email_text_box().send_keys(get_data["lastname"])
        # home_page.password_text_box().send_keys("Mico1234")
        log.info("Tick checkbox")
        home_page.tick_checkbox().click()
        log.info("Add gender " + get_data["gender"])
        self.select_option(home_page.select_gender(), get_data["gender"])
        log.info("Submit form")
        home_page.click_submit().click()
        log.info("Verifying success result")
        message = home_page.verify_success().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_excel_data(2))
    def get_data(self, request):
        return request.param
