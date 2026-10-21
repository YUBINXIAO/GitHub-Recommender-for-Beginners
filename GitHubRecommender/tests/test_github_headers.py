import base64
import importlib
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

PACKAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_DIR)

import data_acquisition as da
import fetch_repos


class TestGitHubHeaders(unittest.TestCase):
    """Authorization is sent only when GITHUB_TOKEN is set. No live HTTP."""

    def test_headers_include_token_only_when_set(self):
        """github_headers() adds Authorization only for a non-empty token."""
        with patch.dict(os.environ, {'GITHUB_TOKEN': 'test-token'}):
            headers = da.github_headers()
        self.assertEqual(headers['Authorization'], 'token test-token')
        self.assertEqual(headers['Accept'], 'application/vnd.github.v3+json')

        with patch.dict(os.environ, {'GITHUB_TOKEN': ''}):
            headers = da.github_headers()
        self.assertNotIn('Authorization', headers)

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop('GITHUB_TOKEN', None)
            headers = da.github_headers()
        self.assertNotIn('Authorization', headers)
        self.assertEqual(headers['Accept'], 'application/vnd.github.v3+json')

    def test_api_calls_send_token_only_when_set(self):
        """Search, README, branch, and issue calls use those headers."""
        readme_payload = {
            'content': base64.b64encode(b'hello').decode('ascii')
        }
        search_payload = {
            'items': [{
                'full_name': 'owner/repo',
                'stargazers_count': 1200,
            }]
        }

        def fake_get(url, headers=None, **kwargs):
            recorded.append(headers)
            response = MagicMock()
            response.status_code = 200
            response.text = ''
            if url.endswith('/readme'):
                response.json.return_value = readme_payload
            elif url.endswith('/issues'):
                response.json.return_value = []
            elif '/search/repositories' in url:
                response.json.return_value = search_payload
            else:
                response.json.return_value = {'default_branch': 'main'}
            return response

        calls = [
            lambda: da.fetch_readme('owner/repo'),
            lambda: da.fetch_default_branch('owner/repo'),
            lambda: da.fetch_issues('owner/repo'),
            lambda: da.fetch_repositories('python', 1000),
        ]

        for token in ('test-token', None):
            recorded = []
            env = {}
            if token is not None:
                env['GITHUB_TOKEN'] = token
            with patch.dict(os.environ, env, clear=False):
                if token is None:
                    os.environ.pop('GITHUB_TOKEN', None)
                with patch('data_acquisition.requests.get', side_effect=fake_get):
                    for call in calls:
                        call()

            self.assertGreater(len(recorded), 0)
            for headers in recorded:
                if token:
                    self.assertEqual(headers['Authorization'], 'token ' + token)
                else:
                    self.assertNotIn('Authorization', headers)

    def test_fetch_repos_sends_token_only_when_set(self):
        """fetch_repos.py search uses GITHUB_TOKEN the same way."""
        payload = {
            'items': [{'name': 'repo', 'stargazers_count': 5}],
            'total_count': 1,
        }
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = payload

        with patch.dict(os.environ, {'GITHUB_TOKEN': 'test-token'}):
            with patch('fetch_repos.requests.get', return_value=response) as mock_get:
                fetch_repos.fetch_github_repositories(max_repos=1)
        headers = mock_get.call_args.kwargs['headers']
        self.assertEqual(headers['Authorization'], 'token test-token')

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop('GITHUB_TOKEN', None)
            with patch('fetch_repos.requests.get', return_value=response) as mock_get:
                fetch_repos.fetch_github_repositories(max_repos=1)
        headers = mock_get.call_args.kwargs['headers']
        self.assertNotIn('Authorization', headers)

    def test_import_does_not_call_the_network(self):
        """Importing data_acquisition must not fetch repositories or news."""
        with patch('data_acquisition.requests.get') as mock_get:
            importlib.reload(da)
        mock_get.assert_not_called()


if __name__ == '__main__':
    unittest.main()
