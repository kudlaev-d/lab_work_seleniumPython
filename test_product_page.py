import unittest
import csv
from const import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage

class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        with open('test-data/test_product_page.csv') as csv_file:
            # Инициализируем объект класса DictReader, передаем параметр quoting
            # для преобразования полей без кавычек во float
            csv_reader = csv.DictReader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            for row in csv_reader:
                self.expected_product = row

    def tearDown(self) -> None:
        self.driver.close()

    def test_productAvailable(self):
        """Тест, что присутствует информация о продукте"""
        product_page = ProductPage(driver=self.driver, page_id=APPLE_CINEMA_ID)
        product_page.open()

        self.assertDictEqual(self.expected_product, product_page.get_product_full_info())
