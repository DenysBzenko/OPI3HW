import unittest
from unittest.mock import patch
from main import fetch_users

class TestLoadingLoop(unittest.TestCase):

    @patch('main.fetch_all_users_data')
    def test_fetch_users_successful(self, mock_fetch):

        mock_fetch.return_value = [
            {
                'nickname': 'JohnDoe',
                'firstName': 'John',
                'lastName': 'Doe',
                'lastSeen': 1672502400
            }
        ]
        result = fetch_users()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['nickname'], 'JohnDoe')

    @patch('main.fetch_all_users_data')
    def test_fetch_users_empty(self, mock_fetch):

        mock_fetch.return_value = []
        result = fetch_users()
        self.assertEqual(len(result), 0)

    @patch('main.fetch_all_users_data')
    def test_fetch_users_failure(self, mock_fetch):

        mock_fetch.side_effect = Exception("API Error")
        with self.assertRaises(Exception):
            fetch_users()

if __name__ == "__main__":
    unittest.main()
