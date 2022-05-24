from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from typing import List

class SearchPage:

    url: str = 'http://tutorialsninja.com/demo/index.php?route=product/search'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_search_criteria_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-search')

    def get_button_search(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-search')

    def get_search_field(self) -> WebElement:
        return self.driver.find_element(By.NAME, 'search')

    def input_search_criteria_keywords(self, keywords: str):
        self.get_search_criteria_field().send_keys(keywords)

    def search_by_criteria(self):
        self.get_button_search().click()

    def search_by_name(self, name:str):
        self.get_search_field().send_keys(name + Keys.ENTER)

