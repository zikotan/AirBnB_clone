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

    def test_help_EOF(self):
        c = "EOF signal to exit."
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_create(self):
        c = ("Use: create <class>\n        "
        "Create a new class instance and print its id.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(c, f.getvalue().strip())
    
    def test_help_show(self):
        c = ("Use: show <class> <id> or <class>.show(<id>)\n        "
        "Shows the representation of a class instance of an id given.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(c, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
