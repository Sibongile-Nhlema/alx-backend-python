#!/usr/bin/env python3
'''
Type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float, float], float]:
    '''
    Args:
        multiplier (float): float value given
    Returns:
        Callable (function): result of nultiplcation of multiplier and a float
    '''
    def float_multiplier(a: float) -> float:
        '''
        Args:
            a (float): value given
            multiplier (float): value recieved from make_multiplier
        Returns:
            ans (float): a multiplied by multiplier
        '''
        return a * multiplier
    return float_multiplier
