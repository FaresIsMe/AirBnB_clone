#!/usr/bin/python3
"""That is my City module"""
import models
from .base_model import BaseModel


class City(BaseModel):
    """Here is the city class"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)
