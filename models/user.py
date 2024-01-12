#!/usr/bin/python3
"""the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User

    Attributes:
        email (str): arg1
        password (str): arg2
        first_name (str): arg3
        last_name (str): arg4
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
