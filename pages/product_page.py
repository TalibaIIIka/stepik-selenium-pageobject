import math

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_CART), 'Button of cart was not found'
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_CART)
        btn_add_to_cart.click()

    def check_items_cart(self, title, price):
        assert title == self.browser.find_element(
            *ProductPageLocators.MSG_SUC_ADD_TO_CART).text, f'Item {title} was not found\n url: {self.browser.current_url}'

        fact_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_OF_BASKET).text
        assert price in fact_price, f'Price expected {price}, real {fact_price}'

    def get_price_of_item(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_ITEM).text
        return price

    def get_title_of_item(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE_OF_ITEM).text
        return title

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
