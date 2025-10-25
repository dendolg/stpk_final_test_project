from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no 'login' in page url"

    def should_be_login_form(self):
        assert (
            self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
            * self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
            * self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_LINK)
            * self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        ), "One or few login form elements wasn't found"

    def should_be_register_form(self):
        assert (
            self.is_element_present(*LoginPageLocators.REG_EMAIL)
            * self.is_element_present(*LoginPageLocators.REG_PASSWORD)
            * self.is_element_present(*LoginPageLocators.REG_PASSWORD_CONFIRM)
            * self.is_element_present(*LoginPageLocators.REG_SUBMIT_BUTTON)
        ), "One or few register form elements wasn't found"
