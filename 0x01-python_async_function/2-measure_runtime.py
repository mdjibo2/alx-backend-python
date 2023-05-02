#!/usr/bin/env python3
"""Defines a function that measures the total execution time for wait_n(n, max_delay)"""
import time
import asyncio
from typing import List


measure_time = __import__('2-measure_runtime').measure_time


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

