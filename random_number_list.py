import random


def random_number_list(number):
    return [random.randint(1, 50) for numbers in range(number)]


def length_of_list(my_list):
    counter = 0
    for num in my_list:
        counter += 1
    return counter

def sum_of_even_position(my_list):
    return sum(my_list[1::2])

def sum_of_odd_position(my_list):
    return sum(my_list[::2])

def multiply_of_third_position(my_list):
    return my_list[2] * my_list[5] * my_list[8]

def calculate_average(my_list):
    return sum(my_list) / len(my_list)

def largest_number(my_list):
    return max(my_list)

def smallest_number(my_list):
    return min(my_list)