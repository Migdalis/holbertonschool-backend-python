#!/usr/bin/env python3
""" Module about async routines and coroutines """
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Function that spawn task_wait_random n times with
        the specified max_delay, and return  the list of all the delays
    """
    rand_list = []
    for i in range(n):
        rand_list.append(await task_wait_random(max_delay))
    return sorted(rand_list)
