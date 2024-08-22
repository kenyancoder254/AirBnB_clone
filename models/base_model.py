#!/usr/bin/python3
"""Foundation of all classes"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class of the project"""

    def __init__(self):
        """creates public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """String rep of the class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates current time"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Dictionary rep of the class"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
