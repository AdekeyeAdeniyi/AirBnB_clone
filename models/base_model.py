#!/usr/bin/python3
"""
    Module for Base class
    Contains the Base class for the AirBnB clone console.
"""
import uuid;
import datetime;

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
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
            Return instance detail in human-readable string.
        """

        return("{} {} {} \n" .format(type(self).__name__, self.id, self.__dict__))
    
    def save(self):
        """
            Update the update_at attributes with current datetime.
        """
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        """
            Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = (self.created_at).isoformat()
        my_dict["updated_at"] = (self.updated_at).isoformat()

        return my_dict