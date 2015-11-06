# -*- coding: utf-8 -*-
import math

OVER_FLOW_ERROR = "Over flow error!"
TYPE_ERROR = "Type error"
ZERO_DIVISION_ERROR = "Zero division!"
WRONG_OPERATORS = "Wrong operators!"
WRONG_OPERATOR = "Wrong operator!"
WRONG_OPERATION = "Wrong operation!"
EMPTY_OPERATION_SCINCE = "Empty operation scine!"
VALUE_ERROR = "Value error!"

def sum(a, b):
    try:
        result = a + b
    except TypeError:
        result = TYPE_ERROR
    return result


def difference(a, b):
    try:
        result = a - b
    except TypeError:
        result = TYPE_ERROR
    except OverflowError:
        result = OVER_FLOW_ERROR
    return result


def division(a, b):
    try:
        result = a / b
    except TypeError:
        result = TYPE_ERROR
    except ZeroDivisionError:
        result = ZERO_DIVISION_ERROR
    except OverflowError:
        result = OVER_FLOW_ERROR
    return result


def multipication(a, b):
    try:
        float(a)
        float(b)
        result = a * b
    except TypeError:
        result = TYPE_ERROR
    except OverflowError:
        result = OVER_FLOW_ERROR
    except ValueError:
        result = TYPE_ERROR
    return result


def factorial(a):
    try:
        result = math.factorial(a)
    except TypeError:
        result = TYPE_ERROR
    except OverflowError:
        result = OVER_FLOW_ERROR
    except ValueError:
        result = VALUE_ERROR
    return result


def wich_operation(args):
    try:
        operation = args[0]
    except Exception:
        operation = EMPTY_OPERATION_SCINCE
    return operation


def can_you_take_two_operand(args):
    try:
        first_operand = args[1]
        second_operand = args[2]
        flag = True
    except Exception:
        flag = False
    return flag


def can_you_take_one_operand(args):
    try:
        operand = args[1]
        flag = True
    except Exception:
        operand = False
        flag = False
    return flag


def calculation(*args):
    operation = wich_operation(args)
    i_have_two_operand = can_you_take_two_operand(args)
    i_have_one_operand = can_you_take_one_operand(args)
    a = 'empty'
    b = 'empty'
    if i_have_two_operand:
        a = args[1]
        b = args[2]
    if i_have_one_operand:
        a = args[1]

    if operation == EMPTY_OPERATION_SCINCE:
        return operation
    elif (operation == '+') and i_have_two_operand:
        return sum(a, b)
    elif (operation == "-") and i_have_two_operand:
        return difference(a, b)
    elif (operation == "/") and i_have_two_operand:
        return division(a, b)
    elif (operation == "*") and i_have_two_operand:
        return multipication(a, b)
    elif (operation == "!") and i_have_one_operand:
        return factorial(a)
    elif (operation == '!') and (not i_have_one_operand):
        return WRONG_OPERATOR
    elif not i_have_two_operand:
        return WRONG_OPERATORS
    else:
        return WRONG_OPERATION

