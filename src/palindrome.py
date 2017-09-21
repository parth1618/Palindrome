import json

base16_numerals = '0123456789ABCDEF'
base32_numerals = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
base64_numerals = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'


def convert_to_base_n(num, base, numerals=base64_numerals):
    """ 
    Convert any int to base 2-64 string. By default function uses 64 character
    long numerals. You can use any custom length long numerals to conver any int
    to base 2-<numerals length>
    :param num:         int Number to Convert
    :param base:        int Base to convert Number
    :param numerals:    str Custom Base Numeral
    :returns:           Converted Number to Base
 
    """
    if num < 0:
        raise ValueError('Number must be >= 0')

    if not 2 <= base <= len(numerals):
        raise ValueError('Base must be between 2-%d' % len(numerals))

    if num == 0:
        return "0"

    left_digits = num // base
    if left_digits == 0:
        return numerals[num % base]
    else:
        return convert_to_base_n(left_digits, base, numerals) + numerals[num % base]


def is_number_palindrome(number):
    """
    Function checks if given number is palindrome
    :param number:  int or str Number
    :returns:       True if palindrome else False

    """
    rev_number = list(str(number))
    rev_number.reverse()
    return rev_number == list(str(number))


def get_list_of_palindrome(to_range, numerals=base64_numerals):
    """
    Get list of all palindrome
    :param: range_to:   int to_range to get all palindrome numbers
    :param: numerals:   str numerals string for base conversion
    :returns:           dictionary of palindrome number by least base
    
    """
    result = {}
    for num in range(1, to_range + 1):
        for base in range(2, len(numerals) + 1):
            number = convert_to_base_n(num, base)
            if is_number_palindrome(number):
                result[str(num)] = {'Base': base}
                break
    return result


def print_pretty_output(result):
    return json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))


def main():
    print get_list_of_palindrome(1000)
