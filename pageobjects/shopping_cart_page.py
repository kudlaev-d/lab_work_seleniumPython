from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from pageobjects.base_page import BasePage

class ShoppingCart(BasePage):

    def __init__(self, driver: WebDriver, page_id: str):
        BasePage.__init__(self, driver)
        self.wait = WebDriverWait(self.driver, 5)

    def get_url(self) -> str:
        return f'{BasePage.host}index.php?route=checkout/cart'

