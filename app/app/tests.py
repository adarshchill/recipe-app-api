"""
Sample tests
"""

from http import client  # noqa
from django.test import SimpleTestCase
from rest_framework.test import APIClient   # noqa
from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc Module"""

    def test_add_numbers(self):
        """Test adding two numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Subtracting Numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

    def test_hi_interviewer(self):
        """Just a HI to interviewer"""
        res = calc.give_me_hi()
        self.assertEqual(res, "Hi Mr/Ms InterViewer")

    def test_ping_google(self):
        """pinging ggogle.com"""
        client = APIClient()  # noqa
        res = client.get("https://www.cricbuzz.com/")
        print(res)
