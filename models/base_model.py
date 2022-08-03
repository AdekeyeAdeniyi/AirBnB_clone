#!/usr/bin/python3
"""
    Module for Base class
    Contains the Base class for the AirBnB clone console.
"""
from multiprocessing import Value
from uuid import uuid4
from datetime import datetime;

class BaseModel:
    """
        BaseModel: Base class for all AirBnB clone console.
        ---------------

        Attributes:
        ---------------
        id: str
            unique id for created instance.
        created_at: str
            current time when instance was created
        updated_at: str
            current time when instance was created/updated
    """

    def __init__(self, *args, **kwargs):
        """
            Constructs all the necessary instances of BaseModel class.
            ---------------

            Parameters
            ---------------
            self: BaseModel instance
            *args: list of arguments
            **kwargs: dict of key-value arguments
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
            Return instance detail in human-readable string.
            ---------------

            Parameters
            ---------------
            self: BaseModel instance
        """

        return("{} {} {} \n" .format(type(self).__name__, self.id, self.__dict__))
    
    def save(self):
        """
            Update the updated_at attribute with current datatime
            ---------------

            Parameters
            ---------------
            self: BaseModel instance
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__ of the instance.
            ---------------

            Parameters
            ---------------
            self: BaseModel instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = (self.created_at).isoformat()
        my_dict["updated_at"] = (self.updated_at).isoformat()

        return my_dict


p = BaseModel(created_at = "2017-09-28T21:03:54.052302")