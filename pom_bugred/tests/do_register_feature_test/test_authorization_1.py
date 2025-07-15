import allure
from authorization_base import TestAuthorizationBase

class TestAuthorizationFail_1(TestAuthorizationBase):
    @allure.title("Register new failed user. Username is busy. Email and password are valid")
    @allure.severity("Critical")
    def test_failed_authorization_1(self):
        self.execute_authorization_preconditions()
        self.enter_username()
        self.enter_vacant_email()
        self.enter_password()
        self.press_registration_button()
        self.check_authorization_fail
