#!/usr/bin/env python3
"""
module declares a coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a coroutine
    """
    start_at = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_at
