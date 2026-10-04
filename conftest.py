import os

import pytest
from selenium import webdriver

from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.test_data import USERNAME, PASSWORD


@pytest.fixture(scope="session")
def test_user():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = os.path.join(
            "screenshots",
            f"{request.node.name}.png"
        )

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def create_test_user(test_user):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://parabank.parasoft.com/parabank/register.htm"
    )

    register_page = RegisterPage(driver)

    register_page.register(
        "Ayush",
        "Shrivastava",
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "123456789",
        test_user["username"],
        test_user["password"]
    )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)