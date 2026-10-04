import pytest

from pages.transfer_funds_page import TransferFundsPage
from utils.login_helper import login


@pytest.mark.parametrize("amount", ["100", "1", "500", "0"])
def test_transfer_funds(driver, amount):
    login(driver)

    driver.get(
        "https://parabank.parasoft.com/parabank/transfer.htm"
    )

    transfer_page = TransferFundsPage(driver)
    transfer_page.transfer_funds(amount)

    assert "Transfer Complete" in driver.page_source