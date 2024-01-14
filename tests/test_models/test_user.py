#!/usr/bin/python3
"""The base_model.py unittests

Unittest classes:
    TestBaseModel_save
"""

import unittest
import os
from models.user import User

class TestBaseModel_save(unittest.TestCase):
    """The save method unittests"""

    def test_save_update_file(self):
        u = User()
        u.save()
        uId = "User." + u.id
        with open("file.json", "r") as f:
            self.assertIn(uId, f.read())


if __name__ == "__main__":
    unittest.main()
