import allure
from do_login_base import DoLoginBase

class TestDoLoginFail_2(DoLoginBase):
    @allure.step("Test failed Do Login. Password is empty. Email is valid (from user in system)")
    @allure.severity("Critical")
    def test_failed_do_login_2(self):
        self.execute_login_preconditions()
        self.enter_email()
        self.enter_empty_password()
        self.press_login_button()
        self.check_dologin_fail
