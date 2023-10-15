#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class to inherit from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method
        """
        super().__init__(*args, **kwargs)
