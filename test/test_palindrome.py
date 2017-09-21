import unittest
from unittest import TestCase

from src.palindrome import convert_to_base_n, is_number_palindrome, get_list_of_palindrome


class TestCodeChallenge(TestCase):
    def test_convert_to_base_n(self):
        self.assertEquals(convert_to_base_n(2, 2), '10')
        self.assertEquals(convert_to_base_n(16, 3), '121')
        self.assertRaises(ValueError, convert_to_base_n, -13, 2)
        self.assertRaises(ValueError, convert_to_base_n, 10, 1)
        self.assertRaises(ValueError, convert_to_base_n, 127, 68)

    def test_is_number_palindrome(self):
        self.assertTrue(is_number_palindrome(121))
        self.assertFalse(is_number_palindrome(17))
        self.assertTrue(is_number_palindrome('121'))
        self.assertFalse(is_number_palindrome('17'))

    def test_get_list_of_palindrome(self):
        response = {
            "1": {"Base": 2},
            "2": {"Base": 3},
            "3": {"Base": 2},
            "4": {"Base": 3},
            "5": {"Base": 2},
            "6": {"Base": 5},
            "7": {"Base": 2},
            "8": {"Base": 3},
            "9": {"Base": 2},
            "10": {"Base": 3},
            "11": {"Base": 10},
            "12": {"Base": 5},
            "13": {"Base": 3},
            "14": {"Base": 6},
            "15": {"Base": 2},
            "16": {"Base": 3},
            "17": {"Base": 2},
            "18": {"Base": 5},
            "19": {"Base": 18},
            "20": {"Base": 3}
        }

        self.assertEquals(get_list_of_palindrome(20), response)


if __name__ == '__main__':
    unittest.main()
