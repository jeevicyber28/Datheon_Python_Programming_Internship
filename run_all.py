import os
import subprocess
import sys


def print_banner():
    print("=" * 60)
    print("      DATHEON PYTHON INTERNSHIP - TASK SUITE RUNNER")
    print("=" * 60)
    print("1. Task 1: Hangman Console Game (hangman.py)")
    print("2. Task 2: Stock Portfolio Tracker (portfolio.py)")
    print("3. Task 3: Directory Cleanup Utility (organizer.py)")
    print("4. Task 4: Rule-Based Assistant (chatbot.py)")
    print("5. Task 5: Inventory Asset System (inventory.py)")
    print("6. Run All Automated Unit Tests")
    print("7. Exit")
    print("=" * 60)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    actions = {
        "1": (os.path.join(base_dir, "task1_hangman", "hangman.py"), "task1_hangman"),
        "2": (os.path.join(base_dir, "task2_stock_tracker", "portfolio.py"), "task2_stock_tracker"),
        "3": (os.path.join(base_dir, "task3_file_organizer", "organizer.py"), "task3_file_organizer"),
        "4": (os.path.join(base_dir, "task4_chatbot", "chatbot.py"), "task4_chatbot"),
        "5": (os.path.join(base_dir, "task5_inventory_system", "inventory.py"), "task5_inventory_system"),
    }

    while True:
        print_banner()
        choice = input("Select an option (1-7): ").strip()

        if choice in actions:
            script_path, cwd_rel = actions[choice]
            target_cwd = os.path.join(base_dir, cwd_rel)
            print(f"\nLaunching {os.path.basename(script_path)}...\n")
            try:
                subprocess.run([sys.executable, script_path], cwd=target_cwd)
            except KeyboardInterrupt:
                print("\nInterrupted by user.")
            print("\nDone. Returning to main menu.\n")
        elif choice == "6":
            print("\nRunning unit test suite...\n")
            subprocess.run([sys.executable, "-m", "unittest", "discover", "tests"], cwd=base_dir)
            print("\nTests complete.\n")
        elif choice in ("7", "exit", "quit", "q"):
            print("\nExiting. Thank you!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
