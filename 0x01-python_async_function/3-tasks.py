#!/usr/bin/env python3
"""
task 3
"""


import asyncio
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds (inclusive)
    and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int = 10) -> Coroutine:
    """
    Regular function that takes an integer max_delay and returns a asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))

