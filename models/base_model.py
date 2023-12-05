#!/usr/bin/python3
"""That is my BaseModel module"""
import json
from datetime import datetime
import uuid
from __init__ import storage

class BaseModel:
    """Here is my BaseModel class from which everything will be inherited"""
    def __init__(self, *args, **kwargs):
        """My init method for the base class
        
        args: The arguments passed to the function in a tuple form
        kwargs: The arguments passed to the function in a key, value pair
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    theValue = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, theValue)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    def __str__(self):
        """My str method that will print some info about my class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Just a method now and it updates one attribute"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        myReturnedDic = {}
        for key, value in  self.__dict__.items():
            if key == 'updated_at' or key == 'created_at':
                myReturnedDic[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                myReturnedDic[key] = value
        myReturnedDic["__class__"] = self.__class__.__name__
        return myReturnedDic
