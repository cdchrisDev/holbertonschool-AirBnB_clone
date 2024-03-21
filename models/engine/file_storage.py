import json

#!/usr/bin/python3
"""A class to seria/deserialise JSON"""

class FileStorage():
    __file_path: "file.json"
    __objects = {}

    def all(self):
        """return all obj"""

        return self.__objects

    def new(self, obj):
        """Set in __objects a new"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.obj_id
            self.__objects[key] = obj

    def save(self):
        """Serialize JSON"""
        Jobj = {}
        with open(self.__file_path, 'w') as f:
            json.dump(Jobj, f)

    def reload(self):
        """Deserialize JSON"""
        try:
            with open(self.__file_path, 'r') as f:
                Jo = json.load(f)
            for key in Jo:
                self.__objects[key] = classes[Jo[key]["__class__"]](**Jo[key])
        except:
            pass