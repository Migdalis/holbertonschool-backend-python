#!/usr/bin/env python3
""" Module with type-annotated """
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Args:
            lst (List): List of elements
        Returns:
            A list of tuples
    """
    return [(i, len(i)) for i in lst]
