#!/usr/bin/python3
"""The file_storage.py unittests

Unittest classes:
    TestBaseModel_methods
"""

import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestBaseModel_methods(unittest.TestCase):
    """The file_storage.py methods unittests"""
    
    def test_new(self):
        b = BaseModel()
        models.storage.new(b)
        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn(b, models.storage.all().values())
        u = User()
        models.storage.new(u)
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())

    def test_save(self):
        b = BaseModel()
        models.storage.new(b)
        models.storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + b.id, text)

    def test_reload(self):
        b = BaseModel()
        models.storage.new(b)
        o = FileStorage._FileStorage__objects    
        self.assertIn("BaseModel." + b.id, o)


if __name__ == "__main__":
    unittest.main()
