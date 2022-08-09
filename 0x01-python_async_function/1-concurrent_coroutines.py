#!/usr/bin/env python3
""" Async routine """


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Function that spawn wait_random n times with
        the specified max_delay, and return  the list of all the delays
    """
    rand_list = []
    for i in range(n):
        rand_list.append(await wait_random(max_delay))
    return sorted(rand_list)
