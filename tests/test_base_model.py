#!/usr/bin/python3
""" Testing the Base Model as it
    is meant to work"""
from datetime import datetime
import inspect
import time
import unittest
from unittest import mock
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))



class TestBaseModel(unittest.TestCase):
    """Test the basemodel class"""

    def test_init(self):
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "John"
        inst.num = 99
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        self.assertEqual(inst.name, "John")


        def test_save(self, mock_storage):
            """Test for save and updates methods"""

            inst = BaseModel()
            old_created_at = inst.created_at
            old_updated_at = inst.updated_at
            inst.save()
            Ncreate = inst.created_at
            Nupdate = inst.update_at
            self.assertNotEqual(old_updated_at, Nupdate)
            self.assertNotEqual(old_created_at, Ncreate)
       