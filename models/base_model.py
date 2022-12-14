#!/usr/bin/python3
"""
    Write a class BaseModel that defines all common
    attributes/methods for other classes:
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
        defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
            creates a new instance
        """
        if kwargs:  # if arguments were passed
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "name":
                    self.name = value
                if key == "my_number":
                    self.my_number = value
                if key == "created_at":
                    # creates a datetime object from the given string
                    self.created_at = \
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    # creates a datetime object from the given string
                    self.updated_at = \
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())  # Generate a random UUID
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # call new method from storage

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
        storage.save()  # call save method from storage

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        # save a copy of self.__dict__ because we don't wanna modify
        dict_aux = self.__dict__.copy()
        dict_aux['__class__'] = self.__class__.__name__
        # isoformat return a string with the next format: Date, Time, UTC
        dict_aux['created_at'] = self.created_at.isoformat()
        dict_aux['updated_at'] = self.updated_at.isoformat()
        return dict_aux
