#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

'''
Annotate the below function’s parameters and
return values with the appropriate types.
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequence elements (e.g., lists, strings, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence from the input iterable
        and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
