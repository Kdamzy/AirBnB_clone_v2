#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
import os

from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None
    
    def __init__(self):
        """Create the engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        dbase = os.getenv('HBNB_MYSQL_DB')
        dbase_url = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                user, password, host, dbase
        )
        self.__engine = create_engine(
            dbase_url,
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """query on the current database session"""

        session = scopes_session(sessionmaker(bind=self.__engine))
        objs = dict()
        all_object = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for object_type in all_object:
                query = self.session.query(object_type)
                for obj in query.all():
                    key + f"{object.__class__.__name__} . {obj.id}"
                    objs[key] = obj
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            return session.query(cls).all()
        else:
            objs = []
            for c in classes:
                objs += session.query(c).all()
            return objs