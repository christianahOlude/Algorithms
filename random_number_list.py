import random
from itertools import count


def random_number_list(number):
    return [random.randint(1, 50) for numbers in range(number)]


def length_of_list(number):
   for numbers in range(number):
       return count(numbers)
   return None