#!/usr/bin/python3
"""
    file_storage Module
"""
from json import load, dump
from os.path import exists


class FileStorage:
    """
        Write a class FileStorage that serializes instances
        to a JSON file and deserializes JSON file to instances
    """

    __file_path = 'file.json'  # path to the JSON file
    __objects = {}  # empty dict but will store all objects by <class name>.id

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dic_aux = {}
        for key, value in self.all().items():
            dic_aux[key] = value.to_dict()
            # open the json file and serializes dic_aux using json.dump
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            dump(dic_aux, json_file)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        self.__objects.clear()
        if exists(self.__file_path):  # check if the file exists
            with open(self.__file_path, "r") as json_file:  # open the file
                # use json.load to convert in a dictionary and deserialize file
                data = load(json_file)
            for val in data.values():
                # import here, to avoid circular import
                from models.base_model import BaseModel
                from models.user import User
                from models.city import City
                from models.state import State
                from models.review import Review
                from models.amenity import Amenity
                from models.place import Place
                # dictionary with all possible classes
                dict_class = {'BaseModel': BaseModel,
                              'User': User, 'City': City,
                              'State': State, 'Review': Review,
                              'Amenity': Amenity, 'Place': Place}
                # pass to new method all additional named arguments
                self.new(dict_class[val['__class__']](**val))
        return 0
