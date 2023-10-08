import unittest
import main
import models
import utils

class TestIntegration(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_get_all_users_stats_endpoint(self):
        response = self.app.get('/api/stats/users?date=2023-27-09-20:00')
        self.assertEqual(response.status_code, 200)

    def test_get_single_user_stats_endpoint(self):
        response = self.app.get('/api/stats/user?date=2023-27-09-20:00&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)

    def test_predict_all_users_endpoint(self):
        response = self.app.get('/api/predictions/users?date=2025-27-09-20:00')
        self.assertEqual(response.status_code, 200)

    def test_predict_single_user_endpoint(self):
        response = self.app.get('/api/predictions/user?date=2025-27-09-20:00&tolerance=0.85&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
