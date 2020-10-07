"""
    This module test the google api class
"""

from src.models.google_api import GoogleGeocodingApi
import requests


def test_get_localisation_success(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """
    
    class MockResponse(object):

        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                    "results": [
                        {
                            "address_components": [
                                {
                                    "long_name": "Naantali",
                                    "short_name": "Naantali",
                                    "types": [
                                        "locality",
                                        "political"
                                    ]
                                },
                                {
                                    "long_name": "Finland",
                                    "short_name": "FI",
                                    "types": [
                                        "country",
                                        "political"
                                    ]
                                },
                                {
                                    "long_name": "21100",
                                    "short_name": "21100",
                                    "types": [
                                        "postal_code"
                                    ]
                                }
                            ],
                            "formatted_address": "Kailo, 21100 Naantali, Finland",
                            "geometry": {
                                "location": {
                                    "lat": 60.47347029999999,
                                    "lng": 22.0053239
                                },
                                "location_type": "GEOMETRIC_CENTER",
                                "viewport": {
                                    "northeast": {
                                        "lat": 60.4748192802915,
                                        "lng": 22.0066728802915
                                    },
                                    "southwest": {
                                        "lat": 60.47212131970849,
                                        "lng": 22.0039749197085
                                    }
                                }
                            },
                            "place_id": "ChIJ9xQg2cyIi0YRk8BBxLhT-eU",
                            "plus_code": {
                                "compound_code": "F2F4+94 Naantali, Finland",
                                "global_code": "9GG4F2F4+94"
                            },
                            "types": [
                                "amusement_park",
                                "establishment",
                                "point_of_interest",
                                "tourist_attraction"
                            ]
                        }
                    ],
                    "status": "OK"
                }

    headers = {'date': "07/10/2020", 'user-agent': '"MoominPappaBot/fake_version'}
    def mock_get(url, headers=headers, timeout=10):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)

    request = GoogleGeocodingApi("user_input")
    result = request.get_localisation()
    expected_result = {"lat": 60.47347029999999,"lng": 22.0053239}
    assert result == expected_result


def test_get_localisation_failure(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to failed
    THEN check the HTTP response
    """
    
    class MockResponse(object):

        def __init__(self):
            self.status_code = 404

        def json(self):
            return {'error': 'bad'}

    headers = {'date': "07/10/2020", 'user-agent': '"MoominPappaBot/fake_version'}
    def mock_get(url, headers=headers, timeout=10):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)

    request = GoogleGeocodingApi("user_input")
    result = request.get_localisation()
    expected_result = None
    assert result == expected_result
    