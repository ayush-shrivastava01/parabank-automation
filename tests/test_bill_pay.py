import pytest

from pages.login_page import LoginPage
from pages.bill_pay_page import BillPayPage
from utils.test_data import USERNAME, PASSWORD


def login(driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    driver.get("https://parabank.parasoft.com/parabank/billpay.htm")


@pytest.mark.parametrize(
    "payee_name, amount",
    [
        ("Electricity Company", "50"),
        ("Water Company", "1"),
        ("Internet Company", "500"),
        ("Electricity Company", "0"),
    ]
)
def test_bill_payment(driver, payee_name, amount):
    login(driver)

    bill_pay = BillPayPage(driver)

    bill_pay.pay_bill(
        payee_name,
        "123 Main Street",
        "Jaipur",
        "Rajasthan",
        "302001",
        "9876543210",
        "12345",
        amount
    )

    assert "Bill Payment Complete" in driver.page_source