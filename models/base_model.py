#!/usr/bin/python3
"""
    Write a class BaseModel that defines all common
    attributes/methods for other classes:
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            print the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dict_aux = self.__dict__
        dict_aux['__class__'] = self.__class__.__name__
        dict_aux['created_at'] = str(self.created_at.isoformat())
        dict_aux['updated_at'] = str(self.updated_at.isoformat())
        return dict_aux
