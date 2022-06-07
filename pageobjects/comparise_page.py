from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pageobjects.base_page import BasePage

class ComparisonPage(BasePage):

    def get_url(self) -> str:
        return f'{BasePage.host}index.php?route=product/compare'

    def get_remove_button(self) -> WebElement:
        """Кнопка удаления в таблице сравнений"""
        return self.driver.find_element(By.CLASS_NAME, 'btn-danger')

    def get_notification(self) -> WebElement:
        """Метод, возвращающий объект, который присутствует на пустой странице сравнения"""
        content: WebElement = self.driver.find_element(By.ID, 'content')
        return content.find_element(By.TAG_NAME, 'p')

    def get_comparable_products(self) -> List[str]:
        """Метод, возвращающий названия сравниваемых продуктов"""
        product_names: List[str] = []
        products_table: WebElement = self.driver.find_element(By.TAG_NAME, 'tbody')
        links: List[WebElement] = products_table.find_elements(By.TAG_NAME, 'a')
        for link in links:
            product_names.append(link.text)

        return product_names

    def is_products_presence(self, product_names: List[str]) -> bool:
        """Метод, проверяющий, все ли искомые продукты отображаются в таблице сравнения"""
        products: List[str] = self.get_comparable_products()
        return sorted(products, key=str.lower) == sorted(product_names, key=str.lower)

    def get_product_comparison_link(self) -> WebElement:
        """Метод, получающий названия (это ссылки) сравниваемых продуктов"""
        link: WebElement = WebDriverWait(self.driver, 5).until\
            (EC.presence_of_element_located((By.LINK_TEXT, 'product comparison')))
        return link

    def open_product_comparison(self):
        """Переход на страницу с таблицей сравнений"""
        self.get_product_comparison_link().click()

    def remove_comparable_product(self):
        """Метод удаления элемента из таблицы сравнения"""
        self.get_remove_button().click()

    def remove_all_comparable_products(self, count: int):
        """Метод последовательного удаления нескольких продуктов из таблицы сравнения"""
        while count > 0:
            self.remove_comparable_product()
            count -= 1

    def is_page_empty(self) -> bool:
        """Пустая ли страница сравнения"""
        return self.get_notification().text == 'You have not chosen any products to compare.'