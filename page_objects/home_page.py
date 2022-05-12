from selenium.webdriver.common.by import By

from page_objects.checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    ice_cream_checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def name_text_box(self):
        return self.driver.find_element(*HomePage.name)

    def email_text_box(self):
        return self.driver.find_element(*HomePage.email)

    def password_text_box(self):
        return self.driver.find_element(*HomePage.password)

    def tick_checkbox(self):
        return self.driver.find_element(*HomePage.ice_cream_checkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def click_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def verify_success(self):
        return self.driver.find_element(*HomePage.success_message)