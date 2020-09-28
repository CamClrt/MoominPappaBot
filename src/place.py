"""
    This module represente a place
"""


class Place:
    """Respresents a place """

    def __init__(self, name, latitude="", longitude="", description=""):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    def __repr__(self):
        return f"{self.name}, {self.latitude} lat., {self.longitude} lng."