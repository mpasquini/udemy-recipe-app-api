from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """test that 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)