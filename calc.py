# -*- coding: utf-8 -*-
import math
from decimal import Decimal, DecimalException

OVER_FLOW_ERROR = "Over flow error!"
TYPE_ERROR = "Type error"
ZERO_DIVISION_ERROR = "Zero division!"
WRONG_OPERATORS = "Wrong operators!"
WRONG_OPERATOR = "Wrong operator!"
WRONG_OPERATION = "Wrong operation!"
VALUE_ERROR = "Value error!"
EMPTY_OPERATION = "Empty operation!"

def sum(a, b):
    return float(a + b)


def difference(a, b):
    try:
        return float(a - b)
    except DecimalException:
        return OVER_FLOW_ERROR


def division(a, b):
    try:
        return float(a / b)
    except ZeroDivisionError:
        return ZERO_DIVISION_ERROR
    except DecimalException:
        return OVER_FLOW_ERROR


def multipication(a, b):
    return float(a * b)


def factorial(a):
    try:
        return float(math.factorial(a))
    except ValueError:
        return VALUE_ERROR
    except TypeError:
        return WRONG_OPERATOR
    except OverflowError:
        return OVER_FLOW_ERROR


def calculation(*args):
   array_all_operations = ['!', '+', '-', '/', '*']
   a = ''; b = ''

   try:
       operation = args[0]
   except IndexError:
       return EMPTY_OPERATION


   try:
       array_all_operations.index(operation)
   except ValueError:
       return WRONG_OPERATION


   if array_all_operations.index(operation):
       try:
           a = Decimal(str(args[1]))
           b = Decimal(str(args[2]))
       except ValueError:
           return WRONG_OPERATORS
       except DecimalException:
           return WRONG_OPERATORS
       except IndexError:
           return EMPTY_OPERATION
   else:
       try:
           a = args[1]
       except ValueError:
           return WRONG_OPERATOR
       except DecimalException:
           return WRONG_OPERATOR
       except IndexError:
           return EMPTY_OPERATION

   if operation == '-':
       return  difference(a, b)
   elif operation == '+':
       return sum(a, b)
   elif operation == '/':
       return division(a, b)
   elif operation == '*':
       return  multipication(a, b)
   elif operation == '!':
       return factorial(a)

