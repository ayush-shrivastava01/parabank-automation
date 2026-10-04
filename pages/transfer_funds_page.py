from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TransferFundsPage(BasePage):

    AMOUNT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")

    def transfer_funds(self, amount):

        self.enter_text(self.AMOUNT, amount)

        # Wait until accounts are loaded
        self.wait.until(
            lambda driver: len(
                Select(driver.find_element(*self.FROM_ACCOUNT)).options
            ) > 0
        )

        self.wait.until(
            lambda driver: len(
                Select(driver.find_element(*self.TO_ACCOUNT)).options
            ) > 0
        )

        from_account = Select(
            self.driver.find_element(*self.FROM_ACCOUNT)
        )

        to_account = Select(
            self.driver.find_element(*self.TO_ACCOUNT)
        )

        # Select available accounts
        from_account.select_by_index(0)

        if len(to_account.options) > 1:
            to_account.select_by_index(1)
        else:
            to_account.select_by_index(0)

        self.click(self.TRANSFER_BUTTON)