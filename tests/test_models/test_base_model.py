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
        my_model.created_at = '2022-10-11'
        self.assertEqual(str(my_model.created_at), '2022-10-11')
    
    def test_update(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.save()
        self.assertNotEqual(str, type(my_model.updated_at))
        
    def test_str(self):
        my_model = BaseModel()
        my_model.id = 20
        self.assertEqual(str(my_model.id), "20")
    
    def test_to_dict(self):
        my_model = BaseModel()
        aux_dic = my_model.to_dict()
        self.assertTrue(type(aux_dic), dict)