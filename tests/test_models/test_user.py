#!/usr/bin/python3
"""The base_model.py unittests

Unittest classes:
    TestBaseModel_save
"""

import unittest
import os
from models.user import User
from datetime import datetime


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

    def test_inst_no_args(self):
        self.assertEqual(type(User()), User)

    def test_inst_with_kwargs(self):
        d = datetime.today()
        d_form = d.isoformat()
        u = User(id="0", created_at=d_form, updated_at=d_form)
        self.assertEqual(u.id,  "0")
        self.assertEqual(u.created_at, d)
        self.assertEqual(u.updated_at, d)


class TestBaseModel_save(unittest.TestCase):
    """The save method unittests"""

    def test_save_update_file(self):
        u = User()
        u.save()
        uId = "User." + u.id
        with open("file.json", "r") as f:
            self.assertIn(uId, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """The save method unittests"""

    def test_to_dict_date_attr_str(self):
        u = User()
        u_dict = u.to_dict()
        self.assertEqual(str, type(u_dict["id"]))
        self.assertEqual(str, type(u_dict["created_at"]))
        self.assertEqual(str, type(u_dict["updated_at"]))

if __name__ == "__main__":
    unittest.main()
