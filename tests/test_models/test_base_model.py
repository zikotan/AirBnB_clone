#!/usr/bin/python3
"""The base_model.py unittests
Unittest classes:
    TestBaseModel_instance
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep 
from models.base_model import BaseModel

class TestBaseModel_instance(unittest.TestCase):
    """Instansiation unittests"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_inst_in_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_pub_date(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_create_at_pub_date(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_args_unused(self):
        c = BaseModel(None)
        self.assertNotIn(None, c.__dict__.values())


if __name__ == "__main__":
    unittest.main()
