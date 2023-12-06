#!/usr/bin/python3
"""That is my State module"""
import models
from .base_model import BaseModel

class State(BaseModel):
    """Here is the state class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)
