import unittest
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage
from pageobjects.shopping_cart_page import ShoppingCart
from const import *

class ShoppingCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.samsung_page = ProductPage(driver=self.driver, page_id=SAMSUNG_SYNCMASTER_ID)
        self.hp_page = ProductPage(driver=self.driver, page_id=HP_LP3065_ID)
        self.shopping_cart = ShoppingCart(driver=self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_to_shopping_cart(self):
        self.samsung_page.open()
        self.samsung_page.clear_qty_field()
        self.samsung_page.input_qty(2)
        self.samsung_page.add_to_cart()

        # Продукт успешно добавился в корзину?
        self.assertTrue(self.samsung_page.is_successfully_added())

        # Открываем страницу следующего продукта и добавляем в корзину
        self.hp_page.open()
        self.samsung_page.add_to_cart()

        # Продукт успешно добавился в корзину?
        self.assertTrue(self.hp_page.is_successfully_added())

        # Открываем корзину и проверяем, что в ней есть добавленные товары
        self.shopping_cart.open()
        self.shopping_cart.get_product_qty()
