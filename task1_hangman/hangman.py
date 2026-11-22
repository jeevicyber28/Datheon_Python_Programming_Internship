import os
import random
import sys
from typing import List, Set, Tuple

# 7 Visual ASCII Gallows Art Stages (0 to 6 incorrect guesses)
GALLOWS_STAGES: List[str] = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

FALLBACK_WORDS: List[str] = [
    "PYTHON", "DEVELOPER", "VARIABLE", "FUNCTION", "ITERATION",
    "RECURSION", "ALGORITHM", "DATABASE", "FRAMEWORK", "COMPILER",
    "TERMINAL", "KEYWORD", "OPERATOR", "DECORATOR", "GENERATOR"
]


def load_word_list(filepath: str) -> List[str]:
    """Load words from an external file or fallback to predefined list."""
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                words = [line.strip().upper() for line in f if line.strip().isalpha()]
            if words:
                return words
        except Exception:
            pass
    return FALLBACK_WORDS


def get_masked_word(secret_word: str, guessed_letters: Set[str]) -> str:
    """Return the masked word representation (e.g. '_ A _ H E O N')."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])


def is_word_guessed(secret_word: str, guessed_letters: Set[str]) -> bool:
    """Check if all unique letters in the secret word have been guessed."""
    return set(secret_word).issubset(guessed_letters)


def validate_guess(guess: str, guessed_letters: Set[str]) -> Tuple[bool, str]:
    """
    Validate user input:
    Returns (is_valid, error_message).
    """
    cleaned = guess.strip().upper()
    if len(cleaned) != 1:
        return False, "Please enter a single alphabetical character."
    if not cleaned.isalpha():
        return False, "Invalid input! Only letters (A-Z) are permitted."
    if cleaned in guessed_letters:
        return False, f"You already guessed '{cleaned}'. Duplicate guess - no penalty deducted!"
    return True, ""


def play_game(secret_word: str, max_mistakes: int = 6) -> bool:
    """Run an interactive round of Hangman. Returns True on win, False on defeat."""
    secret_word = secret_word.upper()
    guessed_letters: Set[str] = set()
    mistakes = 0

    print("\n" + "=" * 50)
    print("      WELCOME TO HANGMAN (WORD GUESSING GAME)")
    print("=" * 50)
    print(f"Guess the hidden word letter-by-letter. You have {max_mistakes} attempts allowed.\n")

    while mistakes < max_mistakes:
        print(GALLOWS_STAGES[mistakes])
        print(f"Word: {get_masked_word(secret_word, guessed_letters)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Mistakes remaining: {max_mistakes - mistakes}")

        try:
            user_input = input("\nEnter your guess letter (or 'quit' to exit): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGame exited by user.")
            return False

        if user_input.lower() in ("quit", "exit"):
            print(f"\nGame aborted. The word was: {secret_word}")
            return False

        is_valid, msg = validate_guess(user_input, guessed_letters)
        if not is_valid:
            print(f"-> {msg}")
            continue

        guessed_char = user_input.upper()
        guessed_letters.add(guessed_char)

        if guessed_char in secret_word:
            print(f"-> Good job! '{guessed_char}' is in the word.")
            if is_word_guessed(secret_word, guessed_letters):
                print(GALLOWS_STAGES[mistakes])
                print("\n" + "*" * 50)
                print(f"  VICTORY! You guessed the word: {secret_word}")
                print("*" * 50)
                return True
        else:
            mistakes += 1
            print(f"-> Sorry, '{guessed_char}' is NOT in the word.")

    print(GALLOWS_STAGES[mistakes])
    print("\n" + "x" * 50)
    print(f"  DEFEAT! You ran out of attempts.")
    print(f"  The correct word was: {secret_word}")
    print("x" * 50)
    return False


def main():
    words_file = os.path.join(os.path.dirname(__file__), "words.txt")
    word_bank = load_word_list(words_file)

    wins = 0
    losses = 0

    while True:
        target_word = random.choice(word_bank)
        result = play_game(target_word)
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\nCurrent Scoreboard -> Wins: {wins} | Losses: {losses}")
        try:
            again = input("Do you want to play another round? (y/n): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break

        if again not in ("y", "yes"):
            print("\nThank you for playing Datheon Hangman! Goodbye.")
            break


if __name__ == "__main__":
    main()
