#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestBaseModel_Amenity(unittest.TestCase):
    
    def test_amenity_name(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)    
