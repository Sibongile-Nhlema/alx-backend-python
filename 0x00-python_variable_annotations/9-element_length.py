#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
'''
Annotate the below function’s parameters and
return values with the appropriate types
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Args:
        lst(list): given list value
    Returns:
        values with the right types
    '''
    return [(i, len(i)) for i in lst]
