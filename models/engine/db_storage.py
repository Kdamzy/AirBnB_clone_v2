#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv

from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """query on the current database session"""

        session = scoped_session(sessionmaker(bind=self.__engine))
        classes = [State, City, User, Place, Review]
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            return session.query(cls).all()
        else:
            objs = []
            for c in classes:
                objs += session.query(c).all()
            return objs