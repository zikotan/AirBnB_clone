#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
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


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        c = "Quit command to exit the program."
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_create(self):
        c = ("Use: create <class>\n        "
        "Create a new class instance and print its id.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        c = ("Use: show <class> <id> or <class>.show(<id>)\n        "
        "Shows the representation of a class instance of an id given.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_destroy(self):
        c = ("Use: destroy <class> <id> or <class>.destroy(<id>)\n        "
        "Delete a class instance of an id given.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_all(self):
        c = ("Use: all <class> or all <class> or <class>.all()\n        "
        "Shows the representation of a class instance of an id given.\n        "
        "Or all classes if no class given")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_count(self):
        c = ("Use: count <class> or <class>.count()\n        "
        "Pritns the number of instances of the given class.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(c, f.getvalue().strip())

    def test_help_update(self):
        c = ("Use: update <class> <id> <attribute_name> <attribute_value>\n        "
        "or <class>.update(<id>, <attribute_name>, <attribute_value>)\n        "
        "or <class>.update(<id>, <dictionary>)\n        "
        "Updates a class instance of an id given.")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(c, f.getvalue().strip())

    




if __name__ == "__main__":
    unittest.main()
