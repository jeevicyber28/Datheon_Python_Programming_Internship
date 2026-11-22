import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task4_chatbot.chatbot import RuleBasedChatbot


class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.bot = RuleBasedChatbot()

    def test_greeting_intent(self):
        tag, resp = self.bot.match_intent("Hello there!")
        self.assertEqual(tag, "greeting")
        self.assertTrue(len(resp) > 0)

    def test_deadline_intent(self):
        tag, resp = self.bot.match_intent("What is the submission deadline?")
        self.assertEqual(tag, "deadline")
        self.assertIn("December 20, 2026", resp)

    def test_exit_intent(self):
        tag, resp = self.bot.match_intent("bye")
        self.assertEqual(tag, "exit")
        self.assertTrue(self.bot.is_exit_command(tag, "bye"))

    def test_fallback_intent(self):
        tag, resp = self.bot.match_intent("gibberishxyzquery123")
        self.assertEqual(tag, "fallback")
        self.assertIn("I'm sorry", resp)


if __name__ == "__main__":
    unittest.main()
