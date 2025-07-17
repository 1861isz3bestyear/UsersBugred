import allure
from base.base_test import BaseTest

@allure.feature("Do login functionality")
class DoLoginBase(BaseTest):
    def execute_login_preconditions(self):
        self.users_page.open()
        self.users_page.click_authorization_button()
        self.authorization_login_page.is_openned()

    def enter_email(self):
        self.authorization_login_page.input_login_email(self.data.EMAIL)

    def enter_empty_email(self):
        self.authorization_login_page.input_login_email(self.data.EMTY_DATA)

    def enter_password(self):
        self.authorization_login_page.input_login_password(self.data.PASSWORD)

    def enter_empty_password(self):
        self.authorization_login_page.input_login_password(self.data.EMTY_DATA)

    def press_login_button(self):
        self.authorization_login_page.press_login_button()

    def check_dologin_success(self):
        self.users_page.is_openned()
        self.users_page.click_authorized_user_toggle()

    def check_dologin_fail(self):
        self.authorization_login_page.is_openned()
