#!/usr/bin/env python3
"""
module declares a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union

Num = Union[int, float]


def sum_mixed_list(input_list: List[Num]) -> float:
    """returns summation of a list of floats"""
    summation = 0

    for a in input_list:
        summation += a
    return summation
