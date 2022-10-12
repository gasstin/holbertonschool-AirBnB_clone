#!/usr/bin/python3
"""
    Write a class City that inherits from BaseModel:
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Create a city

        name: string
        state_id: string
    """
    name = ""
    state_id = ""
