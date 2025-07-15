import allure
from authorization_base import TestAuthorizationBase

class TestAuthorizationFail_3(TestAuthorizationBase):
    @allure.title("Register new failed user. Password is empty. Username and Email are valid")
    @allure.severity("Critical")
    def test_failed_authorization_3(self):
        self.execute_authorization_preconditions()
        self.enter_vacant_username()
        self.enter_vacant_email()
        self.enter_empty_password()
        self.press_registration_button()
        self.check_authorization_fail
