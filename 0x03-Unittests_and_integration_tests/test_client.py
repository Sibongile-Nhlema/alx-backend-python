#!/usr/bin/env python3
'''
Unit tests for GithubOrgClient class.
'''

import unittest
from typing import Dict
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''
    Unit tests for GithubOrgClient class.
    '''

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 mock_get_json: unittest.mock.Mock) -> None:
        '''
        Test that GithubOrgClient.org returns the correct value.
        '''
        client: GithubOrgClient = GithubOrgClient(org_name)
        mock_url: str = GithubOrgClient.ORG_URL.format(org=org_name)

        mock_get_json.return_value = {"org_name": org_name}
        org_info: Dict[str, str] = client.org() # error on this line

        self.assertEqual(org_info["org_name"], org_name)
        mock_get_json.assert_called_once_with(mock_url)


if __name__ == '__main__':
    unittest.main()
