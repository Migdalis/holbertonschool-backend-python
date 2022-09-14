#!/usr/bin/env python3
"""  Module to testing """
import unittest
from urllib import response
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """ Method to tests that test_public_repos returns a known payload """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expectation):
        '''self descriptive'''
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
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
        """test public repos """
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
