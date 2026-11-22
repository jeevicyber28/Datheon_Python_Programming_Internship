import unittest
import os
import sys
import tempfile
import shutil
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task3_file_organizer.organizer import organize_directory, get_unique_destination


class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_collision_resolution(self):
        dest_dir = Path(self.test_dir)
        file1 = dest_dir / "report.pdf"
        file1.write_text("sample content")

        unique_path = get_unique_destination(dest_dir, "report.pdf")
        self.assertEqual(unique_path.name, "report_1.pdf")

    def test_organize_directory(self):
        # Create sample files
        p = Path(self.test_dir)
        (p / "doc1.pdf").write_text("pdf")
        (p / "pic1.jpg").write_text("jpg")
        (p / "script1.py").write_text("code")

        summary = organize_directory(self.test_dir, dry_run=False)
        self.assertEqual(summary["total"], 3)
        self.assertTrue((p / "Documents" / "doc1.pdf").exists())
        self.assertTrue((p / "Images" / "pic1.jpg").exists())
        self.assertTrue((p / "Code" / "script1.py").exists())


if __name__ == "__main__":
    unittest.main()
