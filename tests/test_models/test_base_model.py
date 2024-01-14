#!/usr/bin/python3
"""The base_model.py unittests
Unittest classes:
    TestBaseModel_instance
    TestBaseModel_save
    TestBaseModel_to_dict
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


class TestBaseModel_save(unittest.TestCase):
    """The save method unittests"""

    def test_save_with_arg(self):
        c = BaseModel()
        with self.assertRaises(TypeError):
            c.save(None)

    def test_save_update_file(self):
        c = BaseModel()
        c.save()
        cId = "BaseModel." + c.id
        with open("file.json", "r") as f:
            self.assertIn(cId, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """The save method unittests"""

    def test_to_dict_date_attr_str(self):
        c = BaseModel()
        c_dict = c.to_dict()
        self.assertEqual(str, type(c_dict["created_at"]))
        self.assertEqual(str, type(c_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
