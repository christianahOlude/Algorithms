import random


def random_number_list(number):
    return [random.randint(1, 50) for numbers in range(number)]


def length_of_list(my_list):
    counter = 0
    for num in my_list:
        counter += 1
    return counter

