from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BillPayPage(BasePage):

    PAYEE_NAME = (By.NAME, "payee.name")
    ADDRESS = (By.NAME, "payee.address.street")
    CITY = (By.NAME, "payee.address.city")
    STATE = (By.NAME, "payee.address.state")
    ZIP_CODE = (By.NAME, "payee.address.zipCode")
    PHONE = (By.NAME, "payee.phoneNumber")
    ACCOUNT = (By.NAME, "payee.accountNumber")
    VERIFY_ACCOUNT = (By.NAME, "verifyAccount")
    AMOUNT = (By.NAME, "amount")
    SEND_PAYMENT = (By.XPATH, "//input[@value='Send Payment']")

    def pay_bill(self, name, address, city, state, zip_code,
                 phone, account, amount):

        self.enter_text(self.PAYEE_NAME, name)
        self.enter_text(self.ADDRESS, address)
        self.enter_text(self.CITY, city)
        self.enter_text(self.STATE, state)
        self.enter_text(self.ZIP_CODE, zip_code)
        self.enter_text(self.PHONE, phone)
        self.enter_text(self.ACCOUNT, account)
        self.enter_text(self.VERIFY_ACCOUNT, account)
        self.enter_text(self.AMOUNT, amount)

        self.click(self.SEND_PAYMENT)