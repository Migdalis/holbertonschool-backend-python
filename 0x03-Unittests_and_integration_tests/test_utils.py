#!/usr/bin/env python3
""" Module to testing """
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test the utils class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expect_out):
        """ Method to test that the method returns what it is supposed to """
        real_out = access_nested_map(map, path)
        self.assertEqual(real_out, expect_out)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        """ Method to test that a KeyError is raised for the inputs """
        self.assertRaises(KeyError, access_nested_map, map, path)

class TestGetJson(unittest.TestCase):
    """ Class to test the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Method to test that returns correct output """
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class to test the memoization function """

    def test_memoize(self):
        """ Method to test that memoize return the correct result """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method that always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Method that returns a memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            tst = TestClass()
            self.assertEqual(tst.a_property, mock.return_value)
            self.assertEqual(tst.a_property, mock.return_value)
            mock.asset_called_once()
