#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
