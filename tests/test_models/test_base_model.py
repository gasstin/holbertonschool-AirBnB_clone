#!/usr/bin/python3
import datetime
import imp
import unittest
import io
import contextlib
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    
    def test_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.save()
        
    def test_created(self):
        my_model = BaseModel()
        self.assertTrue(type(my_model.created_at), datetime)
    
    def test_update(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.save()
        self.assertNotEqual(str, type(my_model.updated_at))
        
    def test_str(self):
        my_model = BaseModel()
        my_model.id = 20
        self.assertEqual(str(my_model.id), "20")