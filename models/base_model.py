#!/usr/bin/python3
"""
basemodel class to be contained
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """a class that is called basemodel"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """BaseModel Initialization"""
        if kwargs:
            for moftah, value in kwargs.items():
                if moftah != "__class__":
                    setattr(self, moftah, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """BaseModel class string representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """current datetime update attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """the instances kay/value attributes to be returned"""
        n_d = self.__dict__.copy()
        if "created_at" in n_d:
            n_d["created_at"] = n_d["created_at"].strftime(time)
        if "updated_at" in n_d:
            n_d["updated_at"] = n_d["updated_at"].strftime(time)
        n_d["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in n_d:
            del n_d["_sa_instance_state"]
        return n_d

    def delete(self):
        """the current instance from the storage to be deleted"""
        models.storage.delete(self)
