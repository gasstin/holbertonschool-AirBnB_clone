#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State


class TestBaseModel(unittest.TestCase):
    
    def test_state(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))