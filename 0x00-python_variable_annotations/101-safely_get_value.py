#!/usr/bin/env python3
'''
More involved type annotations
'''

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    Args:
        dct (Mapping[Any, Any]): dictionary-like structure
        key (Any): key to look for in the dic
        default (Union[T, None]): default value to
        return if the key is not found

    Returns:
        Union[Any, T]: value associated with key
        if it exists, otherwise default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
