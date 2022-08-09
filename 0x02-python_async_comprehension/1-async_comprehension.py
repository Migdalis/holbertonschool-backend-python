#!/usr/bin/env python3
""" Module for Async Comprehension """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        This coroutine will collect 10 random numbers using an async
        comprehensing over async_generator, then return the 10 random numbers
    """
    comp_list = [i async for i in async_generator()]
    return comp_list
