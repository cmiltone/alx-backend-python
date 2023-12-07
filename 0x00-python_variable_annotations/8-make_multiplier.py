#!/usr/bin/env python3
"""
module declares a type-annotated function make_multiplier that
takes a float multiplier as argument and returns a
function that multiplies a float by multiplier.
"""
from typing import Callable, Union

Arg = Union[int, float]


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a callable"""

    def callable(num: float) -> float:
        return num * multiplier

    return callable
