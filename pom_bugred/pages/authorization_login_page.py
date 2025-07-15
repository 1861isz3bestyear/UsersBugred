from pages import authorization_login_page
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationLoginPage(BasePage):
    PAGE_URL = Links.AUTHORIZATION_LOGIN_PAGE

    REGISTRATION_USERNAME_FIELD = ("xpath", "//input[@name='name']")
    REGISTRATION_EMAIL_FIELD = ("xpath", "//input[@name='email']")
    REGISTRATION_PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[2]")
    REGISTER_NOW_BUTTON = ("xpath", "//input[@value='Зарегистрироваться']")

    @allure.step("Enter username")
    def input_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_USERNAME_FIELD)).send_keys(username)

    @allure.step("Input email")
    def input_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_EMAIL_FIELD)).send_keys(email)

    @allure.step("Input password")
    def input_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_PASSWORD_FIELD)).send_keys(password)

    @allure.step("Press registration button")
    def press_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_NOW_BUTTON)).click()
