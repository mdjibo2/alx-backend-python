#!/usr/bin/env python3
"""Defines a function that spawns task_wait_random n times with the specified max_delay"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay"""
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

