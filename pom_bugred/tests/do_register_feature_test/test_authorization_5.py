import allure
from authorization_base import TestAuthorizationBase

class TestAuthorizationFail_5(TestAuthorizationBase):
    @allure.title("Register new failed user. Every parameter is invalid")
    @allure.severity("Critical")
    def test_failed_authorization_5(self):
        self.execute_authorization_preconditions()
        self.enter_empty_username()
        self.enter_empty_email()
        self.enter_empty_password()
        self.press_registration_button()
        self.check_authorization_fail
