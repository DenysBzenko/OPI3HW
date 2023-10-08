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

if __name__ == '__main__':
    unittest.main()
