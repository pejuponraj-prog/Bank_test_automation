import pytest
from playwright.sync_api import Page, expect
from pages.login import LoginPage

def test_tc1_login_page_fields(page: Page):
    login=LoginPage(page)
    login.open()
    expect(login.username).to_be_visible()
    expect(login.password).to_be_visible()
    expect(login.login_button).to_be_visible()

def test_tc2_valid_login(page: Page):
    login=LoginPage(page)
    login.open()
    login.login("john", "demo123")
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

def test_tc3_welcome_text(page: Page):
    login=LoginPage(page)
    login.open()
    login.login("john", "demo123")
    expect(page.locator('[data-test="welcome-text"]')).to_have_text("Welcome, John Smith")

@pytest.mark.parametrize("user, pwd", [
    ("john", "wrong123"), 
    ("ponraj", "demo123"),
    ("john", "Demo123") 
     ])
def test_tc4_tc5_invalid_login(page: Page, user, pwd):
    login = LoginPage(page)
    login.open()
    login.login(user, pwd)
    expect(login.error).to_have_text("Invalid username or password")

@pytest.mark.xfail(reason="Bug PAR-20")
@pytest.mark.parametrize("user, pwd", [
    ("JOHN", "demo123"), 
    ("JohN", "demo123") 
    ])
def test_tc6_tc7_username_case_insensitive(page: Page, user, pwd):
    login = LoginPage(page)
    login.open()
    login.login(user, pwd)
    expect(page.get_by_role("heading", name="Accounts Overview")).to_be_visible()


def test_tc8_logout(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("john","demo123")
    page.locator('[data-test="nav-logout"]').click()
    expect(page.locator('[data-test="flash-message"]')).to_have_text("You have been logged out")
    expect(login.login_button).to_be_visible()


def test_tc9_account_after_logout(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("john","demo123")
    page.locator('[data-test="nav-logout"]').click()
    page.goto("/accounts")
    expect(page.get_by_role("heading", name="Customer Login")).to_be_visible()




















