#!/usr/bin/python3
"""The BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initialisation

        Args:
            *args: arg1
            **kwargs: arg2
        """
        myFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, myFormat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

        def save(self):
            """update"""
            self.updated_at = datetime.today()
            models.storage.save()

        def to_dict(self):
            """the dic of the instance
            """
            myDict = self.__dict__copy()
            myDict["created_at"] = self.created_at.isoformat()
            myDict["updated_at"] = self.updated_at.isoformat()
            myDict["__class__"] = self.__class__.__name__
            return myDict

        def __str__(self):
            """representation of the instance
            """
            myName = self.__class__.__name__
            return "[{}] ({}) {}".format(myName, self.id, self.__dict__)
