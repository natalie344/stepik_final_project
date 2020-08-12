from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE), "Basket empty message is not presented"

    def should_be_shoping_link(self):
        assert self.is_element_present(*BasketPageLocators.SHOPING), "Link to shoping is not presented"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOKS), "Basket is not empty"
    
    def should_be_basket_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BOOKS), "Basket is empty"