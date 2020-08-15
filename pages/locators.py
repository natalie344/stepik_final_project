from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form  button[name='registration_submit']")

class ProductPageLocators():
    ADD_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    REVIEW = (By.CSS_SELECTOR, "#write_review")
    NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success")
    MESSAGE_BOOK = (By.CSS_SELECTOR, "#messages div.alert-success div.alertinner strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages div.alert-info div.alertinner strong")

class BasketPageLocators():
    BOOKS = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    SHOPING = (By.CSS_SELECTOR, "#content_inner a")
