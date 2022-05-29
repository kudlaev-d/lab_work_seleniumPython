import unittest
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.comparise_page import ComparisonPage
from pageobjects.product_page import ProductPage

class CompareTest(unittest.TestCase):

    def setUp(self) -> None:
        self.apple_cinema_id: str = '42'
        self.samsung_syncmaster_id: str = '33'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.apple_product_page = ProductPage(driver=self.driver, page_id=self.apple_cinema_id)
        self.samsung_product_page = ProductPage(driver=self.driver, page_id=self.samsung_syncmaster_id)
        self.comparison_page = ComparisonPage(self.driver)
        # Продукты, которые будут сравниваться
        self.comparable_products: List[str] = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']

    def tearDown(self) -> None:
        self.driver.quit()

    def test_compare(self):
        """Тестирование сравнения продуктов"""

        # Открываем страницу продукта Apple Cinema и добавляем его к сравнению
        self.apple_product_page.open()
        self.apple_product_page.add_to_compare()

        # Продукт успешно добавился?
        self.assertTrue(self.apple_product_page.is_successfully_added_to_comparison())

        # Открываем страницу продукта Samsung и добавить его к сравнению
        self.samsung_product_page.open()
        self.samsung_product_page.add_to_compare()

        # Переходим на страницу с таблицей сравнения
        self.comparison_page.open_product_comparison()

        # На странице присутствуют добавленные раннее продукты
        self.assertTrue(self.comparison_page.is_products_presence(self.comparable_products))

        # Удалить все товары из сравнения
        self.comparison_page.remove_all_comparable_products(len(self.comparable_products))

        # Страница сравнения пуста?
        self.assertTrue(self.comparison_page.is_page_empty())
