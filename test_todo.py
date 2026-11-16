import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TODO = Path(__file__).resolve().with_name("todo.py")


class TodoTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.cwd = tmp.name

    def run_todo(self, *args):
        result = subprocess.run(
            [sys.executable, str(TODO), *args],
            cwd=self.cwd,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def test_add_then_list(self):
        # given
        self.run_todo("add", "Buy", "milk")
        self.run_todo("add", "Write", "tests")

        # when
        lines = self.run_todo("list").splitlines()

        # then
        self.assertEqual(len(lines), 2)
        self.assertIn("Buy milk", lines[0])
        self.assertIn("Write tests", lines[1])

    def test_list_without_file_prints_nothing(self):
        # when / then
        self.assertEqual(self.run_todo("list"), "")
