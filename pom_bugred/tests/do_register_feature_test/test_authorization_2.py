import allure
from authorization_base import TestAuthorizationBase

class TestAuthorizationFail_2(TestAuthorizationBase):
    @allure.title("Register new failed user. Email is busy. Username and password are valid")
    @allure.severity("Critical")
    def test_failed_authorization_2(self):
        self.execute_authorization_preconditions()
        self.enter_vacant_username()
        self.enter_email()
        self.enter_password()
        self.press_registration_button()
        self.check_authorization_fail
