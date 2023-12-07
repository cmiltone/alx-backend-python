#!/usr/bin/env python3
"""
module declares a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """returns summation of a list of floats"""
    summation = 0

    for a in input_list:
        summation += a
    return summation
