from playwright.sync_api import Page, expect
import logging
from utils.config_loader import Config
import os

config = Config()


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        # self.base_url = config.get("base_url")
        self.base_url = os.getenv('BASE_URL')

    def go_to_url(self, path: str=""):
        """Navigate to base_url + optional path"""
        url = f"{self.base_url}{path}"
        logging.info(f"Navigating to: {url}")
        self.page.goto(url)

    def fill_textfield(self, locator, text):
        locator.fill(text)

    def click_element(self, locator):
        locator.click()

    def get_element_text(self, locator):
        return locator.inner_text().strip()

    def verify_element_visible(self, locator):
        expect(locator).to_be_visible()

    def verify_element_visible(self, locator):
        expect(locator).to_be_visible()

    def get_element_link(self, locator):
        # Get href attribute
        href = locator.get_attribute("href")
        if href:
            return href.strip()
        else:
            logging.warning(f"No href found for locator: {locator}")
            return ""

    def get_row_data(self, bean_factory, test_case_id):
        try:
            index = bean_factory.test_case_IDs.index(test_case_id)
            row_data = {}
            for attr_name in vars(bean_factory):
                if attr_name == "BeanFactory":
                    continue
                attr_value = getattr(bean_factory, attr_name)
                if isinstance(attr_value, list) and len(attr_value) > index:
                    row_data[attr_name] = attr_value[index]
            return row_data
        except ValueError:
            return None

    def get_test_data(self, bean_factory, test_case_IDs):
        row_data = self.get_row_data(bean_factory, test_case_IDs)
        if row_data is None:
            import pytest
            pytest.fail(f"Test Case ID {test_case_IDs} not found in Excel.")
        print(row_data)
        return row_data