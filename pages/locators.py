from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.NAME, "login-username_inv")
    LOGIN_PASSWORD = (By.NAME, "login-password_inv")
    LOGIN_FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, "password-reset_inv")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit_inv")
    REG_EMAIL = (By.NAME, "registration-email_inv")
    REG_PASSWORD = (By.NAME, "registration-password1_inv")
    REG_PASSWORD_CONFIRM = (By.NAME, "registration-password2_inv")
    REG_SUBMIT_BUTTON = (By.NAME, "registration_submit_inv")
