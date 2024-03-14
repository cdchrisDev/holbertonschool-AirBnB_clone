#!/usr/bin/python3
"""Class BaseModel"""

from os import getenv
import models
import uuid
from datetime import datetime

time ="%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Simple base for Air-Bnb Obj"""
    
    __nmObj = 0

    def __init__(self, *args, **kwargs):
        """ Init of the base model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """Str rep of BaseModel Class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.utcnow()

    def to_dict(self, save_fs=None):
        """Returns dict with key/value pairs"""

        Ndict = self.__dict__.copy()
        if "created_at" in Ndict:
            Ndict["created_at"] = Ndict["created_at"].strftime(time)
        if "updated_at" in Ndict:
            Ndict["updated_at"] = Ndict["updated_at"].strftime(time)
        Ndict["__class__"] = self.__class__.__name__

        return Ndict