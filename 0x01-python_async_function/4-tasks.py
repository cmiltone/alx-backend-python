#!/usr/bin/env python3
"""
module declares a function similar task_wait_n to but calls
task_wait_random
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls task_wait_random n times.
    """
    max_waits = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(max_waits)
