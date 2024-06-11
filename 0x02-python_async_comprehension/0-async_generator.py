#!/usr/bin/env python3
'''
Coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second, then yield a random number
between 0 and 10. Use the random module.
'''

import random
import asyncio


async def async_generator():
    '''
    This coroutine loops 10 times and yields
    a random number between 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
