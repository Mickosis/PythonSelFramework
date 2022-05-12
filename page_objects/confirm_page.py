from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    terms_and_conditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def input_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def click_india(self):
        return self.driver.find_element(*ConfirmPage.india)

    def confirm_terms(self):
        return self.driver.find_element(*ConfirmPage.terms_and_conditions)

    def submit_order(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def verify_success(self):
        return self.driver.find_element(*ConfirmPage.success_message)