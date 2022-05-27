from decimal import Decimal
from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from dataclasses import dataclass

@dataclass
class ProductInfo:
    name: str
    price: Decimal


class SearchPage(BasePage):

    def get_url(self) -> str:
        return 'http://tutorialsninja.com/demo/index.php?route=product/search'

    def get_search_criteria_field(self) -> WebElement:
        """Метод получения поля критериев поиска"""
        return self.driver.find_element(By.ID, 'input-search')

    def get_search_field(self) -> WebElement:
        """Метод получения поля поиска"""
        return self.driver.find_element(By.NAME, 'search')

    def get_button_search_criteria(self) -> WebElement:
        """Метод получения кнопки поиска по критериям"""
        return self.driver.find_element(By.ID, 'button-search')

    def get_button_global_search(self) -> WebElement:
        """Метод получения кнопки глобального поиска"""
        return self.driver.find_element(By.CLASS_NAME, 'input-group-btn')

    def input_search_criteria_keywords(self, keywords: str):
        self.get_search_criteria_field().send_keys(keywords)

    def search_by_criteria(self, criteria: str):
        self.get_button_search_criteria().send_keys(criteria)
        self.get_button_search_criteria().click()

    def search_by_name(self, name: str):
        self.get_search_field().send_keys(name)
        self.get_button_global_search().click()

    def get_price_from_str(self, price_str: str) -> Decimal:
        # $1,202.00
        # Ex Tax: $1,000.00
        split_by_line: List[str] = price_str.split('\n')


    def get_search_results(self) -> List[ProductInfo]:
        """Возвращает список найденных моделей"""
        products: List[ProductInfo] = []
        results_tags: List[WebElement] = self.driver.find_elements(By.CLASS_NAME, 'product-thumb')

        for result_tag in results_tags:
            name: str = self.driver.find_element(By.TAG_NAME, 'h4').text
            try:
                price: str = self.driver.find_element(By.CLASS_NAME, 'price-new').text
            except NoSuchElementException:
                price: str = self.driver.find_element(By.CLASS_NAME, 'price').text
            print(price)

        return products
