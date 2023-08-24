#!/usr/bin/python3
"""the DBStorage engine to be defined"""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
    a database storage engine to be represented
    """

    __engine = None
    __session = None

    def __init__(self):
        """a new DBStorage instance to be initialized"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        on the current database to be queried
        """
        if cls is None:
            aims = self.__session.query(State).all()
            aims.extend(self.__session.query(City).all())
            aims.extend(self.__session.query(User).all())
            aims.extend(self.__session.query(Place).all())
            aims.extend(self.__session.query(Review).all())
            aims.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            aims = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in aims}

    def new(self, obj):
        """to the current database session an object
        to be added"""
        self.__session.add(obj)

    def save(self):
        """to the current database session all session
        to be commited"""
        self.__session.commit()

    def delete(self, obj=None):
        """from current databse session an
        object to be deleted"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """initialize a new session and create the new table"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """the working sqlachemy session to be deleted"""
        self.__session.close()
