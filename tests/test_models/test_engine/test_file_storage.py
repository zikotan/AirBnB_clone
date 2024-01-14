#!/usr/bin/python3
"""The file_storage.py unittests

Unittest classes:
    TestBaseModel_methods
"""

import models
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel_methods(unittest.TestCase):
    """The file_storage.py methods unittests"""
    
    def test_new(self):
        b = BaseModel()
        models.storage.new(b)
        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn(b, models.storage.all().values())

    


if __name__ == "__main__":
    unittest.main()
