#!/usr/bin/python3
"""init method for the models dir"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
