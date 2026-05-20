from playwright.sync_api import expect

from locators.dashboard_page_locators import DashboardPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.login = LoginPageLocators(page)
        self.dashboard = DashboardPageLocators(page)

    def login_action(self, username: str, password: str):
        self.go_to_url()
        self.fill_textfield(self.login.username_field, username)
        self.fill_textfield(self.login.password_field, password)
        self.click_element(self.login.login_button)

    def successful_login(self, username: str, password: str):
        self.login_action(username, password)
        expect(self.dashboard.inventory_container.first).to_be_visible()

    def unsuccessful_login(self, username: str, password: str, error_message: str):
        self.login_action(username, password)
        expect(self.login.error_message).to_contain_text(error_message)
