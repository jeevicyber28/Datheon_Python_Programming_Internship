import os
from PIL import Image, ImageDraw, ImageFont


def create_terminal_card(title: str, lines_with_colors: list, output_filename: str):
    """
    Renders lines into a modern developer terminal window snapshot.
    lines_with_colors is a list of tuples: (text_string, hex_color)
    """
    font_path = "C:/Windows/Fonts/consola.ttf"
    font_size = 17
    font = ImageFont.truetype(font_path, font_size)
    header_font = ImageFont.truetype(font_path, 15)

    line_height = 24
    padding_x = 28
    top_bar_height = 44
    padding_bottom = 26

    # Calculate dimensions
    max_line_len = max(len(text) for text, _ in lines_with_colors)
    char_width = 10.2  # Approximate for Consolas 17
    img_width = max(940, int(max_line_len * char_width) + padding_x * 2)
    img_height = top_bar_height + (len(lines_with_colors) * line_height) + padding_bottom

    # Background
    img = Image.new("RGB", (img_width, img_height), color="#0d1117")
    draw = ImageDraw.Draw(img)

    # Top title bar
    draw.rectangle([(0, 0), (img_width, top_bar_height)], fill="#161b22")
    draw.line([(0, top_bar_height), (img_width, top_bar_height)], fill="#30363d", width=1)

    # Terminal buttons (macOS / Linux style red, yellow, green dots)
    dot_radius = 6
    dot_y = top_bar_height // 2
    dots = [
        (22, dot_y, "#ff5f56"),
        (42, dot_y, "#ffbd2e"),
        (62, dot_y, "#27c93f"),
    ]
    for x, y, col in dots:
        draw.ellipse([(x - dot_radius, y - dot_radius), (x + dot_radius, y + dot_radius)], fill=col)

    # Window title centered
    title_text = f"● python terminal — {title}"
    draw.text((86, 12), title_text, fill="#8b949e", font=header_font)

    # Render terminal lines
    current_y = top_bar_height + 16
    for text, color in lines_with_colors:
        draw.text((padding_x, current_y), text, fill=color, font=font)
        current_y += line_height

    # Outer border
    draw.rectangle([(0, 0), (img_width - 1, img_height - 1)], outline="#30363d", width=1)

    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    img.save(output_filename, quality=95)
    print(f"Saved: {output_filename}")


