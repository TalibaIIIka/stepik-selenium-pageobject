from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    MSG_SUC_ADD_TO_CART = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    TITLE_OF_ITEM = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE_OF_ITEM = (By.CSS_SELECTOR, 'div.product_main p.price_color')

    TOTAL_PRICE_OF_BASKET = (By.CSS_SELECTOR, 'div.alert-info div.alertinner p')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
