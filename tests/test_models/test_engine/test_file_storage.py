#!/usr/bin/python3
"""The file_storage.py unittests

Unittest classes:
    TestBaseModel_methods
    TestBaseModel_instances
"""

import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestBaseModel_methods(unittest.TestCase):
    """The file_storage.py methods unittests"""
   
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

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
        u = User()
        models.storage.new(u)
        models.storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + b.id, text)
            self.assertIn("User." + u.id, text)

    def test_reload(self):
        b = BaseModel()
        models.storage.new(b)
        u = User()
        models.storage.new(u)
        o = FileStorage._FileStorage__objects    
        self.assertIn("BaseModel." + b.id, o)
        self.assertIn("User." + u.id, o)


if __name__ == "__main__":
    unittest.main()
