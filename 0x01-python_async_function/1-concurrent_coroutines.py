#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. It spawns wait_random n times
with the specified max_delay
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random n times
    """
    max_waits = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(max_waits)
