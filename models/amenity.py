#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that will inherit BaseModel
    from the base model file
    """
    def __init__(self, *args, **kwargs):
        """inheretes from BaseModel"""
        super().__init__(*args, **kwargs)
        self.name = ""
