import pytest

from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage
from utils.test_data import USERNAME, PASSWORD


def open_account_page(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    driver.get("https://parabank.parasoft.com/parabank/openaccount.htm")

    return OpenAccountPage(driver)


@pytest.mark.parametrize("account_type", ["SAVINGS", "CHECKING"])
def test_open_account(driver, account_type):
    open_account = open_account_page(driver)

    open_account.open_account(account_type)

    new_account_id = open_account.get_new_account_id()

    assert new_account_id.isdigit()


def test_new_account_id_is_generated(driver):
    open_account = open_account_page(driver)

    open_account.open_account("SAVINGS")

    new_account_id = open_account.get_new_account_id()

    assert len(new_account_id) > 0
    assert new_account_id.isdigit()