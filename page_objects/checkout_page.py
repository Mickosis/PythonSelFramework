from selenium.webdriver.common.by import By

from page_objects.confirm_page import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_titles = (By.XPATH, "//div[@class='card h-100']")
    card_footer = (By.XPATH, "div/button")
    check_out = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirm_check_out = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_titles)

    def get_card_footer(self):
        return self.driver.find_element(*CheckoutPage.card_footer)

    def check_out_items(self):
        return self.driver.find_element(*CheckoutPage.check_out)

    def check_out_confirm(self):
        self.driver.find_element(*CheckoutPage.confirm_check_out).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
