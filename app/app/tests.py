"""
sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    "Test the cals module."

    def test_add_number(self):
        """test adding two number"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_number(self):
        """test substracting two number"""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
