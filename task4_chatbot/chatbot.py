import json
import os
import random
import re
from typing import Any, Dict, List, Optional, Tuple


class RuleBasedChatbot:
    def __init__(self, dataset_path: Optional[str] = None):
        self.intents: List[Dict[str, Any]] = []
        if dataset_path and os.path.exists(dataset_path):
            self.load_intents_from_json(dataset_path)
        else:
            self._load_fallback_intents()

    def load_intents_from_json(self, filepath: str) -> None:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.intents = data.get("intents", [])
        except Exception as e:
            print(f"Warning: Failed to load intents file: {e}. Using fallback dataset.")
            self._load_fallback_intents()

    def _load_fallback_intents(self) -> None:
        self.intents = [
            {
                "tag": "greeting",
                "patterns": [r"\b(hi|hello|hey|good\s*morning)\b"],
                "responses": ["Hello! How can I help you with your Datheon internship today?"]
            },
            {
                "tag": "deadline",
                "patterns": [r"\b(deadline|cutoff|when\s*to\s*submit)\b"],
                "responses": ["The official deadline is Sunday, December 20, 2026."]
            },
            {
                "tag": "exit",
                "patterns": [r"\b(bye|exit|quit|goodbye)\b"],
                "responses": ["Goodbye! Best wishes with your project submission."]
            }
        ]

    def normalize_input(self, text: str) -> str:
        """Lowercases text, trims whitespaces, and removes excessive punctuation."""
        return re.sub(r"[^\w\s]", " ", text.lower()).strip()

    def match_intent(self, user_message: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Matches normalized message against compiled regex patterns.
        Returns (tag, response).
        """
        normalized = self.normalize_input(user_message)
        if not normalized:
            return None, "Please type a question or command."

        for intent in self.intents:
            tag = intent.get("tag", "general")
            patterns = intent.get("patterns", [])
            for pattern in patterns:
                if re.search(pattern, normalized, re.IGNORECASE):
                    responses = intent.get("responses", [])
                    return tag, random.choice(responses) if responses else "Understood."

        return "fallback", (
            "I'm sorry, I didn't quite catch that. You can ask me about:\n"
            " - 'What is Datheon?'\n"
            " - 'What are the tasks?'\n"
            " - 'When is the deadline?'\n"
            " - 'How does certification work?'\n"
            " - Or type 'exit' to quit."
        )

    def is_exit_command(self, tag: Optional[str], raw_text: str) -> bool:
        if tag == "exit":
            return True
        return raw_text.strip().lower() in ("bye", "exit", "quit", "q")

    def run_interactive(self) -> None:
        print("\n" + "=" * 60)
        print("    DATHEON INTERACTIVE TERMINAL ASSISTANT (CHATBOT)")
        print("=" * 60)
        print("Hello! Ask questions regarding the internship, Python tasks, or guidelines.")
        print("Type 'exit', 'quit', or 'bye' to end the session.\n")

        while True:
            try:
                user_input = input("You: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nSession ended.")
                break

            if not user_input:
                continue

            tag, response = self.match_intent(user_input)
            print(f"Bot: {response}\n")

            if self.is_exit_command(tag, user_input):
                break


def main():
    base_dir = os.path.dirname(__file__)
    intents_path = os.path.join(base_dir, "intents.json")
    bot = RuleBasedChatbot(intents_path)
    bot.run_interactive()


if __name__ == "__main__":
    main()
