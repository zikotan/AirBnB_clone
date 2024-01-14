#!/usr/bin/python3
"""The base_model.py unittests

Unittest classes:
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import models
import unittest
from datetime import datetime 
from models.base_model import BaseModel


class TestBaseModel_save(unittest.TestCase):
    """The save method unittests"""
    
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

    def test_save_update_file(self):
        u = User()
        u.save()
        uId = "User." + u.id
        with open("file.json", "r") as f:
            self.assertIn(uId, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """The to_dict method unittests"""
    
    def test_to_dict_date_attr_str(self):
        c = BaseModel()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
