"""This module represente the parser."""

import unidecode

from config import PUNCTUATION
from config import STOP_WORDS
from src.models.google_api import GoogleGeocodingApi
from src.models.mediawiki_api import MediawikiApi
from src.place import Place


class Parser:
    """Respresents the parser."""

    def __init__(self):
        self.stop_words = STOP_WORDS
        self.ponctuation = PUNCTUATION

    def define_place(self, sentence):
        """process question and return a place object."""
        location = self.process_question(sentence)
        place_object = None
        if location is not None:
            place_object = Place()
            google_api = GoogleGeocodingApi(location)
            if (
                google_api.latitude is not None
                and google_api.longitude is not None
            ):
                place_object.latitude = google_api.latitude
                place_object.longitude = google_api.longitude
                mediawiki_api = MediawikiApi(
                    google_api.latitude, google_api.longitude
                )
                place_object.name = mediawiki_api.title
                place_object.description = mediawiki_api.description
                place_object.url = mediawiki_api.url
        return place_object

    def process_question(self, sentence):
        """Find named entities and filter them."""
        sentence_without_case_sensitive = self.remove_case_sensitive(sentence)
        sentence_without_accents = self.remove_accents(
            sentence_without_case_sensitive
        )
        sentence_without_ponctuation = self.remove_ponctuation(
            sentence_without_accents
        )
        location = self.remove_stop_words(sentence_without_ponctuation)
        return location

    def remove_case_sensitive(self, sentence):
        """Parse sentence and remove case-sensitive."""
        return sentence.lower()

    def remove_accents(self, sentence):
        """Parse sentence and remove accents."""
        return unidecode.unidecode(sentence)

    def remove_ponctuation(self, sentence):
        """Parse sentence and remove ponctuation."""
        sentence_without_ponctuation = sentence
        for caracter in sentence:
            if caracter in self.ponctuation:
                sentence_without_ponctuation = (
                    sentence_without_ponctuation.replace(caracter, "")
                )
        return sentence_without_ponctuation.replace("-", " ").strip()

    def remove_stop_words(self, sentence):
        """Parse location & remove stop words."""
        sentence_without_stop_words = sentence.split()
        for word in sentence.split():
            if word in self.stop_words:
                sentence_without_stop_words.remove(word)
        res = " ".join(sentence_without_stop_words)
        return res.strip()
