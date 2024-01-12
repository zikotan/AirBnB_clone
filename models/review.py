#!/usr/bin/python3
"""the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review
    
    Attributes:
        place_id (str): arg1
        user_id (str): arg2
        name (str): arg3
    """
    
    place_id = ""
    user_id = ""
    name = ""
