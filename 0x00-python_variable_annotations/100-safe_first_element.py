#!/usr/bin/env python3
""" Module with type-annotated """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Return the first element in the list or None
    """
    if lst:
        return lst[0]
    else:
        return None
