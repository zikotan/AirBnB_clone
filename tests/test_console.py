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

    def test_help(self):
        c = ("Documented commands (type help <topic>):\n"
        "========================================\n"
        "EOF  all  count  create  destroy  help  quit  show  update")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(c, f.getvalue().strip())

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


class TestHBNBCommand_exit(unittest.TestCase):
    """The exiting unittests"""

    def test_qui_exits(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """The create unittests"""

    @classmethod
    def setUP(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        c = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(c, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
