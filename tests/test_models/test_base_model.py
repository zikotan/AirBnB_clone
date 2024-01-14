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


if __name__ == "__main__":
    unittest.main()
