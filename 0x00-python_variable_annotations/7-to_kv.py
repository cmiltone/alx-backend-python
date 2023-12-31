#!/usr/bin/env python3
"""
module declares a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and
should be annotated as a float.
"""
from typing import Tuple, Union

Arg = Union[int, float]


def to_kv(k: str, v: Arg) -> Tuple[str, float]:
    """returns tuple"""

    return (k, v * v)
