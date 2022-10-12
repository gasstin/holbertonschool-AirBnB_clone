#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    
    def test_new(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
    
    def test_all(self):
        storage = FileStorage()
        storage.all()
        
    def test_reload(self):
        storage = FileStorage()
        storage.reload()        
        
    # def test_save_storage(self):
    #     storage = FileStorage()
    #     storage.save(self)