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
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f" 
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, time_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the objects
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute'
        updated_at with the current datetime
        """
        models.storage.save()
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        return a dictionary containing all keys/value
        of __dict__ instance
        """
        if isinstance(self.created_at, datetime):
            self.created_at = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            self.updated_at = self.updated_at.isoformat()
        d_instances = self.__dict__
        d_instances["__class__"] = self.__class__.__name__
        return d_instances
