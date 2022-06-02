import unittest
from const import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage

class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.expected_product: dict = {
                        'name': 'Apple Cinema 30"',
                        'Brand': ' Apple',
                        'Product Code': ' Product 15',
                        'price': 110.0,
                        'description': 'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 '
                                       'pixel resolution'
                        }

    def tearDown(self) -> None:
        self.driver.close()

    def test_productAvailable(self):
        """Тест, что присутствует информация о продукте"""
        product_page = ProductPage(driver=self.driver, page_id=APPLE_CINEMA_ID)
        product_page.open()

        self.assertEqual(self.expected_product, product_page.get_product_full_info())
