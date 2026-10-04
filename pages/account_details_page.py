from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountDetailsPage(BasePage):

    ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, 'activity.htm')]")
    TRANSACTION_TABLE = (By.ID, "transactionTable")

    def open_account(self):
        self.click(self.ACCOUNT_LINK)

    def is_transaction_table_displayed(self):
        return self.wait.until(
            lambda driver: driver.find_element(
                *self.TRANSACTION_TABLE
            ).is_displayed()
        )