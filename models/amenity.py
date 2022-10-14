#!/usr/bin/python3
"""
    Write a class Amenity that inherits from BaseModel:
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Create a amenity

        name: string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
