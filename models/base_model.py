#!/usr/bin/python3
"""modules to  import"""
import models
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """
    class that will define all commont/
    attributes/methods for other classe
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer for the new model

        Args:
        args: any
        kwargs : to be used
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f" 
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the objects
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute'
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary containing all keys/value
        of __dict__ instance
        """
        d_instances = self.__dict__
        if isinstance(self.created_at, datetime):
            d_instances["created_at"] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            d_instances["updated_at"] = self.updated_at.isoformat()
        d_instances["__class__"] = self.__class__.__name__
        return d_instances
