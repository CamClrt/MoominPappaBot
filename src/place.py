"""
    This module represente a place
"""


class Place:
    """Respresents a place """

    def __init__(self, name, latitude, longitude, address, description):
        self.name = name
        self.latitude = ""
        self.longitude = ""
        self.address = ""
        self.description = ""

    def __repr__(self):
        return f"{self.name}, {self.latitude} lat., {self.longitude} long."