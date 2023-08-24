#!/usr/bin/python3
"""the FileStorage class to be defined"""
import json


class FileStorage:
    """
    an abstracted storage engine to be created
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        a dictionary of instantiated objects
        to be returned
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            c_d = {}
            for c, b in self.__objects.items():
                if type(b) == cls:
                    c_d[c] = b
            return c_d
        return self.__objects

    def new(self, obj):
        """in objects to be set"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """seriealize objects to go to the json file"""
        odict = {a: self.__objects[a].to_dict() for a in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """objects of a json file to be deserialized to be objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for a in json.load(f).values():
                    name = a["__class__"]
                    del a["__class__"]
                    self.new(eval(name)(**a))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """a given objects to be deleted from json file"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """the reload method to be called"""
        self.reload()
