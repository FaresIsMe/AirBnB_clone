#!/usr/bin/python3
"""That is my User module"""
import models
from .base_model import BaseModel


class User(BaseModel):
    """Here is the class of my user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)
