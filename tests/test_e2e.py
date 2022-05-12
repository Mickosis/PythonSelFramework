from selenium.webdriver.common.by import By

from page_objects.home_page import HomePage
from utilities.baseclass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()
        log.info("Getting all products")
        products = checkout_page.get_card_titles()
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            log.info(product_name)
            if product_name == "Blackberry":
                log.info("Product found")
                product.find_element(By.XPATH, "div/button").click()
        checkout_page.check_out_items().click()
        log.info("Checking out")
        confirm_page = checkout_page.check_out_confirm()
        log.info("Adding country")
        confirm_page.input_country().send_keys("ind")
        log.info("Country confirmed")
        self.verify_link_presence("India")
        confirm_page.click_india().click()
        confirm_page.confirm_terms().click()
        confirm_page.submit_order().click()
        success_text = confirm_page.verify_success().text
        assert "Success" in success_text
        # self.driver.get_screenshot_as_file("screen_result.png")
        log.info("Order verified")


