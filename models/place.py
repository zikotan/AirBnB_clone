#!/usr/bin/python3
"""the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place
    
    Attributes:
        city_id (str): arg1
        user_id (str): arg2
        name (str): arg3
        description (str): arg4
        number_rooms (int): arg5
        number_bathrooms (int): arg6
        max_guest (int): arg7
        price_by_night (int): arg8
        latitude (float): arg9
        longitude (float): arg10
        amenity_ids (list): arg11
    """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
