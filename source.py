# -*- coding: utf-8 -*-
import unittest


class RomanConverter():

    def num_to_roman(self, num):
        if not isinstance(num, type(1)):
            raise TypeError("Tipo esperado eh inteiro, recebido foi %s" % type(num))
        if not 0 < num < 4000:
            raise ValueError("numero precisa estar entre 1 e 3999")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []

        for i in range(len(ints)):
            count = int(num / ints[i])
            result.append(nums[i] * count)
            num -= ints[i] * count

        return ''.join(result)

    def roman_to_num(self, roman):
        if not isinstance(roman, type("")):
            raise TypeError("Tipo esperado eh string, recebido foi %s" % type(roman))
        roman = roman.upper()
        nums = {'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1}
        sum = 0
        for i in range(len(roman)):
            try:
                value = nums[roman[i]]
                if i+1 < len(roman) and nums[roman[i+1]] > value:
                    sum -= value
                else:
                    sum += value
            except KeyError:
                raise ValueError('%s nao eh um numeral romano valido.' % roman)
        return sum


class TestRomanConverter(unittest.TestCase):

    def setUp(self):
        self.roman = RomanConverter()

    def test_num_to_roman(self):
        self.assertEqual(self.roman.num_to_roman(4), 'IV')
        self.assertEqual(self.roman.num_to_roman(10), 'X')
        self.assertEqual(self.roman.num_to_roman(19), 'XIX')
        self.assertEqual(self.roman.num_to_roman(53), 'LIII')
        with self.assertRaises(ValueError):
            self.assertEqual(self.roman.num_to_roman(5000), 'X')
        with self.assertRaises(TypeError):
            self.assertEqual(self.roman.num_to_roman('X'), 'X')

    def test_roman_to_num(self):
        self.assertEqual(self.roman.roman_to_num('IV'), 4)
        self.assertEqual(self.roman.roman_to_num('X'), 10)
        self.assertEqual(self.roman.roman_to_num('XIX'), 19)
        self.assertEqual(self.roman.roman_to_num('LIII'), 53)
        with self.assertRaises(ValueError):
            self.assertEqual(self.roman.roman_to_num('HIII'), 10)
        with self.assertRaises(TypeError):
            self.assertEqual(self.roman.roman_to_num(10), 10)


def suite():
        tests = ['test_num_to_roman', 'test_roman_to_num']
        return unittest.TestSuite(map(TestRomanConverter, tests))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
