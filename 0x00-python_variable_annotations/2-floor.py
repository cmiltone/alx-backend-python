#!/usr/bin/env python3
"""
module declares a type-annotated function floor which takes a float
 n as argument and returns the floor of the float.
"""


def floor(n: float) -> int:
    """floors a float value"""
    return int(n // 1)
