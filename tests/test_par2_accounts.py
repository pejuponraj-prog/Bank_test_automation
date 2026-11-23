import pytest
from playwright.sync_api import Page, expect

from pages.accounts_page import AccountsPage
from pages.login import LoginPage
@pytest.fixture()
def accounts_page(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("john", "demo123")
    accounts=AccountsPage(page)
    accounts.open()
    return accounts

def test_tc1_title(accounts_page):
    expect(accounts_page.title).to_be_visible()

def test_tc3_account_details(accounts_page):
    expect(accounts_page.balance(10000001)).to_have_text("£1,000.00")
    expect(accounts_page.balance(10000002)).to_have_text("£5,000.00")
   

def test_tc7_total(accounts_page):
    expect(accounts_page.total).to_have_text("£6,000.00")
def test_tc10_only_own_accounts(accounts_page):
    expect(accounts_page.account_rows).to_have_count(2)
def test_t12_canot_open_history_of_other_account(accounts_page):
    accounts_page.page.goto("/history/3")
    expect(accounts_page.page.get_by_text("Account not found")).to_be_visible()