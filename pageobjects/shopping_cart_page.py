from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pageobjects.base_page import BasePage
from const import *

@dataclass
class CartItem:
    product_name: str
    qty: int
    unit_price: float

    def get_total(self) -> float:
        return self.qty * self.unit_price

@dataclass
class Cart:
    sub_total: float
    vat: float
    items: List[CartItem]

    def get_total(self) -> float:
        """Подсчет стоимости корзины с учетом налогов"""
        total: float = 0.0
        for item in self.items:
            total += item.get_total()
        return total

    def get_eco_tax(self) -> float:
        """Возвращает размер Eco Tax"""
        total_qty: int = 0
        for item in self.items:
            total_qty += item.qty
        return total_qty * ECO_TAX

    def get_vat(self) -> float:
        """Расчет VAT"""
        one_percent: float = self.get_total() / VAT+100
        return one_percent * VAT

    def get_subtotal(self) -> float:
        """Подсчет стоимости до вычета налогов"""
        return self.get_total() - self.get_vat()

class ShoppingCart(BasePage):

    def get_url(self) -> str:
        return f'{BasePage.host}demo/index.php?route=checkout/cart'

    def get_products_table(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'table-responsive')

    # def get_table_body(self) -> List[WebElement]:
    #     return self.get_products_table().find_elements(By.TAG_NAME, 'tbody')

    def get_product_table_rows(self) -> List[WebElement]:
        rows = self.get_products_table().find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        return rows

    def get_product_name(self) -> str:
        rows: List[WebElement] = self.get_product_table_rows()
        for row in rows:
            return row.find_element(By.TAG_NAME, 'a').text

    def get_product_qty(self) -> int:
        qty = []
        rows: List[WebElement] = self.get_product_table_rows()
        for row in rows:
            qty.append(row.find_element(By.CLASS_NAME, 'form-control').get_attribute('value'))
        pass


