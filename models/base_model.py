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


# Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

# Now it’s time to re-create an instance with this dictionary representation.

# <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
# Update models/base_model.py:

# __init__(self, *args, **kwargs):
# you will use *args, **kwargs arguments for the constructor of a BaseModel. 
# (more information inside the AirBnB clone concept page)
# *args won’t be used
# if kwargs is not empty:
# each key of this dictionary is an attribute name (Note __class__ from kwargs is 
# the only one that should not be added as an attribute. See the example output, below)
# each value of this dictionary is the value of this attribute name
# Warning: created_at and updated_at are strings in this dictionary, 
# but inside your BaseModel instance is working with datetime object. 
# You have to convert these strings into datetime object. Tip: you know the string format of these datetime
# otherwise:
# create id and created_at as you did previously (new instance)