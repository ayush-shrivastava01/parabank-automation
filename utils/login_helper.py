from pages.login_page import LoginPage
from utils.test_data import USERNAME, PASSWORD


def login(driver):
    driver.get(
        "https://parabank.parasoft.com/parabank/index.htm"
    )

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)