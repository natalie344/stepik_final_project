from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message(self):
        # сообщение что корзина пуста
        assert self.is_element_present(*BasketPageLocators.MESSAGE), \
            "Basket empty message is not presented"

    def should_be_shoping_link(self):
        # ссылка на продолжение покупок
        assert self.is_element_present(*BasketPageLocators.SHOPING), \
            "Link to shoping is not presented"

    def should_be_basket_empty(self):
        # проверка того, что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.BOOKS), \
            "Basket is not empty"

    def should_be_basket_not_empty(self):
        # проверка того, что корзина не пуста
        assert self.is_element_present(*BasketPageLocators.BOOKS), \
            "Basket is empty"
