import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    """Базовый класс"""

    host: str = os.environ['HOST']

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_url(self) -> str:
        """Абстрактный метод, возвращающий адрес страницы"""
        raise NotImplementedError

    def open(self):
        self.driver.get(self.get_url())
