# ParaBank Test Automation

A Selenium + Python + Pytest automation framework built for testing the
[ParaBank](https://parabank.parasoft.com/parabank/index.htm) online banking demo application.

The project focuses on practical QA automation concepts such as Page Object Model,
explicit waits, Pytest parameterization, reusable test data, logging, failure
screenshots, and HTML test reporting.

## Project Highlights

- 26 automated test cases
- Page Object Model (POM)
- Selenium WebDriver with Python
- Pytest framework
- Explicit waits
- Parameterized test cases
- Automatic test-user creation
- Reusable page actions and login helper
- Failure screenshots
- Execution logging
- HTML test reports

## Tech Stack

| Tool / Technology | Usage |
|---|---|
| Python | Test automation language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML test reports |
| Chrome / ChromeDriver | Browser execution |
| Git / GitHub | Version control and project hosting |

## Application Under Test

**ParaBank** is a publicly available banking demo application used for
automation practice.

The automated tests cover the following workflows:

- User Registration
- Login
- Accounts Overview
- Open New Account
- Fund Transfer
- Bill Payment
- Account / Transaction Details

## Test Coverage

| Module | Tests |
|---|---:|
| Registration | 4 |
| Login | 5 |
| Accounts Overview | 3 |
| Open Account | 3 |
| Transfer Funds | 4 |
| Bill Pay | 4 |
| Account Details | 3 |
| **Total** | **26** |

Some repetitive scenarios are implemented using Pytest parameterization,
for example different account types and different transfer/payment amounts.

## Framework Structure

```text
parabank-automation/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── accounts_overview_page.py
│   ├── open_account_page.py
│   ├── transfer_funds_page.py
│   ├── bill_pay_page.py
│   └── account_details_page.py
│
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_accounts_overview.py
│   ├── test_open_account.py
│   ├── test_transfer_funds.py
│   ├── test_bill_pay.py
│   └── test_account_details.py
│
├── utils/
│   ├── logger.py
│   ├── login_helper.py
│   └── test_data.py
│
├── screenshots/
├── reports/
├── logs/
├── conftest.py
├── requirements.txt
└── README.md
```

## Framework Design

The project uses the **Page Object Model (POM)** to keep page-specific
locators and actions separate from test cases.

### Base Page

`pages/base_page.py` contains reusable Selenium operations such as:

- Clicking elements
- Entering text
- Reading element text
- Waiting for elements using explicit waits

### Page Objects

Each major ParaBank workflow has its own page class.

For example:

```text
LoginPage
RegisterPage
OpenAccountPage
TransferFundsPage
BillPayPage
AccountDetailsPage
```

This keeps the test code cleaner and makes locators and page actions easier
to maintain.

### Test Data

Common test data is maintained in:

```text
utils/test_data.py
```

The framework generates a unique username for the automated test account,
which avoids relying on one permanently stored demo account.

### Reusable Login

Common login steps are kept in:

```text
utils/login_helper.py
```

This avoids repeating the same login setup in multiple test modules.

## Logging

Basic execution logging is implemented using Python's `logging` module.

The log file is generated at:

```text
logs/automation.log
```

The logs capture useful framework actions such as element clicks and
text-entry operations without recording actual passwords.

## Failure Screenshots

The framework automatically captures a screenshot when a test fails.

Screenshots are stored in:

```text
screenshots/
```

The screenshot filename is based on the failed test name.

## HTML Test Reports

The project uses `pytest-html` to generate an HTML execution report.

Run:

```bash
pytest -v --html=reports/test_report.html --self-contained-html
```

The report is generated at:

```text
reports/test_report.html
```

It can be opened in a browser to review the test results.

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd parabank-automation
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Tests

### Run the complete test suite

```bash
pytest -v
```

### Run a specific test file

```bash
pytest -v tests/test_login.py
```

### Run a specific test

```bash
pytest -v tests/test_login.py::test_valid_login
```

### Generate an HTML report

```bash
pytest -v --html=reports/test_report.html --self-contained-html
```

## Test Automation Features

This project demonstrates the following QA automation concepts:

- Selenium WebDriver
- Page Object Model
- Pytest fixtures
- Explicit waits
- Assertions
- Parameterization
- Reusable helper functions
- Dynamic test data
- Failure screenshots
- Logging
- HTML reporting

## Notes

ParaBank is a public demo application rather than a production banking
system. Because it is a shared demo environment, application behavior and
test data can occasionally change between test runs.

The project is intended to demonstrate the structure and implementation of
a practical Selenium automation framework rather than production banking
testing.

## Author

**Ayush Shrivastava**

B.Tech Computer Science and Engineering
