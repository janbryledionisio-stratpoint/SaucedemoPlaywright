class LoginPageLocators:
    def __init__(self, page):

        # --- Login Page Section---
        self.username_field = page.locator("//input[@id='user-name']")
        self.password_field = page.locator("//input[@id='password']")
        self.login_button = page.locator("//input[@id='login-button']")
        self.error_message = page.locator("//h3[@data-test='error']")