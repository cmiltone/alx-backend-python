#!/usr/bin/env python3
"""module annotates function
Augment the following code with
the correct duck-typed annotations:"""
from typing import Any, Sequence, Union

List = Sequence[Any]


def safe_first_element(lst: List) -> Union[Any, None]:
    """function"""
    if lst:
        return lst[0]
    else:
        return None
