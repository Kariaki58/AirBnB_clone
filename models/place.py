#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class to inherit the Basel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitutde = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """inheretes from BaseModel"""
        super().__init__(*args, **kwargs)
