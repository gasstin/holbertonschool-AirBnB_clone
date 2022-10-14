#!/usr/bin/python3
import unittest
from models.user import User


class TestBaseModel(unittest.TestCase):
    
    def test_user_first_name(self):
        user = User()
        # user.first_name = "Francisco"
        self.assertEqual(type(user.first_name), str)
    
    
    def test_user_last_name(self):
        user = User()
        # user.last_name = "Suarez"
        self.assertEqual(type(user.last_name), str)
        
    
    def test_user_first_email(self):
        user = User()
        user.email = "FranciscoSuarez@holberton.com"
        self.assertEqual(user.email, "FranciscoSuarez@holberton.com")
    
    def test_user_first_email(self):
        user = User()
        user.password = "contraseña"
        self.assertEqual(user.password, "contraseña")
    
