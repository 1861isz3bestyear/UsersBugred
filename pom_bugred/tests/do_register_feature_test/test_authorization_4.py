import allure
from authorization_base import TestAuthorizationBase

class TestAuthorizationFail_4(TestAuthorizationBase):
    @allure.title("Register new failed user. Email is busy. Username and password are valid")
    @allure.severity("Critical")
    def test_failed_authorization_4(self):
        self.execute_authorization_preconditions()
        self.enter_empty_username()
        self.enter_vacant_email()
        self.enter_password()
        self.press_registration_button()
        self.check_authorization_fail
