#!/usr/bin/env python3
'''
Annotate the below function’s parameters and
return values with the appropriate types.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Args:
        lst (Iterable[Sequence]): An iterable where each
        element is a sequence (e.g., list, string, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples.
        Each tuple contains a sequence from the input
        iterable and an integer representing the length of that sequence.
    '''
    return [(i, len(i)) for i in lst]
