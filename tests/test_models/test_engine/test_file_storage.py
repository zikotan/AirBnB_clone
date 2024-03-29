#!/usr/bin/python3
"""The file_storage.py unittests

Unittest classes:
    TestBaseModel_methods
    TestBaseModel_instances
"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestBaseModel_instances(unittest.TestCase):
    """The file_storage.py instansiation unittests"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        FileStorage._FileStorage__objects = {}

    def test_FS_inst_no_arg(self):
        self.assertEqual(type(FileStorage()), FileStorage)
    
    def test_FS_inst_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FL_path_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FL_obj_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_inistial(self):
        self.assertEqual(type(models.storage), FileStorage)


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
