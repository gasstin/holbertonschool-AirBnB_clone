#!/usr/bin/python3
import datetime
import imp
import unittest
import io
import contextlib
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    
    # def test_save(self):
    #     my_model = BaseModel({'id': '25d98908-41b9-4b8c-9129-2f5ed6ed4c7e', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), '__class__': 'BaseModel'})
    #     my_model.save()
        
    def test_created(self):
        my_model = BaseModel()
        my_model.created_at = '2022-10-11'
        self.assertEqual(str(my_model.created_at), '2022-10-11')
    
    def test_update(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        storage = FileStorage()
        storage.reload()
        self.assertNotEqual(str, my_model.updated_at)
        
    def test_id(self):
        my_model = BaseModel()
        my_model.id = 20
        self.assertEqual(str(my_model.id), "20")
        
    def test_str(self):
        my_model = BaseModel()
        self.assertEqual(print(my_model), None)
    
    def test_to_dict(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.to_dict()), dict)