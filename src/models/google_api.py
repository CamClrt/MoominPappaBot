"""This module represente the Google API class."""

import requests

from config import APP_NAME
from config import DATE
from config import GEOCODING_API_KEY
from config import GEOCODING_API_URL


class GoogleGeocodingApi:
    """Respresents the Google geocoding API."""

    def __init__(self, location):
        self.key = GEOCODING_API_KEY
        self.api_url = GEOCODING_API_URL
        self.location = location
        self.content = self.get_localisation()

    @property
    def latitude(self):
        """Import data from API and give latitude."""
        if self.content is not None:
            return self.content.get("lat")

    @property
    def longitude(self):
        """Import data from API and give longitude."""
        if self.content is not None:
            return self.content.get("lng")

    def get_localisation(self):
        """Import latitude & longitude from the Google API."""
        parameters = {
            "address": self.location,
            "key": self.key,
        }
        headers = {"date": DATE, "user-agent": APP_NAME}
        response = requests.get(
            self.api_url, params=parameters, headers=headers, timeout=10
        )
        if response.status_code == 200:
            content = response.json()
            if content.get("status") == "OK":
                return (
                    content.get("results")[0].get("geometry").get("location")
                )
            else:
                print("Google API error : status not OK")
        else:
            err = f"Google API error : '{response.status_code}' error occurred"
            print(err)
