from webbrowser import Chrome

from playwright.sync_api import sync_playwright
from utils.config_loader import Config

config = Config()

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None

    def start_browser(self):
        self.playwright = sync_playwright().start()
        browser_type = config.get("browser", "type", default="chrome")
        headless = config.get("browser", "headless", default=True)

        if browser_type == "chrome":
            self.browser = self.playwright.chromium.launch(headless = headless)
        elif browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless = headless)
        elif browser_type == "safari":
            self.browser = self.playwright.webkit.launch(headless = headless)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        return self.browser

    def stop_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def new_context(self, **kwargs):
        """
        Create a new browser context. You can pass kwargs like viewport, storage_state, etc.
        """
        return self.browser.new_context(**kwargs)