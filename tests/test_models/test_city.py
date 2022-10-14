#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestBaseModel(unittest.TestCase):
    
    def test_city(self):
        city = City()
        self.assertTrue(type(city.name), str)
    
