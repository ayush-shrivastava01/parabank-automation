import uuid

from pages.register_page import RegisterPage


def open_registration(driver):
    driver.get(
        "https://parabank.parasoft.com/parabank/register.htm"
    )
    return RegisterPage(driver)


def test_user_registration(driver):
    register_page = open_registration(driver)

    username = "user" + uuid.uuid4().hex[:12]

    print("Testing username:", username)

    register_page.register(
        "Ayush",
        "Shrivastava",
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "123456789",
        username,
        "Test@123"
    )

    assert "Welcome" in driver.page_source


def test_registration_missing_first_name(driver):
    register_page = open_registration(driver)

    username = "user" + uuid.uuid4().hex[:12]

    register_page.register(
        "",
        "Shrivastava",
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "123456789",
        username,
        "Test@123"
    )

    assert "First name is required." in driver.page_source


def test_registration_password_mismatch(driver):
    register_page = open_registration(driver)

    username = "user" + uuid.uuid4().hex[:12]

    register_page.register(
        "Ayush",
        "Shrivastava",
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "123456789",
        username,
        "Test@123",
        "WrongPassword"
    )

    assert "Passwords did not match." in driver.page_source


def test_registration_duplicate_username(driver):
    register_page = open_registration(driver)

    register_page.register(
        "Ayush",
        "Shrivastava",
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "123456789",
        "ayush_auto_20261004",
        "Test@123"
    )

    assert "This username already exists." in driver.page_source