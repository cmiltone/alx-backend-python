#!/usr/bin/env python3
"""
does unit tests for GithubOrgClient
"""
from unittest import TestCase
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """
    tests that GithubOrgClient.org returns the correct value.

    Use @patch as a decorator to make sure get_json is
    called once with the expected argument but make sure it is not executed.

    Use @parameterized.expand as a decorator to parametrize the test with a
    couple of org examples to pass to GithubOrgClient, in this order:

    google
    abc
    Of course, no external HTTP calls should be made.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """test case"""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """
        Test case
        Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url.

        Use patch as a context manager to patch GithubOrgClient.org
        and make it return a known payload.

        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
