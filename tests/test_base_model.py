#!/usr/bin/python3
""" Testing the Base Model as it
    is meant to work"""
from datetime import datetime
import inspect
import time
import unittest
from unittest import mock


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
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(attr, inst.__dict__[attr]), typ)
        self.assertEqual(inst.name, "john")
        self.assertEqual(inst.number, 99)

    @mock.patch('models.storage')
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
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)