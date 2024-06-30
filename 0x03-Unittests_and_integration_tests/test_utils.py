#!/usr/bin/env python3
''''
Unittest for the utils.access_nested_map method
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from typing import Tuple, Dict, Any
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    '''
    Tests for the get_json function
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    def test_get_json(self, test_url: str, test_payload: Dict[str, Any]) -> None:
        '''
        Test get_json returns the expected result and makes a single call
        '''
        with patch('utils.requests.get') as mock_get:
            # Create a mock response object with a json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
