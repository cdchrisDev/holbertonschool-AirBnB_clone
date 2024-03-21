#!/usr/bin/python3
"""Class BaseModel"""

from os import getenv
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

time ="%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Simple base for Air-Bnb Obj"""
    
    __nmObj = 0

    def __init__(self, *args, **kwargs):
        """ Init of the base model """
        if kwargs is None or kwargs == "":
            self.id = str(uuid.uuid4())
            storage.new(self)
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items(): # running dict
                if key != "__class__":
                    setattr(self, key, value) #dynamically
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.update_at) is str:
                self.updated_at = datetime.strptime(kwargs[update_at], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Str rep of BaseModel Class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """Returns dict with key/value pairs"""

        Ndict = self.__dict__.copy()
        if "created_at" in Ndict:
            Ndict["created_at"] = Ndict["created_at"].strftime(time)
        if "updated_at" in Ndict:
            Ndict["updated_at"] = Ndict["updated_at"].strftime(time)
        Ndict["__class__"] = self.__class__.__name__

        return Ndict
