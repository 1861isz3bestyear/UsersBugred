import allure
from base.base_test import BaseTest


@allure.feature("'Do_register' functionality.")
class TestAuthorizationBase(BaseTest):

    def execute_authorization_preconditions(self):
        self.users_page.open()
        self.users_page.click_authorization_button()
        self.authorization_login_page.is_openned()

    def enter_username(self):
        self.authorization_login_page.input_registration_username(self.data.USERNAME)

    def enter_vacant_username(self):
        self.authorization_login_page.input_registration_username(self.data.VACANT_USERNAME)

    def enter_empty_username(self):
        self.authorization_login_page.input_registration_username(self.data.EMTY_DATA)

    def enter_email(self):
        self.authorization_login_page.input_registration_email(self.data.EMAIL)

    def enter_vacant_email(self):
        self.authorization_login_page.input_registration_email(self.data.VACANT_EMAIL)

    def enter_empty_email(self):
        self.authorization_login_page.input_registration_email(self.data.EMTY_DATA)

    def enter_password(self):
        self.authorization_login_page.input_registration_password(self.data.PASSWORD)

    def enter_empty_password(self):
        self.authorization_login_page.input_registration_password(self.data.EMTY_DATA)

    def press_registration_button(self):
        self.authorization_login_page.press_registration_button()

    def check_authorization_success(self):
        self.users_page.is_openned()
        self.users_page.click_authorized_user_toggle()


    def check_authorization_fail(self):
        self.authorization_login_page.is_openned()

#НАПИСАТЬ ПРОВЕРКУ!!!!!!!!!!!!!!!!!!
