#!/usr/bin/python3
"""My file storage class to deal with json things"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amentiy import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """A method to return a dict"""
        return self.__objects

    def new(self, obj):
        """A method to put in the objects ids in the dict"""
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """A method to save the objects in file but first it converts
        the object to json"""
        myJsonObjectInDic = {}
        for key, value in self.__objects.items():
            myJsonObjectInDic[key] = self.__objects[key].to_dict()
        with open(f"{self.__file_path}", "w", encoding='utf-8') as myFileReal:
            json.dump(myJsonObjectInDic, myFileReal)

    def reload(self):
        """"A method to get the json object from a file to
        convert it back to a dict"""
        try:
            with open(f"{self.__file_path}", "r", encoding='utf-8') as myReal:
                for key, value in json.load(myReal).items():
                    theDicOfObj = eval(value["__class__"])(**value)
                    self.__objects[key] = theDicOfObj
        except (FileNotFoundError, json.JSONDecodeError) as hi:
            pass
