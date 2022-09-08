from dataclasses import dataclass

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Dict
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
    items: List[CartItem]
    vat: float = VAT

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
        one_percent: float = (self.get_total() - self.get_eco_tax()) / (VAT+1)
        return one_percent * VAT

    def get_subtotal(self) -> float:
        """Подсчет стоимости до вычета налогов"""
        return (self.get_total() - self.get_eco_tax()) - self.get_vat()

class ShoppingCart(BasePage):

    def get_url(self) -> str:
        return f'{BasePage.host}index.php?route=checkout/cart'

    def get_products_table(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'table-responsive')

    def get_product_table_rows(self) -> List[WebElement]:
        rows = self.get_products_table().find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        return rows

    def get_cart_items(self) -> List[CartItem]:
        cart_items: List[CartItem] = []
        rows = self.get_product_table_rows()
        for row in rows:
            name = row.find_element(By.TAG_NAME, 'a').accessible_name
            qty = int(row.find_element(By.CLASS_NAME, 'form-control').get_attribute('value'))
            unit_price = float(row.find_element(By.CLASS_NAME, 'text-right').text[1:])

            cart_item: CartItem = CartItem(
                product_name=name,
                qty=qty,
                unit_price=unit_price
            )
            cart_items.append(cart_item)
        return cart_items

    def get_cart_prices_table(self) -> WebElement:
        table: WebElement = self.driver.find_element(By.CLASS_NAME, 'col-sm-offset-8')
        return table

    def get_cart_table_price(self, name: str) -> Dict:
        """Возвращает значение из таблицы цен и налогов по необходимому имени"""
        cart_table_prices: Dict = {}
        table_rows = self.get_cart_prices_table().find_elements(By.TAG_NAME, 'tr')

        for row in table_rows:
            td = row.find_elements(By.CLASS_NAME, 'text-right')
            cart_table_prices[td[0].text[:-1]] = float(td[1].text[1:])

        return cart_table_prices[name]

    def get_remove_button(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Remove"]')
        # return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-original-title="Remove"]')))

    def get_notification(self) -> WebElement:
        """Метод, возвращающий объект, который присутствует на пустой странице корзины"""
        content: WebElement = self.driver.find_element(By.ID, 'content')
        return content.find_element(By.TAG_NAME, 'p')

    def is_page_empty(self) -> bool:
        """Пустая ли корзина"""
        return self.get_notification().text == 'Your shopping cart is empty!'

    def remove_product_from_cart(self):
        remove_button = self.get_remove_button()
        remove_button.click()
        self.wait.until(EC.staleness_of(remove_button))

    def remove_all_products_from_cart(self):
        """Метод последовательного удаления всех продуктов из таблицы сравнения
        Идея в том, что мы кликаем на кнопку Remove, если она есть на странице"""
        flag: bool = True
        while flag:
            self.remove_product_from_cart()
            try:
                self.get_remove_button()
            except NoSuchElementException:
                flag = False


