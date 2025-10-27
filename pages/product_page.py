from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()

    def should_be_productname_message(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ), "Message with product name is not found"

    def should_be_price_message(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE
        ), "Message with product price is not found"

    def should_be_the_right_productname_in_message(self):
        product_name_msg = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_msg == product_name, "Wrong product name in message"

    def should_be_the_right_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        product_price_msg = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE
        ).text
        assert (
            product_price == product_price_msg
        ), "Wrong product price (basket price) in message"
