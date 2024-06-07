#!/usr/bin/env python3
'''
type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Args:
        mxd_lst (List[float]): The list of floats and intergers to sum.
    Returns:
        float: The sum of the list of floats and intergers.
    '''
    return float(sum(mxd_lst))
