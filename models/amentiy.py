#!/usr/bin/python3
"""That is my amenity module"""
import models
from .base_model import BaseModel


class Amenity(BaseModel):
    """Here is the amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)
