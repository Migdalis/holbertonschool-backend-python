#!/usr/bin/env python3
"""  Module to testing """

import unittest
from unittest import result
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test client.GithubOrgClient """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """ Method to tests that GithubOrgClient.org
        returns the correct value """
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Method to tests that _public_repos_url returns a known payload """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            rsps = GithubOrgClient(name)._public_repos_url
            self.assertEqual(rsps, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ Method to tests that test_public_repos returns a known payload """
        load = [{"name": "Google"}, {"name": "TT"}]
        get_json_mock.return_value = load

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Method to tests that has_license returns the correct values """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test class to Integration """
    @classmethod
    def setUpClass(cls):
        """ SetUpClass method """
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass method """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Mehod to test GithubOrgClient.public_repos """
        ghc = GithubOrgClient('random')
        self.assertEqual(ghc.org, self.org_payload)
        self.assertEqual(ghc.repos_payload, self.repos_payload)

    def test_public_repos_with_license(self):
        """ Method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True


if __name__ == '__main__':
    unittest.main()
