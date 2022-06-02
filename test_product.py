import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage

class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_id: str = '42'
        self.product_name: str = 'Apple Cinema 30"'

    def tearDown(self) -> None:
        self.driver.close()

    def test_productAvailable(self):
        """Тест, что присутствует информация о продукте"""
        product_page = ProductPage(self.driver, self.product_id)
        product_page.open()

        self.assertTrue(product_page.is_product_available(self.product_name))
