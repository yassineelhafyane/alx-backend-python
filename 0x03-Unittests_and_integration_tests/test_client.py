#!/usr/bin/env python3
"""
Test module for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized

# Assuming GithubOrgClient and get_json are defined in client.py
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
        """
            TestGithubOrgClient class to test GithubOrgClient methods.
                """

                    @parameterized.expand([
                                ("google",),
                                        ("abc",),
                                            ])
                        @patch('client.get_json')
                            def test_org(self, org_name: str, mock_get_json):
                                        """
                                                Test that GithubOrgClient.org returns the correct value.
                                                        """
                                                                # Setup the mock to return a specific value
                                                                        expected_return_value = {"login": org_name}
                                                                                mock_get_json.return_value = expected_return_value

                                                                                        # Instantiate the client
                                                                                                client = GithubOrgClient(org_name)

                                                                                                        # Call the org method and check the result
                                                                                                                result = client.org
                                                                                                                        self.assertEqual(result, expected_return_value)

                                                                                                                                # Ensure get_json was called once with the expected URL
                                                                                                                                        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                unittest.main()
#!/usr/bin/env python3
"""
Test module for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized

# Assuming GithubOrgClient and get_json are defined in client.py
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
        """
            TestGithubOrgClient class to test GithubOrgClient methods.
                """

                    @parameterized.expand([
                                ("google",),
                                        ("abc",),
                                            ])
                        @patch('client.get_json')
                            def test_org(self, org_name: str, mock_get_json):
                                        """
                                                Test that GithubOrgClient.org returns the correct value.
                                                        """
                                                                # Setup the mock to return a specific value
                                                                        expected_return_value = {"login": org_name}
                                                                                mock_get_json.return_value = expected_return_value

                                                                                        # Instantiate the client
                                                                                                client = GithubOrgClient(org_name)

                                                                                                        # Call the org method and check the result
                                                                                                                result = client.org
                                                                                                                        self.assertEqual(result, expected_return_value)

                                                                                                                                # Ensure get_json was called once with the expected URL
                                                                                                                                        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                unittest.main()

