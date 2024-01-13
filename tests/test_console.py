#!/usr/bin/python3
"""The console.py unittests.

Unittets classes:
     TestHBNBCommand_prompting
     TestHBNBCommand_help
     TestHBNBCommand_exit
     TestHBNBCommand_create
     TestHBNBCommand_show
     TestHBNBCommand_all
     TestHBNBCommand_destroy
     TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """The prompting unittests"""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """The help unittests"""

    def test_help_quit(self):
        c = "Quit command to exit the program."
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(c, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
