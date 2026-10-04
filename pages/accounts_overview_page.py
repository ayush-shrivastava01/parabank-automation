from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountsOverviewPage(BasePage):

    ACCOUNTS_TABLE = (By.ID, "accountTable")

    def is_accounts_overview_displayed(self):
        return self.wait.until(
            lambda driver: driver.find_element(
                *self.ACCOUNTS_TABLE
            ).is_displayed()
        )