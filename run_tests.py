# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import TestsFact, TestsSum, TestsDivision, TestsMultiplication, TestsDifference, TestsEmptyAndWrongArguments

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestsFact),
        unittest.makeSuite(TestsSum),
        unittest.makeSuite(TestsDivision),
        unittest.makeSuite(TestsMultiplication),
        unittest.makeSuite(TestsDifference),
        unittest.makeSuite(TestsEmptyAndWrongArguments),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

