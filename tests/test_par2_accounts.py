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
@pytest.fixture()
def  accounts_page1(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("mary", "test123")
    accounts=AccountsPage(page)
    accounts.open()
    return accounts


def test_tc1_title(accounts_page):
    expect(accounts_page.title).to_be_visible()
def test_tc2_title(accounts_page1):
    expect(accounts_page1.title).to_be_visible()

def test_tc3_account_details(accounts_page):
    expect(accounts_page.balance(10000001)).to_have_text("£1,000.00")
    expect(accounts_page.balance(10000002)).to_have_text("£5,000.00")
def test_tc4_account_details(accounts_page1):
    expect(accounts_page1.balance(20000001)).to_have_text("£250.50")

   

def test_tc7_total(accounts_page):
    expect(accounts_page.total).to_have_text("£6,000.00")
def test_tc10_only_own_accounts(accounts_page):
    expect(accounts_page.account_rows).to_have_count(2)
def test_tc11_only_own_accounts(accounts_page1):
    expect(accounts_page1.account_rows).to_have_count(1)
def test_t12_canot_open_history_of_other_account(accounts_page):
    accounts_page.page.goto("/history/3")
    expect(accounts_page.page.get_by_text("Account not found")).to_be_visible()
def test_tc13_canot_open_history_of_other_account(accounts_page1):
    accounts_page1.page.goto("/history/1")
    expect(accounts_page1.page.get_by_text("Account not found")).to_be_visible()
def test_tc14_canot_open_history_of_other_account(accounts_page1):
    accounts_page1.page.goto("/history/2")
    expect(accounts_page1.page.get_by_text("Account not found")).to_be_visible()

def test_tc8_history_link(accounts_page):
    accounts_page.history_link(10000001).click()
    expect(accounts_page.page.get_by_role("heading", name="Transaction History")).to_be_visible()
    expect(accounts_page.page.locator('[data-test="history-account-number"]')).to_have_text("10000001")
    accounts_page.open()
    accounts_page.history_link(10000002).click()
    expect(accounts_page.page.get_by_role("heading", name="Transaction History")).to_be_visible()
    
    expect(accounts_page.page.locator('[data-test="history-account-number"]')).to_have_text("10000002")
def test_tc9_history_link(accounts_page1):
    accounts_page1.history_link(20000001).click()
    expect(accounts_page1.page.get_by_role("heading", name="Transaction History")).to_be_visible()
    expect(accounts_page1.page.locator('[data-test="history-account-number"]')).to_have_text("20000001")