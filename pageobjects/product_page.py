from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from typing import List, Dict, TypedDict
from pageobjects.base_page import BasePage

class Product_info(TypedDict):
    brand: str
    product_code: str
    price: float
    name: str
    description: str

class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, product_id: str):
        BasePage.__init__(self, driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'{BasePage.host}index.php?route=product/product&product_id={self.product_id}'

    def get_review_tab(self) -> WebElement:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reviews')

    def get_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-name')

    def get_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-review')

    def get_rating_values(self) -> List[WebElement]:
        rating_values: List[WebElement] = self.driver.find_elements(By.NAME, 'rating')
        return rating_values

    def get_continue_button(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-review')

    def get_compare_button(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')

    def get_product_main_div(self) -> WebElement:
        """Возвращает контейнер, в котором располагается вся информация о продукте"""
        return self.driver.find_element(By.ID, 'product-product')

    def get_product_info_lists(self) -> List[WebElement]:
        """Возвращает списки, в которых содержится информация о продукте"""
        main_div: WebElement = self.get_product_main_div()
        return main_div.find_elements(By.CLASS_NAME, 'list-unstyled')

    def get_product_name(self) -> str:
        """Возвращает название товара на его странице"""
        a: WebElement = self.get_product_main_div()
        return a.find_element(By.TAG_NAME, 'h1').text

    def get_description_part(self) -> str:
        """Вернет первое предложение из описания продукта"""
        description: List[str] = self.driver.find_element(By.ID, 'tab-description').text.split('.')
        return description[0]

    def get_product_info_wo_price(self) -> Product_info:
        ul_lists: List[WebElement] = self.get_product_info_lists()  # Берем все неупорядоченные списки на странице
        li_info_product: List[WebElement] = ul_lists[0].find_elements(By.TAG_NAME, 'li')  # У первого ul берем все его li

        # Полученные значения разделяем по ':' и добавляем в промежуточный dict
        info: Dict = {}
        for li in li_info_product:
            item: List[str] = li.text.split(': ')
            info[item[0]] = f'{item[1]}'

        # Создаем типизированный словарь
        product_info: Product_info = Product_info(
            brand=info['Brand'],
            product_code=info['Product Code'],
            price=0.0,
            name='',
            description=''
        )

        return product_info

    def get_product_price(self) -> float:
        """Возвращает стоимость продукта"""
        ul_lists: List[WebElement] = self.get_product_info_lists()
        li_price_product = ul_lists[1].find_element(By.TAG_NAME, 'h2')
        return float(li_price_product.text[1:])  # Берем цену, реализованную как заголовок h2, и отбрасываем '$'

    def get_product_full_info(self) -> Product_info:
        """Возвращает полную информацию о продукте"""
        product_info: Product_info = self.get_product_info_wo_price()

        product_info['price'] = self.get_product_price()
        product_info['name'] = self.get_product_name()
        product_info['description'] = self.get_description_part()

        return product_info

    def get_product_qty_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-quantity')

    def is_product_available(self, name: str) -> bool:
        product_name: List[str] = []
        headers: List[WebElement] = self.driver.find_elements(By.TAG_NAME, 'h1')
        for header in headers:
            product_name.append(header.text)
        for product in product_name:
            if product == name:
                return True
        return False

    def is_presence_alert_text(self, text: str) -> bool:
        alert: bool = self.wait. \
            until(ec.text_to_be_present_in_element((By.CLASS_NAME, 'alert-dismissible'), text))
        return alert

    def is_successfully_added(self) -> bool:
        """Если не найден алерт об успешном добавлении (к сравнению/в корзину), то отвалится по тайм-ауту. Иначе True"""
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'alert-dismissible')))
        alert: bool = self.wait.until(ec.text_to_be_present_in_element(
            (By.CLASS_NAME, 'alert-dismissible'), 'Success: You have added'))
        return alert

    def open_review_tab(self):
        self.get_review_tab().click()

    def input_name(self, name: str):
        self.get_name_field().send_keys(name)

    def input_review(self, review: str):
        self.get_review_field().send_keys(review)

    def select_rating_value(self, value: int):
        self.get_rating_values()[value].click()

    def send_review(self):
        self.get_continue_button().click()

    def clear_review_field(self):
        self.get_review_field().clear()

    def add_to_compare(self):
        self.get_compare_button().click()

    def input_qty(self, qty: int):
        self.get_product_qty_field().send_keys(qty)

    def clear_qty_field(self):
        self.get_product_qty_field().clear()

    def add_to_cart(self):
        self.driver.find_element(By.ID, 'button-cart').click()

