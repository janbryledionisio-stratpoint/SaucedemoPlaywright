import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from beanFactory.login_bean_factory import LoginBeanFactory
import pandas as pd

beanFactory = LoginBeanFactory()

testCaseIDs = beanFactory.test_case_IDs


def clean(value):
    if pd.isna(value):
        return ""
    return value

@pytest.mark.parametrize("testCaseID", testCaseIDs)
def test_login(page, testCaseID):

    base_page = BasePage(page)
    login = LoginPage(page)

    row_data = base_page.get_test_data(
        beanFactory,
        testCaseID
    )

    username = clean(row_data.get("username"))
    password = clean(row_data.get("password"))
    error_message = clean(row_data.get("error_message"))

    print("Username :", username)
    print("Password :", password)
    print("ErrorMessage:", error_message)

    if error_message:

        login.unsuccessful_login(
            username,
            password,
            error_message
        )

    else:

        login.successful_login(
            username,
            password
        )