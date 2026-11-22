from playwright.sync_api import Page


class AccountsPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_role("heading", name="Accounts Overview")
        self.account_rows = page.locator('[data-test="account-row"]')
        self.total = page.locator('[data-test="total-balance"]')

    def open(self):
        self.page.goto("/accounts")

    def balance(self, account_number):
        return self.page.locator(
            f'[data-test="account-balance-{account_number}"]'
        )

    def history_link(self, account_number):
        return self.page.locator(f'[data-test="history-link-{account_number}"]')
