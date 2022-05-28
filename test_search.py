import unittest
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.search_page import SearchPage, ProductInfo

class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.first_product_name: str = 'Apple'
        self.second_product_name: str = 'Sony'
        self.third_product_name: str = 'nokia'
        self.criteria_search_text: str = 'stunning'
        self.notification: str = 'There is no product that matches the search criteria.'

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        """Проверка работы функции поиска"""
        # Поиск первого продукта
        self.search_page.search_by_name(self.first_product_name)
        product: List[ProductInfo] = self.search_page.get_search_results()

        self.assertEqual(product[0].name, 'Apple Cinema 30"')
        self.assertEqual(product[0].price, 110.00)

        # Поиск второго продукта
        self.search_page.clean_search_field()
        self.search_page.search_by_name(self.second_product_name)
        product: List[ProductInfo] = self.search_page.get_search_results()

        self.assertEqual(product[0].name, 'Sony VAIO')
        self.assertEqual(product[0].price, 1202.00)

        # Поиск третьего продукта, которого нет на сайте
        self.search_page.clean_search_field()
        self.search_page.search_by_name(self.third_product_name)

        self.assertEqual(self.notification, self.search_page.get_notification())

        # Поиск по доп. критериям
        self.search_page.clean_search_criteria_field()
        self.search_page.search_in_description_checkbox()
        self.search_page.search_by_criteria(self.criteria_search_text)

        product: List[ProductInfo] = self.search_page.get_search_results()

        self.assertEqual(product[0].name, 'HP LP3065')
        self.assertEqual(product[1].name, 'iMac')
