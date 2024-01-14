#!/usr/bin/python3
"""The file_storage.py unittests

Unittest classes:
    TestBaseModel_methods
"""

import models
import unittest
from datetime import datetime 
from models.base_model import BaseModel


class TestBaseModel_methods(unittest.TestCase):
    """The save method unittests"""

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_to_dict_date_attr_str(self):
        c = BaseModel()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
