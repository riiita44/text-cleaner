import unittest
import subprocess
import sys


class TestTextCleaner(unittest.TestCase):

    def test_basic_cleaning(self):
        """行末の空白と連続する空行を整理する"""
        result = subprocess.run(
            [sys.executable, "text_cleaner.py"],
            input="Hello   \n\n\nPython   \n",
            text=True,
            capture_output=True
        )
        self.assertEqual(result.stdout, "Hello\n\nPython\n")

    def test_remove_duplicates(self):
        """重複した行を削除する"""
        result = subprocess.run(
            [sys.executable, "text_cleaner.py", "-r"],
            input="Apple\nBanana\nApple\n",
            text=True,
            capture_output=True
        )
        self.assertEqual(result.stdout, "Apple\nBanana\n")

    def test_remove_empty(self):
        """空行をすべて削除する"""
        result = subprocess.run(
            [sys.executable, "text_cleaner.py", "-e"],
            input="Apple\n\nBanana\n",
            text=True,
            capture_output=True
        )
        self.assertEqual(result.stdout, "Apple\nBanana\n")

    def test_help(self):
        """ヘルプを表示する"""
        result = subprocess.run(
            [sys.executable, "text_cleaner.py", "-h"],
            text=True,
            capture_output=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout)


if __name__ == "__main__":
    unittest.main()
