#!/usr/bin/env python3
""" Asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Asynchronous coroutine that takes in an integer argument
        and waits for a random delay between 0 and max_delay
    """
    await asyncio.sleep(max_delay)
    return (random.uniform(0, max_delay))
