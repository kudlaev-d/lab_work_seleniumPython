from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pageobjects.base_page import BasePage
from string import ascii_letters
from random import choice

class ProductPage(BasePage):

    def get_url(self) -> str:
        return'http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42'

    def get_review_tab(self) -> WebElement:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reviews')

    def get_alert_text(self) -> str:
        alert: WebElement = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-dismissible')))
        return alert.text

    def get_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-name')

    def get_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-review')

    def get_rating_values(self) -> List[WebElement]:
        rating_values: List[WebElement] = self.driver.find_elements(By.NAME, 'rating')
        return rating_values

    def get_continue_button(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-review')

    def get_headers(self) -> List[str]:
        headers: List[WebElement] = self.driver.find_elements(By.TAG_NAME, 'h1')
        product_name: List[str] = []
        for header in headers:
            product_name.append(header.text)
        return product_name

    def product_is_available(self, name: str) -> bool:
        products: List[str] = self.get_headers()
        for product in products:
            if product == name:
                return True
        return False

    def open_review_tab(self):
        self.get_review_tab().click()

    def input_name(self, name: str):
        self.get_name_field().send_keys(name)

    def input_review(self, review: str):
        self.get_review_field().send_keys(review)

    @classmethod
    def generate_random_string(cls, length) -> str:
        """Метод генерации случайной строки заданной длины"""
        letters = ascii_letters + ' '
        rand_string: str = ''.join(choice(letters) for i in range(length))
        return rand_string

    def select_rating_value(self, value: int):
        self.get_rating_values()[value].click()

    def send_review(self):
        self.get_continue_button().click()

    def clear_review_field(self):
        self.get_review_field().clear()
