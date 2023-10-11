#!/usr/bin/python3
"""models to import"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    class  that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        method sets in __objects the obj with key <obj class name>.id
        """
        key = f"{__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        function to serializes __objects to the JSON file
        """
        class_dict = FileStorage.__objects
        dict_o = {obj: class_dict[obj].to_dict() for obj in class_dict.keys()}
        with open(FileStorage.__file_path, "w") as q:
            json.dump(dict_o, q)

    def reload(self):
        """
        function to ddeserializ the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path) as q:
                dict_o = json.load(q)
                for i in dict_o.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i)
        except FileNotFoundError:
            pass
