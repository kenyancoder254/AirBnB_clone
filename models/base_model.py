#!/usr/bin/python3
"""Define all common attributs/methods"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, id, created_at, updated_at):
        """Constructor"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Display class information"""
        return f"[{self.__class.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary with class information"""
        record_dict = self.__dict__.copy()
        record_dict['__class__'] = self.__class__.__name__
        if 'created_at' in record_dict:
            record_dict['created_at'] = record_dict['created_at'].isoformat()
        if 'updated_at' in record_dict:
            record_dict['updated_at'] = record_dict['updated_at']
    return record_dict
