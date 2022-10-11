#!/usr/bin/python3
"""
    file_storage Module
"""
# from types import SimpleNamespace
from json import load, dump
from os.path import exists
# from models.base_model import BaseModel



class FileStorage:
    """
        Write a class FileStorage that serializes instances
        to a JSON file and deserializes JSON file to instances 
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        key_aux = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key_aux] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dic_aux = {}
        for key, value in self.all().items():
            dic_aux[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            dump(dic_aux, json_file)
        
    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                data = load(json_file)
            for val in data.values():
                from models.base_model import BaseModel
                self.new(BaseModel(**val))
            