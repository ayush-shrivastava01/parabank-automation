from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")

    def register(self, first_name, last_name, address, city,
                 state, zip_code, phone, ssn, username,
                 password, confirm_password=None):

        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.ADDRESS, address)
        self.enter_text(self.CITY, city)
        self.enter_text(self.STATE, state)
        self.enter_text(self.ZIP_CODE, zip_code)
        self.enter_text(self.PHONE, phone)
        self.enter_text(self.SSN, ssn)
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)

        if confirm_password is None:
            confirm_password = password

        self.enter_text(self.CONFIRM_PASSWORD, confirm_password)

        self.click(self.REGISTER_BUTTON)