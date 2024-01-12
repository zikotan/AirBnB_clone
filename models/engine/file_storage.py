#!/usr/bin/python3
"""The FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """the abstacted storage engine

    Attributes:
    __file_pat (str): arg1
    __objects (dict): arg2
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """obj with key"""
        myName = obj.__class__.name__
        FileStorage.__objects["{}.{}".format(myName, obj.id)] = obj

    def save(self):
        """serialize"""
        myDict = FileStorage.__objects
        myObjdict = {obj: myDict[obj].to_dict() for obj in myDict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(myObjdict, f)

    def reload(self):
        """deserialize"""
        try:
            with open(FileStorage.__file_path) as f:
                myObjdict = json.load(f)
                for o in myObjdict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return
