import unittest
from typing import Final, List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.product_page import ProductPage
from random import randrange


class AddReviewTest(unittest.TestCase):

    MAX_RATING: Final = 5

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_page = ProductPage(self.driver)
        self.product_page.open()
        self.expected_rating_alert: str = 'Warning: Please select a review rating!'
        self.expected_unsuccessful_review_alert: str = 'Warning: Review Text must be between 25 and 1000 characters!'
        self.expected_successful_review_alert: str = 'Thank you for your review. ' \
                                                     'It has been submitted to the webmaster for approval.'
        self.name: str = 'John'
        self.wrong_review_length: int = 24

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_review(self):
        """Тест добавления отзыва о товаре"""

        # Открыть вкладку review, не заполняя поля кликнуть Continue
        self.product_page.open_review_tab()
        self.product_page.send_review()

        self.assertTrue(self.product_page.is_presence_alert_text(self.expected_rating_alert))

        # Выбрать любой рейтинг, ввести имя и комментарий в 24 символа
        self.product_page.select_rating_value(randrange(AddReviewTest.MAX_RATING))
        self.product_page.input_name(self.name)
        self.product_page.input_review(self.product_page.generate_random_string(self.wrong_review_length))
        self.product_page.send_review()

        self.assertTrue(self.product_page.is_presence_alert_text(self.expected_unsuccessful_review_alert))

        # Ввести в поле комментария больше 25 символов (25-1000)
        self.product_page.clear_review_field()
        self.product_page.input_review(self.product_page.generate_random_string(randrange(25, 1001)))
        self.product_page.send_review()

        self.assertTrue(self.product_page.is_presence_alert_text(self.expected_successful_review_alert))
