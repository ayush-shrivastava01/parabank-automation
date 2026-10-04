from pages.login_page import LoginPage
from pages.account_details_page import AccountDetailsPage
from utils.test_data import USERNAME, PASSWORD


def open_account_details(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    account_page = AccountDetailsPage(driver)
    account_page.open_account()

    return account_page


def test_account_transaction_details(driver):
    account_page = open_account_details(driver)

    assert account_page.is_transaction_table_displayed()


def test_account_details_page_loaded(driver):
    open_account_details(driver)

    assert "Account Activity" in driver.page_source


def test_transaction_table_contains_data(driver):
    account_page = open_account_details(driver)

    transaction_table = driver.find_element(
        *account_page.TRANSACTION_TABLE
    )

    assert transaction_table.is_displayed()