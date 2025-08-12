def is_palindrome(number):
    num = str(number)
    reverse = num[::-1]
    if reverse == num:
        return True
    else:
        return False


def is_prime(number, num):
    if number / num == 1:
        return True
    else:
        return False


