from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pageobjects.base_page import BasePage


# @dataclass
# class ProductInfo:
#     name: str
#     brand: str
#     product_code: str
#     price: Decimal
#     description: str

class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, page_id: str):
        BasePage.__init__(self, driver)
        self.page_id = page_id
        self.wait = WebDriverWait(self.driver, 5)

    def get_url(self) -> str:
        return f'{BasePage.host}demo/index.php?route=product/product&product_id={self.page_id}'

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

    # def get_headers(self) -> List[str]:
    #     headers: List[WebElement] = self.driver.find_elements(By.TAG_NAME, 'h1')
    #     product_name: List[str] = []
    #     for header in headers:
    #         product_name.append(header.text)
    #     return product_name
    #
    # def product_is_available(self, name: str) -> bool:
    #     products: List[str] = self.get_headers()
    #     for product in products:
    #         if product == name:
    #             return True
    #     return False

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
        alert: bool = WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'alert-dismissible'), text))
        return alert

    def is_successfully_added_to_comparison(self) -> bool:
        """Если не найден алерт об успешном добавлении к сравнению, то отвалится по тайм-ауту. Иначе True"""
        alert: bool = self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'alert-dismissible'), 'Success: You have added'))
        return True

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