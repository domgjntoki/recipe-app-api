"""
Samples tests
"""
from django.test import TestCase

from app import calc


class CalcTests(TestCase):
    """Test for calc app"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(calc.subtract(10, 5), 5)
