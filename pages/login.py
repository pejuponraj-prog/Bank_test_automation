from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username=page.locator('[data-test="username"]')
        self.password=page.locator('[data-test="password"]')
        self.login_button=page.locator('[data-test="login-button"]')
        self.error=page.locator('[data-test="login-error"]')

    def open(self):
        self.page.goto("/login")

    def login(self, user ,pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()

        
     