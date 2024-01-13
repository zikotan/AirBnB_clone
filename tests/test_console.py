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
    """Prompting unittests"""


if __name__ == "__main__":
    unittest.main()
