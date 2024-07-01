#!/usr/bin/env python3
'''
Unit tests for GithubOrgClient class.
'''

import unittest
from typing import Dict, List
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

    @patch('client.get_json')
    def test_public_repo(self, mock_get_json: unittest.mock.Mock) -> None:
        '''
        Tests that the list of repos is what we expect from the chosen payload
        Return Value was chosed as None
        '''
        mock_payload  = [
            {"name": "repoOne", "license": {"key": "mit"}},
            {"name": "repoTwo", "license": {"key": "apache-2.0"}},
            {"name": "repoThree", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client: GithubOrgClient = GithubOrgClient("test_org")
            repos: List[str] = client.public_repos()

            self.assertEqual(repos, ["repoOne", "repoTwo", "repoThree"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool) -> None:
        '''
        Tests the has_license method of GithubOrgClient
        '''
        result: bool = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
