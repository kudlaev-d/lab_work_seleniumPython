import unittest
from const import *
from pageobjects.product_page import ProductPage
from webdriver_factory import WebDriverFactory
from read_from_csv_file import read_from_csv_file

class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.expected_product = read_from_csv_file('test-data/test_product_page.csv')

    def tearDown(self) -> None:
        self.driver.close()

    def test_productAvailable(self):
        """Тест, что присутствует информация о продукте"""
        product_page = ProductPage(driver=self.driver, product_id=APPLE_CINEMA_ID)
        product_page.open()

        self.assertEqual(self.expected_product, product_page.get_product_full_info())