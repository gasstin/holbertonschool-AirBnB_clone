#!/usr/bin/python3
"""
    file_storage Module
"""
from json import dumps, loads
from os.path import exists



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
        FileStorage.__objects['{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dic_aux = {}
        for key, value in self.__objects.items():
            dic_aux[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            json_file.write(dumps(dic_aux))
        
        # with open(self.__file_path, "w", encoding="utf-8") as json_file:
        #     json_file.write(dumps(self.__objects))


    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                self.__objects.update(loads(json_file.read()))