# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import TestsFact, TestsSum, TestsDivision, TestsMultiplication, TestsDifference, TestsEmptyAndWrongArguments

if __name__ == '__main__':
    suite_fact = unittest.TestSuite((
        unittest.makeSuite(TestsFact),
    ))
    suite_sum = unittest.TestSuite((
        unittest.makeSuite(TestsSum),
    ))
    suite_division = unittest.TestSuite((
        unittest.makeSuite(TestsDivision),
    ))
    suite_mult = unittest.TestSuite((
        unittest.makeSuite(TestsMultiplication),
    ))
    suite_diff = unittest.TestSuite((
        unittest.makeSuite(TestsDifference),
    ))
    suite_arguments = unittest.TestSuite((
        unittest.makeSuite(TestsEmptyAndWrongArguments),
    ))
    result = unittest.TextTestRunner().run(suite_fact)
    result = unittest.TextTestRunner().run(suite_sum)
    result = unittest.TextTestRunner().run(suite_division)
    result = unittest.TextTestRunner().run(suite_mult)
    result = unittest.TextTestRunner().run(suite_diff)
    result = unittest.TextTestRunner().run(suite_arguments)
    sys.exit(not result.wasSuccessful())

