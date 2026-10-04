from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OpenAccountPage(BasePage):

    ACCOUNT_TYPE = (By.ID, "type")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//input[@value='Open New Account']")
    NEW_ACCOUNT_ID = (By.ID, "newAccountId")

    def open_account(self, account_type="SAVINGS"):

        account_type_dropdown = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_TYPE)
        )

        Select(account_type_dropdown).select_by_visible_text(account_type)

        from_account_dropdown = self.wait.until(
            EC.visibility_of_element_located(self.FROM_ACCOUNT)
        )

        def get_account_option(driver):
            select = Select(
                driver.find_element(*self.FROM_ACCOUNT)
            )

            for option in select.options:
                text = option.text.strip()

                if text.isdigit():
                    return text

            return False

        account_number = self.wait.until(get_account_option)

        Select(
            self.driver.find_element(*self.FROM_ACCOUNT)
        ).select_by_visible_text(account_number)

        self.click(self.OPEN_ACCOUNT_BUTTON)

    def get_new_account_id(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.NEW_ACCOUNT_ID
            )
        ).text