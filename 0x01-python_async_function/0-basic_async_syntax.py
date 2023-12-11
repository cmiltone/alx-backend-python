#!/usr/bin/env python3
"""
module declares an asynchronous coroutine that takes in an
integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0
and max_delay (included and float value) seconds and eventually returns it.
"""
from random import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine that accepts an integer
    """
    max_wait = random() * max_delay
    await asyncio.sleep(max_wait)

    return max_wait
