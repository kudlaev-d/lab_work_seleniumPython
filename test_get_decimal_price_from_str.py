import unittest
from decimal import Decimal
from pageobjects.search_page import get_decimal_price_from_str


class ExtractDecimalPriceTest(unittest.TestCase):

    def test(self):
        examples = [
            ['$110.00', Decimal(110.0)],
            ['$1,202.00\nEx Tax: $1,000.00', Decimal(1202.0)],
            ['$122.00\nEx Tax: $100.00', Decimal(122.0)]
        ]

        for example in examples:
            self.assertEqual(example[1], get_decimal_price_from_str(example[0]))
