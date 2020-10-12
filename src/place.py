"""This module represente a place."""


class Place:
    """Respresents a place.

    >>> place_object = Place("Uluru", -25.344, 131.036)
    >>> print(place_object)
    Uluru, -25.344 lat., 131.036 lng.
    """

    def __init__(
        self, name="", latitude="", longitude="", description="", url=""
    ):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.url = url

    def __repr__(self):
        elements = [
            self.name,
            str(self.latitude),
            str(self.longitude),
            self.description,
            self.url,
        ]
        return ", ".join(elements)
