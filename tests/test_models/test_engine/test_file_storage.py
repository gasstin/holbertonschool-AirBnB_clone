#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_storage_new(self):
        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)
        prin = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertEqual(storage.all()[prin], my_model)

    def test_file_storage_all(self):
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_file_storage_save(self):
        storage = FileStorage()
        storage.all().clear()
        my_model = BaseModel()
        storage.save()
        self.assertNotEqual(len(storage.all()), 0)

    def test_file_storage_reload(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertNotEqual(len(storage.all()), 0)
