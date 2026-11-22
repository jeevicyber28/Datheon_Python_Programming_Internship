import os
from pathlib import Path


def generate_sandbox_files(sandbox_path: str = None) -> str:
    """Creates a sandbox folder with dummy files across various extensions to test organization safely."""
    if sandbox_path is None:
        sandbox_path = os.path.join(os.path.dirname(__file__), "test_sandbox")

    p = Path(sandbox_path)
    p.mkdir(parents=True, exist_ok=True)

    dummy_files = [
        ("report_q3.pdf", "Quarterly Report Content"),
        ("resume_2026.docx", "Candidate Profile"),
        ("notes.txt", "Meeting notes and action points"),
        ("financials.xlsx", "Sample Excel Data"),
        ("profile_avatar.png", "PNG image bytes representation"),
        ("banner.jpg", "JPEG banner bytes"),
        ("tutorial_demo.mp4", "Video stream mock"),
        ("backup_files.zip", "Archived zip mock"),
        ("main_server.py", "print('Python Service')"),
        ("app_logic.js", "console.log('JS App');"),
        ("styles.css", "body { margin: 0; }"),
        ("podcast_episode1.mp3", "Audio raw data"),
        ("mystery_data.xyz", "Uncategorized custom file"),
        # Duplicate to test collision handling
        ("notes_duplicate.txt", "Another notes copy")
    ]

    print(f"Generating test sandbox in: {p.resolve()}")
    for fname, content in dummy_files:
        target_file = p / fname
        target_file.write_text(content, encoding="utf-8")
        print(f" + Created: {fname}")

    print("\nSandbox populated successfully. You can now run organizer.py!")
    return str(p.resolve())


if __name__ == "__main__":
    generate_sandbox_files()
