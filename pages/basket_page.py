from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_CARD_IN_BASKET), "Found at least one product card"

    def should_be_text_about_missing_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "'Basket is empty' message not found"