"""
    This module test the mediawiki api class
"""

from src.models.mediawiki_api import MediawikiApi
import requests


def test_get_data_success(monkeypatch):
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
                    "continue": {
                        "excontinue": 1,
                        "continue": "||info"
                    },
                    "query": {
                        "pages": {
                            "151688": {
                                "pageid": 151688,
                                "ns": 0,
                                "title": "Naantali",
                                "index": -1,
                                "extract": "Naantali (en suédois Nådendal, en latin Vallis Gratiae - la vallée de grâce) est une ville du sud-ouest de la Finlande. Cette petite ville, qui compte une population de 19 000 habitants, se situe dans la province de Finlande occidentale et la région de Finlande du Sud-Ouest, à 15 km à l'ouest de Turku, la capitale provinciale.",
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-08T00:35:54Z",
                                "lastrevid": 169716755,
                                "length": 14393,
                                "fullurl": "https://fr.wikipedia.org/wiki/Naantali",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Naantali&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Naantali"
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
                                "fullurl": "https://fr.wikipedia.org/wiki/Muumimaailma",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Muumimaailma&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Muumimaailma"
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
                                "fullurl": "https://fr.wikipedia.org/wiki/Kultaranta",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Kultaranta&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Kultaranta"
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
                                "fullurl": "https://fr.wikipedia.org/wiki/Port_de_Naantali",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Port_de_Naantali&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Port_de_Naantali"
                            },
                            "8030094": {
                                "pageid": 8030094,
                                "ns": 0,
                                "title": "Gare de Raisio",
                                "index": 3,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-08T01:28:12Z",
                                "lastrevid": 172271773,
                                "length": 3275,
                                "fullurl": "https://fr.wikipedia.org/wiki/Gare_de_Raisio",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Gare_de_Raisio&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Gare_de_Raisio"
                            },
                            "8700429": {
                                "pageid": 8700429,
                                "ns": 0,
                                "title": "Luonnonmaa",
                                "index": 4,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-08T00:47:21Z",
                                "lastrevid": 168445475,
                                "length": 2377,
                                "fullurl": "https://fr.wikipedia.org/wiki/Luonnonmaa",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Luonnonmaa&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Luonnonmaa"
                            },
                            "8730617": {
                                "pageid": 8730617,
                                "ns": 0,
                                "title": "Väski",
                                "index": 5,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-08T00:47:22Z",
                                "lastrevid": 142856396,
                                "length": 2571,
                                "fullurl": "https://fr.wikipedia.org/wiki/V%C3%A4ski",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=V%C3%A4ski&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/V%C3%A4ski"
                            },
                            "11241331": {
                                "pageid": 11241331,
                                "ns": 0,
                                "title": "Église de Naantali",
                                "index": 6,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-04T16:28:31Z",
                                "lastrevid": 172798736,
                                "length": 6523,
                                "fullurl": "https://fr.wikipedia.org/wiki/%C3%89glise_de_Naantali",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=%C3%89glise_de_Naantali&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/%C3%89glise_de_Naantali"
                            },
                            "12779182": {
                                "pageid": 12779182,
                                "ns": 0,
                                "title": "Hôtel d'hydrothérapie de Naantali",
                                "index": 7,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-06T12:57:56Z",
                                "lastrevid": 163030139,
                                "length": 1948,
                                "fullurl": "https://fr.wikipedia.org/wiki/H%C3%B4tel_d%27hydroth%C3%A9rapie_de_Naantali",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=H%C3%B4tel_d%27hydroth%C3%A9rapie_de_Naantali&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/H%C3%B4tel_d%27hydroth%C3%A9rapie_de_Naantali"
                            },
                            "13178413": {
                                "pageid": 13178413,
                                "ns": 0,
                                "title": "Chantier de réparation navale de Turku",
                                "index": 8,
                                "contentmodel": "wikitext",
                                "pagelanguage": "fr",
                                "pagelanguagehtmlcode": "fr",
                                "pagelanguagedir": "ltr",
                                "touched": "2020-10-04T16:30:15Z",
                                "lastrevid": 168359997,
                                "length": 8461,
                                "fullurl": "https://fr.wikipedia.org/wiki/Chantier_de_r%C3%A9paration_navale_de_Turku",
                                "editurl": "https://fr.wikipedia.org/w/index.php?title=Chantier_de_r%C3%A9paration_navale_de_Turku&action=edit",
                                "canonicalurl": "https://fr.wikipedia.org/wiki/Chantier_de_r%C3%A9paration_navale_de_Turku"
                            }
                        }
                    }
                }

    parameters={
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

    headers = {'date': "10/10/2020", 'user-agent': '"MoominPappaBot/fake_version'}

    def mock_get(url, params=parameters, headers=headers, timeout=10):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)

    request = MediawikiApi("user_input1", "user_input2")
    result = request.get_data()
    expected_result = {'title': 'Naantali', 'extract': "Naantali (en suédois Nådendal, en latin Vallis Gratiae - la vallée de grâce) est une ville du sud-ouest de la Finlande. Cette petite ville, qui compte une population de 19 000 habitants, se situe dans la province de Finlande occidentale et la région de Finlande du Sud-Ouest, à 15 km à l'ouest de Turku, la capitale provinciale.", 'fullurl': 'https://fr.wikipedia.org/wiki/Naantali'}
    assert result == expected_result

def test_get_data_failure(monkeypatch):
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

    parameters={
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

    headers = {'date': "10/10/2020", 'user-agent': '"MoominPappaBot/fake_version'}

    def mock_get(url, params=parameters, headers=headers, timeout=10):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)

    request = MediawikiApi("user_input1", "user_input2")
    result = request.get_data()
    expected_result = None
    assert result == expected_result