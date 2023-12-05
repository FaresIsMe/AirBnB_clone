#!/usr/bin/python3
"""My file storage class to deal with json things"""
import json

class FileStorge:
    __file_path = 'myFile.json'
    __objects = {}
    def all(self):
        """A method to return a dict"""
        return self.__objects
    def new(self, obj):
        """A method to put in the objects ids in the dict"""
        self.__objects[obj.id] = obj.to_dict()
    def save(self):
        """A method to save the objects in file but first it converts
        the object to json"""
        print(self.__objects)
        with open(f"{self.__file_path}", "w", encoding='utf-8') as myFileReal:
            myJsonDic = json.dumps(self.__objects)
            myFileReal.write(myJsonDic)
    def reload(self):
        """"A method to get the json object from a file to convert
        it back to a dict"""
        try:
            with open(f"{self.__file_path}", "r", encoding='utf-8') as myFileReal:
                myJsonObject = json.load(myFileReal)
        except (FileNotFoundError, json.JSONDecodeError) as hi:
            pass