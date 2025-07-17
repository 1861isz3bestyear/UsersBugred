import allure
from do_login_base import DoLoginBase

class TestDoLoginSuccess(DoLoginBase):
    @allure.title("Login user. All parametres(Email, Password) are valid")
    @allure.severity("Critical")
    def test_successfull_do_login(self):
        self.execute_login_preconditions()
        self.enter_email()
        self.enter_password()
        self.press_login_button()
        self.check_dologin_success()
