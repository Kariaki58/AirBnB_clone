#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that will inherit BaseModel
    """
    def __init__(self, *args, **kwargs):
        """inherets all from BaseModel"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
