#!/usr/bin/python3
import unittest
from models.review import Review


class TestBaseModel(unittest.TestCase):
    
    def test_review_text(self):
        review = Review()
        self.assertEqual(type(review.text), str)
