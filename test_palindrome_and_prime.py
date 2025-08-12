from unittest import TestCase

from palindrome_and_prime import is_palindrome, is_prime


class Test(TestCase):
    def test_is_palindrome(self):
        number = 131
        expected = True
        actual = is_palindrome(number)
        self.assertEqual(expected, actual)

    def test_is_not_palindrome(self):
        number = 123
        expected = False
        actual = is_palindrome(number)
        self.assertEqual(expected, actual)

    def test_is_prime(self):
        number = 13
        num = 13
        expected = True
        actual = is_prime(number, num)
        self.assertEqual(expected, actual)

    def test_is_not_prime(self):
        number = 12
        num = 10
        expected = False
        actual = is_prime(number, num)
        self.assertEqual(expected, actual)
