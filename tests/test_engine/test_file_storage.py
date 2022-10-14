#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    
    def test_file_storage_new(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        self.assertTrue(storage.all()[f"{my_model.__class__.__name__}.{my_model.id}"], my_model)
    
    def test_file_storage_all(self):
        storage = FileStorage()
        self.assertTrue(type(storage.all()), dict)
        

    def test_file_storage_save(self):
        _file_path = "file.json"
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        my_model.save()
        from os.path import exists
        self.assertTrue(exists, _file_path)
    
    def test_file_storage_reload(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        storage.save()
        storage.all().clear()
        storage.reload()
        self.assertNotEqual(len(storage.all()), 0)
        
        
    # def test_save_storage(self):
    #     storage = FileStorage()
    #     storage.save(self)