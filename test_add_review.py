import unittest
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.search_page import SearchPage, ProductInfo

class AddReviewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.search_page = SearchPage(self.driver)
        self.search_page.open()

    def tearDown(self) -> None:
        self.driver.quit()