import unittest
from GitHubRecommender.data_processing import clean_and_transform, process_repositories

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {
                'name': 'Sample-Repo',
                'stargazers_count': 100,  
                'language': 'Python',
                'url': 'https://github.com/user/Sample-Repo',  
                'description': 'A sample repository',
                'updated_at': '2023-01-01T00:00:00Z'
            },
            {
                'name': 'Another-Repo',
                'stargazers_count': 50,  # Change to integer
                'language': 'JavaScript',
                'url': 'https://github.com/user/Another-Repo',  
                'description': 'Another repository',
                'updated_at': '2023-01-02T00:00:00Z'
            }
        ]

    def test_clean_and_transform(self):
        transformed_data = clean_and_transform(self.sample_data)
        self.assertEqual(len(transformed_data), 2)

        # Test if 'stars' are correctly converted to int
        self.assertIsInstance(transformed_data[0]['stars'], int)

        # Test if 'url' is correctly transformed
        self.assertEqual(transformed_data[0]['url'], 'user/Sample-Repo')

        # Test categorization based on stars
        self.assertEqual(transformed_data[0]['category'], 'Moderately Popular')
        self.assertEqual(transformed_data[1]['category'], 'Moderately Popular')

    def test_process_repositories(self):
        processed_data = process_repositories(self.sample_data)
        self.assertEqual(len(processed_data), 2)

        # Test the structure of processed data
        self.assertIn('name', processed_data[0])
        self.assertIn('description', processed_data[0])
        self.assertIn('language', processed_data[0])
        self.assertIn('stars', processed_data[0])
        self.assertIn('updated_at', processed_data[0])

        # Test if 'stars' and 'updated_at' are correctly extracted
        self.assertEqual(processed_data[0]['stars'], 100)
        self.assertEqual(processed_data[0]['updated_at'], '2023-01-01T00:00:00Z')

if __name__ == '__main__':
    unittest.main()

