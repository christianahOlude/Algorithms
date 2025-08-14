import random

def random_number_list(number):
    return [random.randint(1, 50) for numbers in range(number)]

def length_of_list(my_list):
    counter = 0
    for num in my_list:
        counter += 1
    return counter

def sum_of_even_position(my_list):
    even_position = my_list[1::2]

    summ = 0
    for num in even_position:
         summ += num
    return summ


def sum_of_odd_position(my_list):
    odd_position = my_list[::2]

    summ = 0
    for num in odd_position:
        summ += num
    return summ

def multiply_of_third_position(my_list):
    third_position = my_list[::3]

    multiple = 1
    for num in third_position:
        multiple *= num
    return multiple

def calculate_average(my_list):
    summ = 0
    counter = 0
    for num in my_list:
        counter += 1
        summ += num
    return summ / counter

def largest_number(my_list):
    return max(my_list)

def smallest_number(my_list):
    return min(my_list)