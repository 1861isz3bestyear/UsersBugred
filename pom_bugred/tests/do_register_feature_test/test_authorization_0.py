import allure
from authorization_base import TestAuthorizationBase


class TestAuthorizationSuccess(TestAuthorizationBase):
    @allure.title("Register new user. All parametres (Username, Email, Password) are valid")
    @allure.severity("Critical")
    def test_succesfull_authorization(self):
        self.execute_authorization_preconditions()
        self.enter_username()
        self.enter_email()
        self.enter_password()
        self.press_registration_button()
        self.check_authorization_success()
