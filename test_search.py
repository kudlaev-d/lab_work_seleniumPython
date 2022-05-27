import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage
from pageobjects.search_page import SearchPage

class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.product_name: str = 'Sony'

    def tearDown(self) -> None:
        self.driver.close()

    def test_search(self):
        """Проверка работы функции поиска"""

        self.search_page.search_by_name(self.product_name)
        self.search_page.get_search_results()

