#test_integration
import unittest
import main
import json

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        main.app.testing = True

    def test_get_all_users_stats_endpoint(self):
        response = self.app.get('/api/stats/users?date=2023-09-27T20:00:00')
        self.assertEqual(response.status_code, 200)
        data = response.json
        # Replace with the correct expected response
        expected_response = {"key": "value"}
        self.assertEqual(data, expected_response)
        data = json.loads(response.data)
        self.assertEqual(data["usersOnline"], 34)

    def test_get_single_user_stats_endpoint(self):
        response = self.app.get('/api/stats/user?date=2023-09-27T20:00:00&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)
        data = response.json
        # Replace with the correct expected response
        expected_response = {"key": "value"}
        self.assertEqual(data, expected_response)
        data = json.loads(response.data)
        self.assertTrue(data["wasUserOnline"])
        self.assertEqual(data["nearestOnlineTime"], "2023-09-27 19:00")
        self.assertEqual(data["pageViews"], 133.33)
        self.assertEqual(data["purchases"], 4)

    def test_predict_all_users_endpoint(self):
        response = self.app.get('/api/predictions/users?date=2025-09-27T20:00:00')
        self.assertEqual(response.status_code, 200)
        data = response.json
        # Replace with the correct expected response
        expected_response = {"key": "value"}
        self.assertEqual(data, expected_response)
        data = json.loads(response.data)
        self.assertEqual(data["onlineUsers"], 31)

    def test_predict_single_user_endpoint(self):
        response = self.app.get('/api/predictions/user?date=2025-09-27T20:00:00&tolerance=0.85&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 200)
        data = response.json
        # Replace with the correct expected response
        expected_response = {"key": "value"}
        self.assertEqual(data, expected_response)
        data = json.loads(response.data)
        self.assertTrue(data["willBeOnline"])

        self.assertAlmostEqual(data["onlineChance"], 0.67, places=2)


    def test_get_single_user_stats_endpoint_missing_date(self):
        response = self.app.get('/api/stats/user?userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 400)  # Bad request due to missing date

    def test_get_single_user_stats_endpoint_invalid_user(self):
        response = self.app.get('/api/stats/user?date=2023-09-27T20:00:00&userId=INVALID_USER')
        self.assertEqual(response.status_code, 404)  # User not found

    def test_predict_single_user_endpoint_invalid_tolerance(self):
        response = self.app.get('/api/predictions/user?date=2025-09-27T20:00:00&tolerance=invalid&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 400)  # Bad request due to invalid tolerance


    def test_get_single_user_stats_endpoint_missing_user(self):
        response = self.app.get('/api/stats/user?date=2023-09-27T20:00:00')
        self.assertEqual(response.status_code, 400)  # Bad request due to missing user

    def test_predict_single_user_endpoint_future_date(self):
        response = self.app.get('/api/predictions/user?date=2025-09-27T20:00:00&userId=A4DC2287-B03D-430C-92E8-02216D828709')
        self.assertEqual(response.status_code, 400)  # Bad request due to future date


if __name__ == '__main__':
    unittest.main()
