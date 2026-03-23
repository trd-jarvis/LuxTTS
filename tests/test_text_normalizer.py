import unittest

from zipvoice.tokenizer.normalizer import EnglishTextNormalizer


class TestEnglishTextNormalizer(unittest.TestCase):
    def setUp(self):
        self.normalizer = EnglishTextNormalizer()

    def test_normalize_collapses_whitespace(self):
        text = "Dr.   Smith has  2   apples"
        self.assertEqual(
            self.normalizer.normalize(text),
            "doctor. Smith has two apples",
        )

    def test_normalize_expands_currency_fraction_percent(self):
        text = "I paid $1.50 for 1/2 cake at 25% off"
        self.assertEqual(
            self.normalizer.normalize(text),
            "I paid one dollar, fifty cents for one half cake at twenty-five percent off",
        )


if __name__ == "__main__":
    unittest.main()
