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

    LOGIN_EMAIL_FIELD = ("xpath", "//input[@name='login']")
    LOGIN_PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[1]")
    LOGIN_NOW_BUTTON = ("xpath", "//input[@value='Авторизоваться']")

    @allure.step("Enter username for registration")
    def input_registration_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_USERNAME_FIELD)).send_keys(username)

    @allure.step("Enter email for registration")
    def input_registration_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_EMAIL_FIELD)).send_keys(email)

    @allure.step("Enter password for registration")
    def input_registration_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_PASSWORD_FIELD)).send_keys(password)

    @allure.step("Press registration button")
    def press_registration_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_NOW_BUTTON)).click()


    @allure.step("Enter email for login")
    def input_login_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_EMAIL_FIELD)).send_keys(email)

    @allure.step("Enter password for login")
    def input_login_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_PASSWORD_FIELD)).send_keys(password)

    @allure.step("Press login button")
    def press_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_NOW_BUTTON)).click()
