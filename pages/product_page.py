from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import MainPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_write_review()
        self.should_be_add_to_basket_form()

    def should_be_write_review(self):
        # проверкa на кнопку написание рецензии
        assert self.is_element_present(*ProductPageLocators.REVIEW), "Review is not presented"

    def should_be_add_to_basket_form(self):
        # проверкa, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.ADD_FORM), "Add to basket form is not presented"
    
    def add_to_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        button = self.browser.find_element(*ProductPageLocators.ADD_FORM)
        button.click()
        self.solve_quiz_and_get_code()
        messages_book = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK).text
        messages_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert name == messages_book, "Book's title is wrong"
        assert price == messages_price, "Price is wrong"
        time.sleep(10)
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
    
