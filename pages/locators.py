from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[href*='password-reset']")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASSWORD = (By.NAME, "registration-password1")
    REG_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REG_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
