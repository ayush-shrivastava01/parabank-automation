from pages.login_page import LoginPage
from utils.test_data import USERNAME, PASSWORD


def open_login(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    return LoginPage(driver)


def test_valid_login(driver):
    login_page = open_login(driver)
    login_page.login(USERNAME, PASSWORD)

    assert "Accounts Overview" in driver.page_source


def test_invalid_password(driver):
    login_page = open_login(driver)
    login_page.login(USERNAME, "WrongPassword123")

    assert "The username and password could not be verified." in driver.page_source


def test_invalid_username(driver):
    login_page = open_login(driver)
    login_page.login("invalid_user_xyz_999", "WrongPassword123")

    assert "The username and password could not be verified." in driver.page_source


def test_empty_username(driver):
    login_page = open_login(driver)
    login_page.login("", PASSWORD)

    assert "Please enter a username and password." in driver.page_source


def test_empty_password(driver):
    login_page = open_login(driver)
    login_page.login(USERNAME, "")

    assert "Please enter a username and password." in driver.page_source