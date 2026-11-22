import argparse
import os
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

EXTENSION_CATEGORIES: Dict[str, str] = {
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".md": "Documents",
    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".webp": "Images",
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    # Archives
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".7z": "Archives",
    ".rar": "Archives",
    # Code
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".cpp": "Code",
    ".java": "Code",
    ".sql": "Code",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio"
}


def get_unique_destination(destination_dir: Path, filename: str) -> Path:
    """
    Collision resolver: If a file already exists at the destination,
    appends an incremented index like 'filename_1.ext' instead of overwriting.
    """
    dest = destination_dir / filename
    if not dest.exists():
        return dest

    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1
    while True:
        candidate = destination_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_directory(target_path: str, dry_run: bool = False) -> Dict[str, int]:
    """
    Scans the directory, maps files by extension to categories,
    creates dynamic subfolders, and safely moves files with collision handling.
    """
    target = Path(target_path).resolve()
    if not target.exists() or not target.is_dir():
        raise ValueError(f"Target path '{target_path}' is not a valid directory.")

    # All known category folder names so we don't accidentally move category folders
    category_folder_names = set(EXTENSION_CATEGORIES.values()) | {"Others"}

    summary: Dict[str, int] = {cat: 0 for cat in category_folder_names}
    errors: List[str] = []
    total_moved = 0

    print("\n" + "=" * 60)
    print(f"  DATHEON AUTOMATED FILE ORGANIZER {'[DRY RUN]' if dry_run else ''}")
    print("=" * 60)
    print(f"Scanning target directory: {target}\n")

    # Use scandir for optimal OS filesystem performance
    with os.scandir(target) as entries:
        for entry in entries:
            # Skip subdirectories and category folders
            if not entry.is_file():
                continue

            file_path = Path(entry.path)
            ext = file_path.suffix.lower()

            # Determine category
            category = EXTENSION_CATEGORIES.get(ext, "Others")
            dest_dir = target / category

            try:
                dest_file = get_unique_destination(dest_dir, file_path.name)
                action_text = f"MOVE: {file_path.name} -> /{category}/{dest_file.name}"

                if not dry_run:
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file_path), str(dest_file))

                print(f" [OK] {action_text}")
                summary[category] += 1
                total_moved += 1

            except PermissionError as pe:
                err_msg = f" [PERMISSION ERROR] Cannot move {file_path.name}: {pe}"
                print(err_msg)
                errors.append(err_msg)
            except Exception as e:
                err_msg = f" [ERROR] Could not relocate {file_path.name}: {e}"
                print(err_msg)
                errors.append(err_msg)

    # Print summary
    print("\n" + "-" * 60)
    print("EXECUTION SUMMARY:")
    for cat, count in sorted(summary.items()):
        if count > 0:
            print(f" - {cat:<15}: {count} files")
    print(f"Total Files Relocated: {total_moved}")
    if errors:
        print(f"Total Errors/Warnings: {len(errors)}")
    print("-" * 60)

    summary["total"] = total_moved
    summary["errors"] = len(errors)
    return summary


def main():
    parser = argparse.ArgumentParser(description="Autonomous Desktop Directory Organizer & Cleanup Utility")
    parser.add_argument(
        "--path",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "test_sandbox"),
        help="Target folder path to organize (default: local test_sandbox)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate file relocation without modifying files"
    )
    args = parser.parse_args()

    organize_directory(args.path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
