#!/usr/bin/python3
"""
    Module for Base class
    Contains the Base class for the AirBnB clone console.
"""
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

    def __init__(self):
        """
            Constructs all the necessary instances of BaseModel class.
            ---------------

            Parameters
            ---------------
            self: BaseModel instance
        """
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