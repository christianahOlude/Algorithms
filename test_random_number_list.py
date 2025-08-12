from unittest import TestCase

from random_number_list import random_number_list


class Test(TestCase):
    def test_random_number_list(self):
        number = 10
        actual = random_number_list(number)
        self.assertEqual(number, len(actual))
        print(actual)
