import allure
from do_login_base import DoLoginBase

class TestDoLoginFail_1(DoLoginBase):
    @allure.title("Test failed Do Login. Email is empty. Password is valid (from user in system)")
    @allure.severity("Critical")
    def test_failed_do_login_1(self):
        self.execute_login_preconditions()
        self.enter_empty_email()
        self.enter_password()
        self.press_login_button()
        self.check_dologin_fail
