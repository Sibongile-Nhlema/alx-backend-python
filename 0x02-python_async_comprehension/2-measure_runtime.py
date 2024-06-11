#!/usr/bin/env python3
'''
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
'''
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    A coroutine that executes async_comprehension 4 times in parallel
    using asyncio.gather
    '''
    start_time = time.time()

    # Run async_comprehension 4 times in parallel
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
