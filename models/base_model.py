#!/usr/bin/python3
import uuid
from datetime import datetime
"""BaseModel"""


class BaseModel:
    """Foundation of all classes in the project"""

    def __init__(self):
        """public instance method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print content of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dict containg all key/values of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        if 'created_at' in instance_dict:
            instance_dict['created_at'] = (
                    instance_dict['created_at'].isoformat()
                    )
        if 'updated_at' in instance_dict:
            instance_dict['updated_at'] = (
                    instance_dict['updated_at'].isoformat()
                    )
        return instance_dict
