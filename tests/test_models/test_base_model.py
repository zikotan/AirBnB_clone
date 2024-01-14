#!/usr/bin/python3
"""The base_model.py unittests
Unittest classes:
    TestBaseModel_instance
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import models
import unittest
from datetime import datetime 
from models.base_model import BaseModel


class TestBaseModel_to_dict(unittest.TestCase):
    """The save method unittests"""

    def test_to_dict_date_attr_str(self):
        c = BaseModel()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
