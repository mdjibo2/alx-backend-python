#!/usr/bin/env python3
"""
2. Measure the runtime
"""

import asyncio
from time import perf_counter
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of wait_n function
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()

    total_time = end_time - start_time
    return total_time / n

if __name__ == '__main__':
    n = 5
    max_delay = 9

    print(f"Average time: {measure_time(n, max_delay)} seconds")

