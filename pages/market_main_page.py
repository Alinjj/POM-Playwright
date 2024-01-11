from pages.base import Base
from Locators.basket_page import Basket
from Locators.market_page import Market
from data.assertion import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0)
        self.click(Market.GO_TO_SHOPPING_CART)

    def checkout(self):
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Ivan")
        self.input(Basket.LAST_NAME, "Ivanov")
        self.input(Basket.ZIP, "123456")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertions.have_text(Basket.DESC, "Thank you for your order!", "no")