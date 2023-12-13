#!/usr/bin/env python3
"""
module declares a coroutine that will loop 10 times, each time asynchronously
wait 1 second, then yield
a random number between 0 and 10. Use the random module
"""
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """an async coroutine"""
    n = 0
    while n < 10:
        await asyncio.sleep(1)
        n += 1
        yield random() * 10