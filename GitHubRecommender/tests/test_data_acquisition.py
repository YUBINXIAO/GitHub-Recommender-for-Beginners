import unittest
from GitHubRecommender.data_acquisition import fetch_repositories, fetch_contributors_count, parse_repositories

class TestDataAcquisition(unittest.TestCase):
    
    def test_fetch_repositories(self):
        """Test fetch_repositories function with valid inputs."""
        result = fetch_repositories('python', 100)
        self.assertIsInstance(result, list)  # Checks if the result is a list
        self.assertGreater(len(result), 0)    # Checks if at least one repository is returned

    def test_fetch_contributors_count(self):
        """Test fetch_contributors_count function with a known repository."""
        # Using a known repository URL for testing
        test_url = 'https://api.github.com/repos/python/cpython'
        result = fetch_contributors_count(test_url)
        self.assertIsInstance(result, int)   # Checks if the result is an integer
        self.assertGreater(result, 0)        # Checks if the contributors count is greater than 0

    def test_parse_repositories(self):
        """Test parse_repositories function with a sample data."""
        sample_data = [
            {
                'name': 'sample_repo',
                'stargazers_count': 150,
                'language': 'Python',
                'html_url': 'https://github.com/sample/sample_repo'
            }
        ]
        result = parse_repositories(sample_data)
        self.assertIsInstance(result, list)              # Checks if the result is a list
        self.assertEqual(len(result), 1)                 # Checks if the list contains one item
        self.assertEqual(result[0]['name'], 'sample_repo')  # Checks if the name is correctly parsed

if __name__ == '__main__':
    unittest.main()

    
    



