# -*- coding: utf-8 -*-
import unittest
import calc
from math import isnan


class TestsFact(unittest.TestCase):
    _operation = '!'

    def test_simple(self):
        result = calc.calculation(self._operation, 3)
        self.assertEquals(result, 6)

    def test_very_big(self):
        result = calc.calculation(self._operation, 1e308)
        self.assertEquals(result, calc.OVER_FLOW_ERROR)

    def test_empty(self):
        result = calc.calculation(self._operation, )
        self.assertEquals(result, calc.EMPTY_OPERATION)

    def test_negative(self):
        result = calc.calculation(self._operation, -3)
        self.assertEquals(result, calc.VALUE_ERROR)

    def test_float(self):
        result = calc.calculation(self._operation, 4.3)
        self.assertEquals(result, calc.VALUE_ERROR)

    def test_negative_float(self):
        result = calc.calculation(self._operation, -10.3)
        self.assertEquals(result, calc.VALUE_ERROR)

    def test_pow_dec(self):
        result = calc.calculation(self._operation, 1e2)
        self.assertEquals(result, calc.calculation(self._operation, 100))



class TestsSum(unittest.TestCase):
    _operation = '+'

    def test_simple(self):
        result = calc.calculation(self._operation, 4, 2)
        self.assertEquals(result, 6)

    def test_float_and_negative(self):
        result = calc.calculation(self._operation, 43.2, -2)
        self.assertEquals(result, 41.2)

    def test_float(self):
        result = calc.calculation(self._operation, 0.9999999999, 0.0000000001)
        self.assertEquals(result, 1)

    def test_float_second(self):
        result = calc.calculation(self._operation, 0.2, 0.1)
        self.assertEquals(result, 0.3)


    def test_infinity(self):
        result = calc.calculation(self._operation, 1e309, 1e309)
        self.assertEquals(result, float("inf"))

    def test_zero(self):
        result = calc.calculation(self._operation, 0, 1.0)
        self.assertEquals(result, 1.0)



class TestsDivision(unittest.TestCase):
    _operation = '/'

    def test_div(self):
        result = calc.calculation('/', 5, 2)
        self.assertEquals(result, 2.5)

    def test_simple(self):
        result = calc.calculation(self._operation, 4, 2)
        self.assertEquals(result, 2)

    def test_float(self):
        result = calc.calculation(self._operation, 4.2, 2.1)
        self.assertEquals(result, 2.0)

    def test_zero(self):
        result = calc.calculation(self._operation, 32, 0)
        self.assertEquals(result, calc.ZERO_DIVISION_ERROR)

    def test_nan_on_nan(self):
        result = calc.calculation(self._operation, 1e309, 1e309)
        self.assertEquals(result, calc.OVER_FLOW_ERROR)

    def test_nan(self):
        result = calc.calculation(self._operation, 1, 9e1000000000000000000000000000000000000)
        self.assertEquals(result, 0.0)


class TestsMultiplication(unittest.TestCase):
    _operation = '*'

    def test_simple(self):
        result = calc.calculation(self._operation, 4, 2)
        self.assertEquals(result, 8)

    def test_float(self):
        result = calc.calculation(self._operation, 4.2, 2.0)
        self.assertEquals(result, 8.4)

    def test_float_two_minus(self):
        result = calc.calculation(self._operation, -4.2, -2.0)
        self.assertEquals(result, 8.4)

    def test_float_minus(self):
        result = calc.calculation(self._operation, 4.2, -2.0)
        self.assertEquals(result, -8.4)

    def test_infinity(self):
        result = calc.calculation(self._operation, 1e309, 1e309)
        self.assertEquals(result, float("inf"))


class TestsDifference(unittest.TestCase):
    _operation = '-'

    def test_simple(self):
        result = calc.calculation(self._operation, 4, 2)
        self.assertEquals(result, 2)

    def test_dif(self):
        result = calc.calculation('-', 0.3, 0.1)
        self.assertEquals(result, 0.2)

    def test_float(self):
        result = calc.calculation(self._operation, 4.2, 2.0)
        self.assertEquals(result, 2.2)

    def test_float_minus(self):
        result = calc.calculation(self._operation, 4.2, -2.0)
        self.assertEquals(result, 6.2)

    def test_infinity(self):
        result = calc.calculation(self._operation, 1e309, 1e309)
        self.assertEquals(result, calc.OVER_FLOW_ERROR)


class TestsEmptyAndWrongArguments(unittest.TestCase):
    operation = '+'
    _factorial = '!'
    _rand_one = 32
    _rand_two = 2
    _wrong_operation = 'wrong'
    _wrong_one = 'wrong'

    def test_without_one_operand(self):
        result = calc.calculation(self.operation, self._rand_one)
        self.assertEquals(result, calc.EMPTY_OPERATION)

    def test_without_two_operands(self):
        result = calc.calculation(self.operation)
        self.assertEquals(result, calc.EMPTY_OPERATION)

    def test_wrong_operator(self):
        result = calc.calculation(self.operation, self._rand_one, self._wrong_one)
        self.assertEquals(result, calc.WRONG_OPERATORS)

    def test_wrong_factorial(self):
        result = calc.calculation(self._factorial, self._wrong_one)
        self.assertEquals(result, calc.WRONG_OPERATOR)

    def test_wrong_operation(self):
        result = calc.calculation(self._wrong_operation, self._rand_one, self._rand_two)
        self.assertEquals(result, calc.WRONG_OPERATION)

    def test_empty_operation(self):
        result = calc.calculation()
        self.assertEquals(result, calc.EMPTY_OPERATION)

