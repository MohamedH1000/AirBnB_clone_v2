#!/usr/bin/python3
"""This module instantiates storage object
@TODOS:
    checks HBNB_TYPE_STORAGE environmental variable to determine storage type
"""
from os import getenv
from .user import User
from .city import City
from .place import Place
from .state import State
from .review import Review
from .amenity import Amenity
import pymysql

pymysql.install_as_MySQLdb()
"""install mysqlbd to execute data from database"""

if getenv('HBNB_TYPE_STORAGE') == 'db':
    """module for mysql to import data from"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    """function for storing data"""
else:
    """this is file for storing data in python"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    """import data from this filestorage file"""
storage.reload()
"""to reload data from this function"""
