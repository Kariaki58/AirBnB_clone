#!/usr/bin/python3
"""Modules to import"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that will inherit BaseModel
    """
    state_id = ""
    name = ""
