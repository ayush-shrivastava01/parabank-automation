from pages.login_page import LoginPage
from pages.accounts_overview_page import AccountsOverviewPage
from utils.test_data import USERNAME, PASSWORD


def open_accounts_overview(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    return AccountsOverviewPage(driver)


def test_accounts_overview(driver):
    accounts_page = open_accounts_overview(driver)

    assert accounts_page.is_accounts_overview_displayed()


def test_accounts_overview_title(driver):
    open_accounts_overview(driver)

    assert "Accounts Overview" in driver.page_source


def test_accounts_table_present(driver):
    accounts_page = open_accounts_overview(driver)

    table = driver.find_element(
        *accounts_page.ACCOUNTS_TABLE
    )

    assert table.is_displayed()