import unittest
import models

class TestModels(unittest.TestCase):

    def test_get_users_online(self):
        date = "2023-09-27 20:00"
        result = models.get_users_online(date)
        self.assertIsInstance(result, int)

    def test_get_user_online_status_valid_user(self):
        user_id = "A4DC2287-B03D-430C-92E8-02216D828709"
        date = "2023-09-27 20:00"
        was_online, nearest_online_time, page_views, purchases = models.get_user_online_status(user_id, date)
        self.assertIsInstance(was_online, bool)
        self.assertIsInstance(nearest_online_time, str)
        self.assertIsInstance(page_views, float)
        self.assertIsInstance(purchases, int)

    def test_get_user_online_status_invalid_user(self):
        user_id = "INVALID_USER_ID"
        date = "2023-09-27 20:00"
        was_online, nearest_online_time, page_views, purchases = models.get_user_online_status(user_id, date)
        self.assertIsNone(was_online)
        self.assertIsNone(nearest_online_time)
        self.assertIsNone(page_views)
        self.assertIsNone(purchases)

if __name__ == '__main__':
    unittest.main()
