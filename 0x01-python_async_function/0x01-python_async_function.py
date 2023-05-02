#!/usr/bin/env python3
'''
async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay
'''


import asyncio
from typing import List
from random import uniform
from time import perf_counter


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (inclusive) seconds and eventually returns it.

    Args:
        max_delay (int): Maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: Random delay between 0 and max_delay seconds (inclusive).
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns n instances of the wait_random coroutine
    with the specified max_delay, and returns a sorted list of the resulting
    delays.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum number of seconds to wait for each coroutine.

    Returns:
        List[float]: List of delays returned by each coroutine, sorted in
        ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)


async def main():
    """
    Asynchronous main function that calls the wait_n coroutine with various
    n and max_delay values, and prints the resulting delays.
    """
    start_time = perf_counter()
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))
    end_time = perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


asyncio.run(main())

