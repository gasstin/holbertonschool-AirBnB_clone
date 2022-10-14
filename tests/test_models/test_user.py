#!/usr/bin/python3
import unittest
from models.user import User


class TestBaseModel(unittest.TestCase):
    
    def test_user_first_name(self):
        user = User()
        self.assertEqual(type(user.first_name), str)
    
    def test_user_last_name(self):
        user = User()
        self.assertEqual(type(user.last_name), str)
    
    def test_user_email(self):
        user = User()
        self.assertTrue(type(user.email), str)
    
    def test_user_password(self):
        user = User()
        self.assertTrue(type(user.password), str)
    
