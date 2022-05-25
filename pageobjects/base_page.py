from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """Базовый класс"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self) -> str:
        """Абстрактный метод, возвращающий адрес страницы"""
        raise NotImplementedError

    def open(self):
        self.driver.get(self.get_url())
