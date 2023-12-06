#!/usr/bin/python3
"""That is my place module"""
import models
from .base_model import BaseModel

class Place(BaseModel):
    """Here is the place class"""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amentiy_ids = []
    def __init__(self, *args, **kwargs):
        """The init function of my user that inheritest from """
        super().__init__(*args, **kwargs)
