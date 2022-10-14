#!/usr/bin/python3
import unittest
from models.state import State


class TestBaseModel(unittest.TestCase):
    
    def test_state(self):
        state = State()
        self.assertEqual(type(state.name), str)