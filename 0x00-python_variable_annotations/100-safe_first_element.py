#!/usr/bin/env python3
'''
Augment the following code with the correct duck-typed annotations
'''

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Args:
        lst (Sequence[Any]): sequence of elements of unknown type.

    Returns:
        Union[Any, None]: first element of the sequence if it exists,
        otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None
