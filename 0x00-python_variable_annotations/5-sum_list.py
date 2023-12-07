#!/usr/bin/env python3
"""
module declares a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(arr: list[float]) -> float:
    """returns string representation of a float value"""
    summation = 0

    for a in arr:
        summation += a
    return summation
