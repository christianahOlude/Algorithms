def is_palindrome(number):
    converted_number = str(number)
    reverse = converted_number[::-1]
    if reverse == converted_number:
        return True
    else:
        return False

def is_prime(number, num):
    if number / num == 1:
        return True
    else:
        return False


