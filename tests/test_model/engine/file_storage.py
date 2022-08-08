#!/usr/bin/python3
""" Module for FileStorage Class"""

import json
import os

class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return Filestorage object """
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        new_obj_id = "{} {}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[new_obj_id] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as to_file:
            (json.dump(new_dict, to_file))

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict