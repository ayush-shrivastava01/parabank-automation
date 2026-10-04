Yes. You mean you want the **entire README as one single copy-paste block**, with all sections in the correct order.

Replace your entire `README.md` with this:

```markdown
# ParaBank Test Automation

Selenium + Python + Pytest automation framework for testing the ParaBank banking demo application.

## Project Overview

This project automates functional UI testing of the ParaBank application using Selenium WebDriver, Python, and Pytest.

The framework follows the Page Object Model (POM) to keep page-specific locators and actions separate from test cases.

## Application Under Test

ParaBank Banking Demo

https://parabank.parasoft.com/parabank/index.htm

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and fixtures |
| Page Object Model | Framework design |
| HTML Reports | Test execution reporting |
| Git/GitHub | Version control |
| GitHub Actions | Continuous Integration |

## Test Coverage

The automation suite contains 26 test cases covering:

| Module | Coverage |
|---|---|
| Registration | Valid registration, validation, password mismatch, duplicate username |
| Login | Valid login, invalid credentials, empty fields |
| Accounts Overview | Page loading and account table validation |
| Account Details | Account activity and transaction table |
| Open Account | Savings and checking account creation |
| Fund Transfer | Parameterized transfer scenarios |
| Bill Payment | Parameterized bill payment scenarios |

## Framework Structure

```text
parabank-automation/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── accounts_overview_page.py
│   ├── account_details_page.py
│   ├── open_account_page.py
│   ├── transfer_funds_page.py
│   └── bill_pay_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_accounts_overview.py
│   ├── test_account_details.py
│   ├── test_open_account.py
│   ├── test_transfer_funds.py
│   ├── test_bill_pay.py
│   └── test_smoke.py
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

The framework uses the Page Object Model (POM).

- Page classes contain locators and reusable page actions.
- Test files contain test scenarios and assertions.
- `BasePage` provides common Selenium operations and explicit waits.
- `conftest.py` manages Pytest fixtures, WebDriver setup, test-user creation, and failure screenshots.
- Utility modules provide reusable test data, logging, and login functionality.

## Test Data

Test data is maintained separately in:

```text
utils/test_data.py
```

The project generates a unique username for automated test-user creation to reduce conflicts during registration.

## Reusable Login

A reusable login helper is implemented in:

```text
utils/login_helper.py
```

This avoids repeating the same login steps across tests that require an authenticated session.

## Parameterized Testing

Pytest parameterization is used for scenarios such as:

- Different account types
- Different fund transfer amounts
- Different bill payment amounts

This allows the same test logic to be executed with multiple data sets.

## Explicit Waits

The framework uses Selenium `WebDriverWait` and expected conditions to wait for elements before interacting with them.

This helps reduce failures caused by elements not being immediately available.

## Logging

Execution logging is implemented using Python's `logging` module.

Logs are written to:

```text
logs/automation.log
```

The logger records important automation actions such as element interactions and text entry.

## Failure Screenshots

When a test fails, the Pytest fixture automatically captures a screenshot.

Screenshots are saved in:

```text
screenshots/
```

The screenshot filename corresponds to the failed test name.

## HTML Test Reports

Pytest HTML reporting is used to generate execution reports.

Example command:

```powershell
pytest -v --html=reports/test_report.html --self-contained-html
```

Reports are generated in:

```text
reports/
```

## Continuous Integration

The project is integrated with GitHub Actions for automated CI execution.

The CI workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Chrome.
5. Runs the smoke test suite using headless Chrome.
6. Generates an HTML test report.
7. Uploads the report as a GitHub Actions artifact.

The smoke tests are executed automatically when changes are pushed to the `main` branch or when a pull request targets `main`.

### CI Smoke Tests

The CI smoke suite contains three stable checks covering:

- ParaBank homepage availability
- Login form availability
- Registration page availability

The complete 26-test automation suite is maintained separately as the project's broader regression coverage and can be executed locally when required.

## Running the Tests

### 1. Clone the repository

```powershell
git clone https://github.com/ayush-shrivastava01/parabank-automation.git
cd parabank-automation
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run all tests

```powershell
pytest -v
```

### 6. Run a specific test module

Example:

```powershell
pytest -v tests/test_login.py
```

### 7. Run the smoke tests

```powershell
pytest -v tests/test_smoke.py
```

### 8. Generate an HTML report

```powershell
pytest -v --html=reports/test_report.html --self-contained-html
```

## Test Automation Features

- Page Object Model
- Explicit waits
- Parameterized test cases
- Reusable login utility
- Test data management
- Logging
- Automatic failure screenshots
- HTML test reports
- GitHub Actions CI integration
- Headless Chrome execution in CI
- Automated smoke testing on push and pull requests

## Notes

ParaBank is a publicly available demo banking application. Because it is an external demo environment, application state and behavior can occasionally vary between test executions.

The automation framework maintains the complete regression suite separately from the smaller CI smoke suite used for fast and reliable build validation.

## Author

**Ayush Shrivastava**

B.Tech — Computer Science and Engineering
NIMS University, Jaipur

GitHub:
https://github.com/ayush-shrivastava01

LinkedIn:
https://www.linkedin.com/in/ayush-shrivastava01/