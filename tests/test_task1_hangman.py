import unittest
import os
import sys

# Ensure tasks are importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task1_hangman.hangman import (
    get_masked_word,
    is_word_guessed,
    validate_guess,
    load_word_list
)


class TestHangman(unittest.TestCase):

    def test_masked_word_initial(self):
        secret = "PYTHON"
        guessed = set()
        masked = get_masked_word(secret, guessed)
        self.assertEqual(masked, "_ _ _ _ _ _")

    def test_masked_word_partial(self):
        secret = "PYTHON"
        guessed = {"P", "O"}
        masked = get_masked_word(secret, guessed)
        self.assertEqual(masked, "P _ _ _ O _")

    def test_is_word_guessed(self):
        secret = "DATHEON"
        guessed = {"D", "A", "T", "H", "E", "O", "N"}
        self.assertTrue(is_word_guessed(secret, guessed))

        partial = {"D", "A", "T"}
        self.assertFalse(is_word_guessed(secret, partial))

    def test_validate_guess_valid(self):
        is_valid, msg = validate_guess("A", set())
        self.assertTrue(is_valid)
        self.assertEqual(msg, "")

    def test_validate_guess_duplicate(self):
        guessed = {"A", "B"}
        is_valid, msg = validate_guess("A", guessed)
        self.assertFalse(is_valid)
        self.assertIn("Duplicate guess", msg)

    def test_validate_guess_invalid_characters(self):
        is_valid, msg = validate_guess("1", set())
        self.assertFalse(is_valid)

        is_valid, msg = validate_guess("AB", set())
        self.assertFalse(is_valid)


if __name__ == "__main__":
    unittest.main()
