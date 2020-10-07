"""
    This module represente a place
"""


class Place:
    """Respresents a place
    
    >>> place_object = Place("Uluru", -25.344, 131.036)
    >>> print(place_object)
    Uluru, -25.344 lat., 131.036 lng.
    """

    def __init__(self, latitude="", longitude="", description=""):
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    def __repr__(self):
        return f"{self.latitude}lat., {self.longitude}lng., {self.description}"