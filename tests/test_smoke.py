from selenium.webdriver.common.by import By


def test_parabank_homepage_loads(driver):
    driver.get(
        "https://parabank.parasoft.com/parabank/index.htm"
    )

    assert "ParaBank" in driver.title


def test_login_form_is_available(driver):
    driver.get(
        "https://parabank.parasoft.com/parabank/index.htm"
    )

    assert driver.find_element(By.NAME, "username").is_displayed()
    assert driver.find_element(By.NAME, "password").is_displayed()


def test_registration_page_loads(driver):
    driver.get(
        "https://parabank.parasoft.com/parabank/register.htm"
    )

    assert "Register" in driver.page_source