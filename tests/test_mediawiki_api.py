"""This module test the mediawiki api class."""

import requests

from src.models.mediawiki_api import MediawikiApi


def test_get_data_success(monkeypatch):
    """GIVEN a monkeypatched version of requests.get() WHEN the HTTP response
    is set to successful THEN check the HTTP response."""

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                "continue": {"excontinue": 1, "continue": "||info"},
                "query": {
                    "pages": {
                        "151688": {
                            "pageid": 151688,
                            "ns": 0,
                            "title": "Naantali",
                            "index": -1,
                            "extract": "Naantali (en suédois Nådendal, en latin Vallis Gratiae - la vallée de grâce) est une ville du sud-ouest de la Finlande. Cette petite ville, qui compte une population de 19 000 habitants, se situe dans la province de Finlande occidentale et la région de Finlande du Sud-Ouest, à 15 km à l'ouest de Turku, la capitale provinciale.",  # noqa: E501
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-10-08T00:35:54Z",
                            "lastrevid": 169716755,
                            "length": 14393,
                            "fullurl": "https://fr.wikipedia.org/wiki/Naantali",  # noqa: E501
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Naantali&action=edit",  # noqa: E501
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Naantali",  # noqa: E501
                        },
                        "2709037": {
                            "pageid": 2709037,
                            "ns": 0,
                            "title": "Muumimaailma",
                            "index": 0,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-10-04T16:19:49Z",
                            "lastrevid": 168229306,
                            "length": 1447,
                            "fullurl": "https://fr.wikipedia.org/wiki/Muumimaailma",  # noqa: E501
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Muumimaailma&action=edit",  # noqa: E501
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Muumimaailma",  # noqa: E501
                        },
                        "5751499": {
                            "pageid": 5751499,
                            "ns": 0,
                            "title": "Kultaranta",
                            "index": 1,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-10-08T00:43:32Z",
                            "lastrevid": 164009230,
                            "length": 11889,
                            "fullurl": "https://fr.wikipedia.org/wiki/Kultaranta",  # noqa: E501
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Kultaranta&action=edit",  # noqa: E501
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Kultaranta",  # noqa: E501
                        },
                        "7700543": {
                            "pageid": 7700543,
                            "ns": 0,
                            "title": "Port de Naantali",
                            "index": 2,
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2020-10-04T16:25:50Z",
                            "lastrevid": 162923416,
                            "length": 2675,
                            "fullurl": "https://fr.wikipedia.org/wiki/Port_de_Naantali",  # noqa: E501
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Port_de_Naantali&action=edit",  # noqa: E501
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Port_de_Naantali",  # noqa: E501
                        },
                    }
                },
            }

    parameters = {
        "action": "query",
        "prop": "extracts|info",
        "inprop": "url",
        "explaintext": True,
        "exsentences": 2,
        "exlimit": 1,
        "generator": "geosearch",
        "ggsradius": 10000,
        "ggscoord": f"{00000}|{00000}",
        "format": "json",
    }

    headers = {
        "date": "10/10/2020",
        "user-agent": '"MoominPappaBot/fake_version',
    }

    def mock_get(url, params=parameters, headers=headers, timeout=10):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    request = MediawikiApi("user_input1", "user_input2")
    result = request.get_data()
    expected_result = {
        "title": "Naantali",
        "extract": "Naantali (en suédois Nådendal, en latin Vallis Gratiae - la vallée de grâce) est une ville du sud-ouest de la Finlande. Cette petite ville, qui compte une population de 19 000 habitants, se situe dans la province de Finlande occidentale et la région de Finlande du Sud-Ouest, à 15 km à l'ouest de Turku, la capitale provinciale.",  # noqa: E501
        "fullurl": "https://fr.wikipedia.org/wiki/Naantali",
    }
    assert result == expected_result


def test_get_data_failure(monkeypatch):
    """GIVEN a monkeypatched version of requests.get() WHEN the HTTP response
    is set to failed THEN check the HTTP response."""

    class MockResponse(object):
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"error": "bad"}

    parameters = {
        "action": "query",
        "prop": "extracts|info",
        "inprop": "url",
        "explaintext": True,
        "exsentences": 2,
        "exlimit": 1,
        "generator": "geosearch",
        "ggsradius": 10000,
        "ggscoord": f"{00000}|{00000}",
        "format": "json",
    }

    headers = {
        "date": "10/10/2020",
        "user-agent": '"MoominPappaBot/fake_version',
    }

    def mock_get(url, params=parameters, headers=headers, timeout=10):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    request = MediawikiApi("user_input1", "user_input2")
    result = request.get_data()
    expected_result = None
    assert result == expected_result
