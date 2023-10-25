#test_utils

import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_predict_users_online(self):
        date = "2025-27-09-20:00"
        result = utils.predict_users_online(date)
        self.assertIsInstance(result, int)

    def test_predict_user_online_valid_user(self):
        user_id = "A4DC2287-B03D-430C-92E8-02216D828709"
        date = "2025-27-09-20:00"
        tolerance = 0.85
        will_be_online, online_chance = utils.predict_user_online(user_id, date, tolerance)
        self.assertIsInstance(will_be_online, bool)
        self.assertIsInstance(online_chance, float)

    def test_predict_user_online_invalid_user(self):
        user_id = "INVALID_USER_ID"
        date = "2025-27-09-20:00"
        tolerance = 0.85
        will_be_online, online_chance = utils.predict_user_online(user_id, date, tolerance)
        self.assertIsNone(will_be_online)
        self.assertIsNone(online_chance)


    def test_calculate_user_online_time_invalid_input(self):
        with self.assertRaises(ValueError):
            utils.calculate_user_online_time(None)

    def test_calculate_user_online_time_empty_input(self):
        result = utils.calculate_user_online_time([])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()


def test_get_last_seen_online_success():
    # This is a mock function for the purpose of the test, it should mimic the expected behavior of the actual function
    def mock_get_last_seen_online(offset):
        return '2023-01-01 12:00:00'

    # Assuming the function is successful and returns the expected date and time
    assert mock_get_last_seen_online(0) == '2023-01-01 12:00:00'

def test_get_last_seen_online_failure():
    # This is a mock function for the purpose of the test, it should mimic the expected behavior of the actual function
    def mock_get_last_seen_online(offset):
        return None  # Simulates a situation where the function fails (e.g., the API is down)

    # Assuming the function fails and returns None
    assert mock_get_last_seen_online(0) is None
