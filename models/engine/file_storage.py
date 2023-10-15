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
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        function to serializes __objects to the JSON file
        """
        temp_dict = {}
        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF8") as file:
            json.dump(temp_dict, file)

    def reload(self):
        """
        function to ddeserializ the JSON fie to __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as file:
                dict_o = json.load(file)
            for key, value in dict_o.items():
                obj_class = value["__class__"]
                if obj_class == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                if obj_class == "User":
                    self.__objects[key] = User(**value)
                if obj_class == "Amenity":
                    self.__objects[key] = Amenity(**value)
                if obj_class == "City":
                    self.__objects[key] = City(**value)
                if obj_class == "State":
                    self.__objects[key] = State(**value)
                if obj_class == "Place":
                    self.__objects[key] = Place(**value)
                if obj_class == "Review":
                    self.__objects[key] = Review(**value)
        except Exception:
            pass
