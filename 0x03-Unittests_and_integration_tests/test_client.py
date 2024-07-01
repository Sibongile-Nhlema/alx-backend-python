#!/usr/bin/env python3
'''
Unit tests for GithubOrgClient class.
'''

import unittest
from typing import Dict
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: unittest.mock.Mock) -> None:
        '''
        Tests the public_repos_url property of GithubOrgClient.
        '''
        mock_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        mock_org.return_value = mock_payload

        client: GithubOrgClient = GithubOrgClient("test_org")
        repos_url: str = client._public_repos_url

        self.assertEqual(repos_url, mock_payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
