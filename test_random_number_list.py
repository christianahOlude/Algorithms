from unittest import TestCase

from samba.dcerpc.security import ace_object

from random_number_list import random_number_list, length_of_list


class Test(TestCase):
    def test_random_number_list(self):
        number = 10
        actual = random_number_list(number)
        self.assertEqual(number, len(actual))
        print(actual)

    def test_length_of_list(self):
        number = [1,2,3,4,5]
        actual = length_of_list(number)
        self.assertEqual(5, actual)