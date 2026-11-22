# Datheon Python Programming Internship

Official project repository for the **Datheon Python Programming Internship** (Application ID: `DT-2026-LSOJW`, Batch 01).

This repository contains all 4 standard internship tasks built purely using the Python 3 Standard Library with **100% free and open-source tools — zero paid models, subscriptions, or external API keys**.

---

## Task Overview

| Task | Title | Location | Core Libraries | Deliverables |
|---|---|---|---|---|
| **Task 1** | Hangman Word Guessing Game (Console) | `task1_hangman/` | `random`, string manipulation | `hangman.py`, `words.txt` |
| **Task 2** | Stock Portfolio Performance Tracker | `task2_stock_tracker/` | `csv`, file I/O | `portfolio.py`, `portfolio_summary.csv`, `sp500_tickers.csv` |
| **Task 3** | Automated File Organizer & Cleanup Utility | `task3_file_organizer/` | `pathlib`, `os.scandir`, `shutil` | `organizer.py`, `generate_test_files.py` |
| **Task 4** | Rule-Based Interactive Terminal Assistant / Chatbot | `task4_chatbot/` | `re` (regex), `json` | `chatbot.py`, `intents.json` |

---

## Repository Structure

```
Datheon_Python_Internship/
├── README.md
├── task1_hangman/
│   ├── hangman.py                    # Terminal Hangman game engine
│   ├── words.txt                     # English vocabulary bank
│   └── task1_hangman_demo.png        # Execution preview
├── task2_stock_tracker/
│   ├── portfolio.py                  # Portfolio valuation & calculations
│   ├── portfolio_summary.csv         # Generated performance summary log
│   ├── sp500_tickers.csv             # S&P 500 reference prices
│   └── task2_stock_portfolio.png     # Execution preview
├── task3_file_organizer/
│   ├── organizer.py                  # Directory sorting automation
│   ├── generate_test_files.py        # Sandbox clutter generator
│   └── task3_file_organizer.png      # Execution preview
└── task4_chatbot/
    ├── chatbot.py                    # Multi-intent conversational assistant
    ├── intents.json                  # Query regex patterns & responses
    └── task4_chatbot.png             # Execution preview
```

---

## Detailed Task Documentation & Execution

### Task 1: Hangman Word Guessing Game (Console)
- **Goal:** Build an interactive, modular console game implementing string manipulation and control flow.
- **Features:**
  - 7 progressive visual ASCII gallows art stages.
  - Guessed letters tracked using Python `set` structure.
  - Duplicate guess prevention without penalty deduction.
  - Secret word chosen dynamically from `words.txt` via `random.choice()`.
  - Clean victory and defeat screens with scoreboard.
- **Run Command:**
  ```bash
  python task1_hangman/hangman.py
  ```

![Task 1 - Hangman Game Demo](task1_hangman/task1_hangman_demo.png)

---

### Task 2: Stock Portfolio Performance Tracker
- **Goal:** Calculate real-time portfolio valuation and persist performance logs to CSV.
- **Features:**
  - Ticker position tracking with weighted-average cost basis.
  - Capital invested vs. current market value calculation.
  - Profit/Loss percentage breakdown per holding.
  - Automatic export to `portfolio_summary.csv` using the built-in `csv` module.
- **Run Command:**
  ```bash
  python task2_stock_tracker/portfolio.py
  ```

![Task 2 - Stock Portfolio Tracker Demo](task2_stock_tracker/task2_stock_portfolio.png)

---

### Task 3: Automated File Organizer & Cleanup Utility
- **Goal:** Automate filesystem operations and directory sorting using Python OS libraries.
- **Features:**
  - Extension mapping dictionary for `/Documents`, `/Images`, `/Videos`, `/Archives`, `/Code`, and `/Audio`.
  - High-performance directory inspection using `os.scandir()`.
  - Collision-safe moving (`shutil.move`) with auto-incrementing filenames (`file_1.ext`).
  - `--dry-run` flag to simulate operations safely without moving files.
  - Formatted execution summary with relocation counts and error handling.
- **Run Command:**
  ```bash
  # Step 1: Generate test sandbox
  python task3_file_organizer/generate_test_files.py

  # Step 2: Organize target folder
  python task3_file_organizer/organizer.py --path task3_file_organizer/test_sandbox
  ```

![Task 3 - File Organizer Demo](task3_file_organizer/task3_file_organizer.png)

---

### Task 4: Rule-Based Interactive Terminal Assistant / Chatbot
- **Goal:** Build a responsive conversational assistant with multi-intent recognition.
- **Features:**
  - Regular expression pattern matching against user queries loaded from `intents.json`.
  - Input normalization (case-folding, whitespace trimming, regex extraction).
  - Handles FAQ queries (program overview, deadline dates, task lists, certification requirements).
  - Contextual fallback replies for unrecognized inputs and clean termination (`exit`, `quit`, `bye`).
- **Run Command:**
  ```bash
  python task4_chatbot/chatbot.py
  ```

![Task 4 - Chatbot Demo](task4_chatbot/task4_chatbot.png)

---

## Submission Details

- **Program:** Datheon Python Programming Internship
- **Batch:** Batch 01 (Anna University)
- **Application ID:** `DT-2026-LSOJW`
- **Completed Tasks:** Task 1, Task 2, Task 3, Task 4 (All 4 Completed)
- **GitHub Repository:** [https://github.com/jeevicyber28/Datheon_Python_Internship](https://github.com/jeevicyber28/Datheon_Python_Internship)
