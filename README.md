# Datheon Python Internship - Project Portfolio

An enterprise-ready repository containing solutions for the **Datheon Python Programming Internship**. All components are written using Python 3 and its Standard Library, requiring **zero paid services, external subscriptions, or proprietary API keys**.

---

## Repository Overview

| Directory | Task Title | Primary Script | Core Technologies | Status |
|---|---|---|---|---|
| `task1_hangman/` | Hangman Word Guessing Game | `hangman.py` | String manipulation, ASCII art, Set data structure | Completed |
| `task2_stock_tracker/` | Stock Portfolio Performance Tracker | `portfolio.py` | File I/O, CSV parsing, Financial arithmetic | Completed |
| `task3_file_organizer/` | Autonomous File Cleanup Utility | `organizer.py` | `pathlib`, `os.scandir`, `shutil`, collision resolution | Completed |
| `task4_chatbot/` | Rule-Based Terminal Assistant | `chatbot.py` | Regular expressions, Intent matching, JSON state | Completed |
| `task5_inventory_system/` | Enterprise Asset Inventory System | `inventory.py` | OOP, ABC (`abc`), Encapsulation, Dunder methods | Completed |
| `tests/` | Automated Unit Test Suite | `unittest` | 22 test cases validating business logic | Passing |

---

## Architecture & Design

```
Datheon_Python_Internship/
├── .gitignore
├── requirements.txt
├── run_all.py                   # Central interactive launcher
├── README.md
├── task1_hangman/
│   ├── hangman.py               # Hangman console game engine
│   └── words.txt                # Technical vocabulary word bank
├── task2_stock_tracker/
│   ├── portfolio.py             # Portfolio tracking and valuation
│   ├── portfolio_summary.csv    # Exported performance summary
│   └── sp500_tickers.csv        # Market pricing dataset
├── task3_file_organizer/
│   ├── organizer.py             # Autonomous directory sorter
│   └── generate_test_files.py   # Test dataset generator
├── task4_chatbot/
│   ├── chatbot.py               # Multi-intent terminal chatbot
│   └── intents.json             # Intent mapping patterns & replies
├── task5_inventory_system/
│   ├── models.py                # Abstract Base Classes & derived assets
│   └── inventory.py             # Inventory manager & audit report generator
└── tests/
    ├── test_task1_hangman.py
    ├── test_task2_portfolio.py
    ├── test_task3_organizer.py
    ├── test_task4_chatbot.py
    └── test_task5_inventory.py
```

---

## Detailed Task Documentation

### Task 1: Hangman Console Game
- **Objective:** Interactive word-guessing game with visual gallows art and 6-attempt limit.
- **Key Features:**
  - 7 progressive visual ASCII stages.
  - Guess history tracking using Python `set` to avoid duplicate penalties.
  - Case-insensitive input validation with informative feedback.
  - External dictionary loader (`words.txt`) with an embedded fallback list.
- **Execution:**
  ```bash
  python task1_hangman/hangman.py
  ```

---

### Task 2: Stock Portfolio Performance Tracker
- **Objective:** Track financial holdings, evaluate gain/loss percentages, and persist logs to CSV.
- **Key Features:**
  - Encapsulated `Holding` and `PortfolioTracker` classes.
  - Dynamic weighted-average cost basis calculation on duplicate buys.
  - Automatic export to `portfolio_summary.csv` with timestamps and totals.
  - Benchmark market price integration from `sp500_tickers.csv`.
- **Execution:**
  ```bash
  python task2_stock_tracker/portfolio.py
  ```

---

### Task 3: Autonomous Directory Cleanup Utility
- **Objective:** Sort files by extension into dedicated categories and prevent collisions.
- **Key Features:**
  - Efficient file discovery using `os.scandir()`.
  - Built-in conflict resolution: appends unique index suffixes (e.g., `file_1.pdf`) to avoid overwriting.
  - Dry-run simulation flag (`--dry-run`) to test moves safely.
  - Structured execution summary reporting files moved and permission errors handled.
- **Execution:**
  ```bash
  # Generate sample cluttered files
  python task3_file_organizer/generate_test_files.py

  # Organize directory
  python task3_file_organizer/organizer.py --path task3_file_organizer/test_sandbox
  ```

---

### Task 4: Rule-Based Conversational Chatbot
- **Objective:** Contextual terminal assistant with regular expression intent classification.
- **Key Features:**
  - Multi-intent matching using regex patterns loaded from `intents.json`.
  - Input normalization (case flattening, punctuation stripping, whitespace trimming).
  - Graceful fallback guidance when questions are not recognized.
  - Clean exit mechanisms (`exit`, `quit`, `bye`).
- **Execution:**
  ```bash
  python task4_chatbot/chatbot.py
  ```

---

### Task 5: Enterprise Smart Inventory System (OOP Architecture)
- **Objective:** Production-grade asset management implementing strict Object-Oriented principles.
- **Key Features:**
  - **Abstraction:** Abstract Base Class `Item` via Python `abc.ABC` with mandatory methods (`calculate_late_fee`, `display_metadata`).
  - **Inheritance:** Derived classes `Book`, `Magazine`, and `DigitalMedia` implementing specialized logic.
  - **Encapsulation:** Private properties (`__price`, `__title`) with `@property` and `@setter` validation.
  - **Polymorphism:** Unique overdue penalty formulas per media class.
  - **Dunder Methods:** `__str__`, `__repr__`, `__eq__`, and `__len__`.
  - **Audit Reporting:** Tabular console reporting via `InventoryManager`.
- **Execution:**
  ```bash
  python task5_inventory_system/inventory.py
  ```

---

## Unified Test Suite

All modules are covered by automated unit tests using Python's standard `unittest` framework.

```bash
# Run all unit tests
python -m unittest discover tests -v
```

**Test Results:**
```
Ran 22 tests in 0.05s
OK
```

---

## Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeevicyber28/Datheon_Python_Internship.git
   cd Datheon_Python_Internship
   ```

2. **Run the interactive launcher:**
   ```bash
   python run_all.py
   ```

---

## License & Attribution

Developed by **Jeevi** for the **Datheon Python Programming Internship**.
Built completely with free and open-source standard libraries.
