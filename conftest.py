import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.register_page import RegisterPage
from utils.test_data import USERNAME, PASSWORD


def create_chrome_driver():
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope="session")
def test_user():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }


@pytest.fixture
def driver(request):
    driver = create_chrome_driver()

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
    driver = create_chrome_driver()

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