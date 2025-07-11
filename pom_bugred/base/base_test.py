import pytest
from config.data import Data
from pages.authorization_login_page import AuthorizationLoginPage
from pages.users_page import UsersPage


class BaseTest:

    data: Data

    authorization_login_page: AuthorizationLoginPage
    users_page: UsersPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.users_page = UsersPage(driver)
        request.cls.authorization_login_page = AuthorizationLoginPage(driver)
