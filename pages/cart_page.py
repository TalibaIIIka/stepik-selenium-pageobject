from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def should_empty_msg_present(self):
        assert 'Your basket is empty.' in self.browser.find_element(*CartPageLocators.CONTENT_INNER).text, \
            'Basket is not empty'

    def should_not_be_items(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS), 'Should not be items in cart'
