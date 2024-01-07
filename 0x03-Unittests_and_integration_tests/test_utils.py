#!/usr/bin/env python3
"""
does unit tests for utils
"""
from unittest import TestCase
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(TestCase):
    """
    In this task you will write the first unit test for
    utils.access_nested_map.

    Create a TestAccessNestedMap class that inherits from unittest.TestCase.

    Implement the TestAccessNestedMap.test_access_nested_map method
    to test that the method returns what it is supposed to.

    Decorate the method with @parameterized.expand to test the function for
    following inputs:
    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """test case"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Use the assertRaises context manager to test that a KeyError
        is raised for the following inputs (use @parameterized.expand):

        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    Define the TestGetJson(unittest.TestCase) class and implement the
    TestGetJson.test_get_json method to test that utils.get_json
    returns the expected result.

    We don't want to make any actual external HTTP calls.
    Use unittest.mock.patch to patch requests.get.
    Make sure it returns a Mock object with a json method that
    returns test_payload which you parametrize alongside the test_url that
    you will pass to get_json with the following inputs:

    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests case"""
        attributes = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attributes)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """
    Implement the TestMemoize(unittest.TestCase) class with a
    test_memoize method.

    Inside test_memoize, define following class

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    Use unittest.mock.patch to mock a_method. Test that when calling
    a_property twice,
    the correct result is returned but a_method is only called once
    using assert_called_once.
    """
    def test_memoize(self) -> None:
        """Test case"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
