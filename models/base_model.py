#!/usr/bin/python3
"""That is my BaseModel module"""
import json
import datetime
import uuid

class BaseModel:
    """Here is my BaseModel class from which everything will be inherited"""
    def __init__(self):
        """My init method for the base class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """My str method that will print some info about my class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Just a method now and it updates one attribute"""
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        myReturnedDic = {}
        for key, value in  self.__dict__.items():
            if key == 'updated_at' or key == 'created_at':
                myReturnedDic[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                myReturnedDic[key] = value
        myReturnedDic["__class__"] = self.__class__.__name__
        return myReturnedDic
