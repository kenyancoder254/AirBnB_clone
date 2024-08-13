#!/usr/bin/python3
"""Base class"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for the project"""
    def __init__(self):
        """
        initializes public attributes with values
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        """string representation of the class"""
        return (f"[{self.__class__.__name__}] ({self.id}) self.__dict__")

    def save(self):
        """updates the current time"""
        self.updated_at = datetime.utcnow().isoformat()

    def to_dict(self):
        """Dictionary rep of the classs"""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"] + "Z"
        data["updated_at"] = data["updated_at"] + "Z"
        return data