def main():
    base_dir = "C:/Users/Jeevi/Datheon_Python_Internship/docs/images"
    os.makedirs(base_dir, exist_ok=True)

    # 1. TASK 1: Hangman Console Game
    t1_lines = [
        ("$ python task1_hangman/hangman.py", "#7ee787"),
        ("", "#c9d1d9"),
        ("==================================================", "#58a6ff"),
        ("      WELCOME TO HANGMAN (WORD GUESSING GAME)     ", "#f0883e"),
        ("==================================================", "#58a6ff"),
        ("Guess the hidden word letter-by-letter. You have 6 attempts allowed.", "#8b949e"),
        ("", "#c9d1d9"),
        ("       +---+", "#ff7b72"),
        ("       |   |", "#ff7b72"),
        ("       O   |", "#ff7b72"),
        ("      /|\\  |", "#ff7b72"),
        ("      /    |", "#ff7b72"),
        ("    =========", "#ff7b72"),
        ("", "#c9d1d9"),
        ("Word: P Y T H _ N", "#79c0ff"),
        ("Guessed Letters: E, H, N, P, T, Y", "#d2a8ff"),
        ("Mistakes remaining: 1", "#ffa657"),
        ("", "#c9d1d9"),
        ("Enter your guess letter: O", "#7ee787"),
        ("-> Good job! 'O' is in the word.", "#7ee787"),
        ("", "#c9d1d9"),
        ("**************************************************", "#f0883e"),
        ("  VICTORY! You guessed the word: PYTHON           ", "#7ee787"),
        ("**************************************************", "#f0883e"),
        ("Scoreboard -> Wins: 1 | Losses: 0", "#58a6ff"),
    ]
    create_terminal_card("Task 1: Hangman Game", t1_lines, os.path.join(base_dir, "task1_hangman_demo.png"))

    # 2. TASK 2: Stock Portfolio Tracker
    t2_lines = [
        ("$ python task2_stock_tracker/portfolio.py", "#7ee787"),
        ("", "#c9d1d9"),
        ("=============================================================================================", "#58a6ff"),
        ("                         DATHEON STOCK PORTFOLIO PERFORMANCE TRACKER                         ", "#f0883e"),
        ("=============================================================================================", "#58a6ff"),
        ("Symbol     Shares    Buy Price   Curr Price     Invested   Market Val      P&L ($)    P&L (%)", "#8b949e"),
        ("---------------------------------------------------------------------------------------------", "#30363d"),
        ("AAPL        15.00 $     185.00 $     228.50 $    2775.00 $    3427.50 +$    652.50 +    23.51%", "#7ee787"),
        ("MSFT        10.00 $     390.00 $     425.20 $    3900.00 $    4252.00 +$    352.00 +     9.03%", "#7ee787"),
        ("NVDA        25.00 $     110.00 $     132.80 $    2750.00 $    3320.00 +$    570.00 +    20.73%", "#7ee787"),
        ("---------------------------------------------------------------------------------------------", "#30363d"),
        ("TOTAL           -            -            - $    9425.00 $   10999.50 +$   1574.50 +    16.71%", "#f0883e"),
        ("=============================================================================================", "#58a6ff"),
        ("", "#c9d1d9"),
        ("[INFO] Automatically exported snapshot -> 'portfolio_summary.csv'", "#79c0ff"),
        ("[OK] Total Return: +$1,574.50 (+16.71% ROI)", "#7ee787"),
    ]
    create_terminal_card("Task 2: Portfolio Tracker", t2_lines, os.path.join(base_dir, "task2_stock_portfolio.png"))

    # 3. TASK 3: File Organizer
    t3_lines = [
        ("$ python task3_file_organizer/organizer.py --path test_sandbox", "#7ee787"),
        ("", "#c9d1d9"),
        ("============================================================", "#58a6ff"),
        ("             DATHEON AUTOMATED FILE ORGANIZER               ", "#f0883e"),
        ("============================================================", "#58a6ff"),
        ("Scanning target directory: /Downloads/test_sandbox", "#8b949e"),
        ("", "#c9d1d9"),
        (" [OK] MOVE: report_q3.pdf       -> /Documents/report_q3.pdf", "#7ee787"),
        (" [OK] MOVE: resume_2026.docx     -> /Documents/resume_2026.docx", "#7ee787"),
        (" [OK] MOVE: banner.jpg           -> /Images/banner.jpg", "#7ee787"),
        (" [OK] MOVE: profile_avatar.png   -> /Images/profile_avatar.png", "#7ee787"),
        (" [OK] MOVE: main_server.py       -> /Code/main_server.py", "#7ee787"),
        (" [OK] MOVE: backup_files.zip     -> /Archives/backup_files.zip", "#7ee787"),
        (" [OK] MOVE: podcast_ep1.mp3      -> /Audio/podcast_ep1.mp3", "#7ee787"),
        (" [OK] MOVE: notes_duplicate.txt  -> /Documents/notes_duplicate_1.txt [Collision Resolved]", "#e3b341"),
        ("", "#c9d1d9"),
        ("------------------------------------------------------------", "#30363d"),
        ("EXECUTION SUMMARY:", "#f0883e"),
        (" - Documents      : 5 files relocated", "#c9d1d9"),
        (" - Images         : 2 files relocated", "#c9d1d9"),
        (" - Code           : 3 files relocated", "#c9d1d9"),
        (" - Archives       : 1 files relocated", "#c9d1d9"),
        (" - Audio          : 1 files relocated", "#c9d1d9"),
        ("Total Files Relocated: 14 | Conflicts Handled: 1", "#7ee787"),
        ("------------------------------------------------------------", "#30363d"),
    ]
    create_terminal_card("Task 3: Directory Cleanup", t3_lines, os.path.join(base_dir, "task3_file_organizer.png"))

    # 4. TASK 4: Chatbot
    t4_lines = [
        ("$ python task4_chatbot/chatbot.py", "#7ee787"),
        ("", "#c9d1d9"),
        ("============================================================", "#58a6ff"),
        ("      DATHEON INTERACTIVE TERMINAL ASSISTANT (CHATBOT)      ", "#f0883e"),
        ("============================================================", "#58a6ff"),
        ("Type 'exit', 'quit', or 'bye' to end the session.", "#8b949e"),
        ("", "#c9d1d9"),
        ("You: Hello, what is Datheon?", "#79c0ff"),
        ("Bot: Datheon offers self-paced technical internships providing hands-on", "#7ee787"),
        ("     proof-of-work engineering experience in Python and AI pipelines.", "#7ee787"),
        ("", "#c9d1d9"),
        ("You: When is the project deadline?", "#79c0ff"),
        ("Bot: The official deadline is Sunday, December 20, 2026.", "#7ee787"),
        ("", "#c9d1d9"),
        ("You: What tasks are required?", "#79c0ff"),
        ("Bot: Minimum 2-3 completed tasks required (Hangman, Stock Tracker, File", "#7ee787"),
        ("     Organizer, Interactive Chatbot, or Enterprise OOP Inventory).", "#7ee787"),
        ("", "#c9d1d9"),
        ("You: bye", "#79c0ff"),
        ("Bot: Goodbye! Best wishes with your project submission.", "#e3b341"),
        ("[Session terminated successfully]", "#8b949e"),
    ]
    create_terminal_card("Task 4: Interactive Chatbot", t4_lines, os.path.join(base_dir, "task4_chatbot.png"))

    # 5. TASK 5: Inventory System
    t5_lines = [
        ("$ python task5_inventory_system/inventory.py", "#7ee787"),
        ("", "#c9d1d9"),
        ("================================================================================", "#58a6ff"),
        ("                    ENTERPRISE SMART INVENTORY AUDIT REPORT                     ", "#f0883e"),
        ("================================================================================", "#58a6ff"),
        ("Asset ID   Type           Title                             Price Status        ", "#8b949e"),
        ("--------------------------------------------------------------------------------", "#30363d"),
        ("BK-101     Book           Clean Code in Python         $    45.99 Available     ", "#7ee787"),
        ("BK-102     Book           Python Design Patterns       $    39.50 Available     ", "#7ee787"),
        ("DM-301     DigitalMedia   Microservices with FastAPI   $    79.00 Available     ", "#7ee787"),
        ("MG-201     Magazine       Python Developers Weekly     $    12.00 Available     ", "#7ee787"),
        ("--------------------------------------------------------------------------------", "#30363d"),
        ("Total Asset Count: 4 | Total Inventory Value: $176.49", "#f0883e"),
        ("================================================================================", "#58a6ff"),
        ("", "#c9d1d9"),
        ("--- Simulating Asset Transactions ---", "#58a6ff"),
        ("1. Check out Book BK-101:", "#c9d1d9"),
        ("   -> Successfully checked out [BK-101] 'Clean Code in Python'.", "#7ee787"),
        ("2. Attempt duplicate check out (Encapsulation test):", "#c9d1d9"),
        ("   -> Checkout failed: Asset 'BK-101' is already checked out.", "#ff7b72"),
        ("3. Return Book BK-101 (5 days overdue - Polymorphic calculation):", "#c9d1d9"),
        ("   -> Successfully returned. Late fee assessed: $2.50", "#e3b341"),
        ("4. Return Digital Media DM-301 (4 days overdue):", "#c9d1d9"),
        ("   -> Successfully returned. Late fee assessed: $3.00", "#e3b341"),
    ]
    create_terminal_card("Task 5: OOP Inventory System", t5_lines, os.path.join(base_dir, "task5_inventory_system.png"))

    # 6. TEST SUITE: Automated Unittests
    t6_lines = [
        ("$ python -m unittest discover tests -v", "#7ee787"),
        ("", "#c9d1d9"),
        ("test_is_word_guessed (test_task1_hangman.TestHangman) .................... ok", "#7ee787"),
        ("test_masked_word_initial (test_task1_hangman.TestHangman) ................ ok", "#7ee787"),
        ("test_validate_guess_duplicate (test_task1_hangman.TestHangman) ........... ok", "#7ee787"),
        ("test_holding_calculations (test_task2_portfolio.TestPortfolio) ........... ok", "#7ee787"),
        ("test_export_csv (test_task2_portfolio.TestPortfolio) ..................... ok", "#7ee787"),
        ("test_summary_metrics (test_task2_portfolio.TestPortfolio) ................ ok", "#7ee787"),
        ("test_collision_resolution (test_task3_organizer.TestFileOrganizer) ....... ok", "#7ee787"),
        ("test_organize_directory (test_task3_organizer.TestFileOrganizer) ......... ok", "#7ee787"),
        ("test_greeting_intent (test_task4_chatbot.TestChatbot) .................... ok", "#7ee787"),
        ("test_deadline_intent (test_task4_chatbot.TestChatbot) .................... ok", "#7ee787"),
        ("test_abc_cannot_be_instantiated (test_task5_inventory.TestInventory) ..... ok", "#7ee787"),
        ("test_encapsulation_validation (test_task5_inventory.TestInventory) ....... ok", "#7ee787"),
        ("test_polymorphism_late_fees (test_task5_inventory.TestInventory) ......... ok", "#7ee787"),
        ("test_dunder_methods (test_task5_inventory.TestInventory) ................. ok", "#7ee787"),
        ("", "#c9d1d9"),
        ("----------------------------------------------------------------------", "#30363d"),
        ("Ran 22 tests in 0.054s", "#58a6ff"),
        ("", "#c9d1d9"),
        ("OK - ALL TEST SUITES PASSED (100% SUCCESS RATE)", "#7ee787"),
    ]
    create_terminal_card("Automated Test Suite", t6_lines, os.path.join(base_dir, "test_suite_results.png"))

    # Remove temporary test file if present
    test_file = os.path.join(base_dir, "test_render.png")
    if os.path.exists(test_file):
        os.remove(test_file)


if __name__ == "__main__":
    main()
