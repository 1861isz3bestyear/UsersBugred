import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class UsersPage(BasePage):
    PAGE_URL = Links.USERS_PAGE

    BUTTON_FOR_AUTHORIZATION_PAGE = ("xpath", "//a[@href='/user/login/index.html']")

    AUTHORIZED_USER_TOGGLE = ("xpath", "//a[@href='#']")


    @allure.step("Click 'Authorization button link'")
    def click_authorization_button(self):
        self.wait.until(EC.element_to_be_clickable(self. BUTTON_FOR_AUTHORIZATION_PAGE)).click()

    @allure.step("Click 'Authorized toggle bar'")
    def click_authorized_user_toggle(self):
        self.wait.until(EC.element_to_be_clickable(self.AUTHORIZED_USER_TOGGLE)).click()
