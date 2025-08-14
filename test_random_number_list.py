from unittest import TestCase
from random_number_list import random_number_list, length_of_list, sum_of_even_position, sum_of_odd_position, \
    multiply_of_third_position, calculate_average, largest_number, smallest_number


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
        print(actual)

    def test_sum_of_even_position(self):
        number = [1,2,3,4,5]
        actual = sum_of_even_position(number)
        self.assertEqual(6, actual)

    def test_sum_of_odd_position(self):
        number = [1,2,3,4,5]
        actual = sum_of_odd_position(number)
        self.assertEqual(9, actual)

    def test_multiply_of_third_position(self):
        number = [1,2,3,4,5,6,7,8,9,10]
        actual = multiply_of_third_position(number)
        self.assertEqual(162, actual)

    def test_calculate_average(self):
        number = [1,2,3,4,5,6,7,8,9,10]
        actual = calculate_average(number)
        self.assertEqual(5.5, actual)

    def test_largest_number(self):
        number = [1,2,3,4,5]
        actual = largest_number(number)
        self.assertEqual(5, actual)

    def test_smallest_number(self):
        number = [0,1,2,3,4,5]
        actual = smallest_number(number)
        self.assertEqual(0, actual)