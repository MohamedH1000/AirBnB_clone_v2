#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """a json file instances to be serielized and back to instances
     by the deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """objects of the dictionary to be returned"""
        if cls is not None:
            n_d = {}
            for moftah, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    n_d[moftah] = value
            return n_d
        return self.__objects

    def new(self, obj):
        """the object to be set"""
        if obj is not None:
            moftah = obj.__class__.__name__ + "." + obj.id
            self.__objects[moftah] = obj

    def save(self):
        """objects to the json file to be serialized"""
        json_objects = {}
        for moftah in self.__objects:
            json_objects[moftah] = self.__objects[moftah].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """the json file to be serialized to oobjects"""
        try:
            with open(self.__file_path, 'r') as f:
                loa = json.load(f)
            for moftah in loa:
                self.__objects[moftah] = classes[loa[moftah]["__class__"]](**loa[moftah])
        except:
            pass

    def delete(self, obj=None):
        """to delete the objects from the json file"""
        if obj is not None:
            moftah = obj.__class__.__name__ + '.' + obj.id
            if moftah in self.__objects:
                del self.__objects[moftah]

    def close(self):
        """call the reload method"""
        self.reload()
