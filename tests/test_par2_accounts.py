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
