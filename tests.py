import unittest
from datetime import datetime, timedelta
from last_seen_formatter import format_last_seen

class TestFormatter(unittest.TestCase):

    def test_format_last_seen_just_now(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(seconds=10)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "just now")

    def test_format_last_seen_less_than_a_minute_ago(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(seconds=40)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "less than a minute ago")

    def test_format_last_seen_couple_of_minutes_ago(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(minutes=30)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "couple of minutes ago")

    def test_format_last_seen_hour_ago(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(hours=1, minutes=30)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "hour ago")

    def test_format_last_seen_today(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(hours=3)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "today")

    def test_format_last_seen_yesterday(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(days=1)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "yesterday")

    def test_format_last_seen_this_week(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(days=5)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "this week")

    def test_format_last_seen_long_time_ago(self):
        current_time = datetime.now()
        last_seen = current_time - timedelta(days=8)
        self.assertEqual(format_last_seen(last_seen.timestamp()), "long time ago")

if __name__ == "__main__":
    unittest.main()
