#!/usr/bin/env python3
"""  Module to testing """

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized
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


if __name__ == '__main__':
    unittest.main()
