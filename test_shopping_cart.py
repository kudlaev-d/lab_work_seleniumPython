import unittest
from typing import List
from pageobjects.product_page import ProductPage
from pageobjects.shopping_cart_page import ShoppingCart, CartItem, Cart
from const import *
from webdriver_factory import WebDriverFactory

class ShoppingCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
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
        cart_items: List[CartItem] = self.shopping_cart.get_cart_items()
        cart: Cart = Cart(items=cart_items)

        # Сравниваем имена товаров и общую стоимость с ожидаемой
        self.assertEqual(cart_items[0].product_name, 'Samsung SyncMaster 941BW')
        self.assertEqual(cart_items[1].product_name, 'HP LP3065')
        self.assertEqual(self.shopping_cart.get_cart_table_price('Total'), 606)
        # Рассчитываем итоговую стоимость сами и сравниваем с той, что на сайте
        self.assertEqual(self.shopping_cart.get_cart_table_price('Total'), cart.get_total())

        self.shopping_cart.remove_all_products_from_cart(len(cart_items))

        self.assertTrue(self.shopping_cart.is_page_empty())



