from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List


class ProductPage:

    url: str = 'http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

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


