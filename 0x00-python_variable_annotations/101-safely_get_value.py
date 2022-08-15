#!/usr/bin/env python3
""" Module with type-annotated """
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        Returns:
            Value of the key or None if not exist
    """
    if key in dct:
        return dct[key]
    else:
        return default
