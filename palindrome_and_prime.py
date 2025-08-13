def is_palindrome(number):
    converted_number = str(number)
    reverse = converted_number[::-1]
    if reverse == converted_number:
        return True
    else:
        return False


def is_prime(number: int):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
            return True
    else:
        return None