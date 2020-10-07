"""
    This module represente the Google API class
"""

from config import GEOCODING_API_KEY, GEOCODING_API_URL, DATE, APP_NAME
import requests


class GoogleGeocodingApi():
    """Respresents the Google geocoding API"""

    def __init__(self, location):
        self.key = GEOCODING_API_KEY
        self.location = location
        self.url = None
    
    @property
    def latitude(self):
        """Import data from API and give latitude"""
        if self.get_localisation() != None:
            return self.get_localisation().get("lat")
    
    @property
    def longitude(self):
        """Import data from API and give longitude"""
        if self.get_localisation() != None:
            return self.get_localisation().get("lng")

    def set_url(self):
        """When GoogleGeocodingApi object is created, a customized url is generated"""
        self.url = GEOCODING_API_URL.replace("LOCATION", self.location).replace("KEY", self.key)
    
    def get_localisation(self):
        """Import latitude & longitude from the Google API"""
        self.set_url()
        
        headers = {'date': DATE, 'user-agent': APP_NAME}
        response = requests.get(self.url, headers=headers, timeout=10)
        if response.status_code == 200:
            content = response.json()
            if content.get("status") == "OK":
                return content.get("results")[0].get("geometry").get("location")
            else:
                print("API error : status not OK")
        else:
            err = f"API error : '{response.status_code}' error occurred"
            print(err)
