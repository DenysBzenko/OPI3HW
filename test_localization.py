import unittest
from localization import translate

class TestLocalization(unittest.TestCase):

    def test_translation_english(self):
        self.assertEqual(translate("just now", "en"), "just now")

    def test_translation_ukrainian(self):
        self.assertEqual(translate("just now", "uk"), "щойно")

    def test_translation_arabic(self):
        self.assertEqual(translate("just now", "ar"), "الآن")

    def test_translation_french(self):
        self.assertEqual(translate("just now", "fr"), "à l'instant")

    def test_translation_invalid_language(self):
        self.assertEqual(translate("just now", "de"), "just now")  # Should default to English

if __name__ == "__main__":
    unittest.main()
