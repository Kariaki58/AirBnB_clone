#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Review class that inherits BaseModel
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
