#!/usr/bin/python3
"""That is my review module"""
import models
from .base_model import BaseModel

class Review(BaseModel):
    """Here is the review class"""
    text = ""
    place_id = ""
    user_id = ""
    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)