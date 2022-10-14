#!/usr/bin/python3
import unittest
from models.place import Place


class TestBaseModel_Place(unittest.TestCase):
    
    def test_place_name(self):
        place = Place()
        self.assertEqual(type(place.name), str)
    
