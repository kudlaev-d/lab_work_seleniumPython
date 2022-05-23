import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.product_page import ProductPage

class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product = 'Apple Cinema 30"'

    def tearDown(self) -> None:
        self.driver.close()

    def test_productAvailable(self):
        '''Проверка, что присутствует информация о продукте'''

        product_page = ProductPage(self.driver)
        product_page.open()

        self.assertTrue(product_page.product_is_available(self.product))

