#!/usr/bin/env python3
''''
Unittest for the utils.access_nested_map method
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Tuple, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    '''
    Tests for the access_nested_map method
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Any) -> None:
        '''
        Test access_nested_map with various inputs
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])

    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                               path: Tuple[str, ...]) -> None:
        '''
        Tests access_nested_map with invalid inputs
        '''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


if __name__ == '__main__':
    unittest.main()
