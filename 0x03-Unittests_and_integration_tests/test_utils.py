#!/usr/bin/env python3
""" Module to testing """
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
