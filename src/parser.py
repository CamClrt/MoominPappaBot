"""
    This module represente the parser
"""

from src.place import Place
from src.models.google_api import GoogleGeocodingApi
#from src.models.wikimedia_api import ???
from config import STOP_WORDS, PUNCTUATION, FORMULATION
import unidecode
import re


class Parser:
    """Respresents the parser """

    def __init__(self):
        self.stop_words = STOP_WORDS
        self.ponctuation = PUNCTUATION
        self.formulation = FORMULATION
    
    def define_place(self, sentence):
        """process question and return a place object"""
        location = self.process_question(sentence)
        place_object = None
        if location != None:
            place_object = Place()
            google_api = GoogleGeocodingApi(location)
            if google_api.latitude != None and google_api.longitude != None:
                place_object.latitude = google_api.latitude
                place_object.longitude = google_api.longitude
                #wikimedia part
                #si aucun coordonnées alors référencer place_object par None
        return place_object

    def process_question(self, sentence): 
        """Find named entities and filter them"""
        sentence_without_case_sensitive = self.remove_case_sensitive(sentence)
        sentence_without_accents = self.remove_accents(sentence_without_case_sensitive)
        sentence_without_ponctuation = self.remove_ponctuation(sentence_without_accents)
        normelized_sentence = sentence_without_ponctuation
        location = self.extract_location(normelized_sentence)
        return location

    def remove_case_sensitive(self, sentence):
        """Parse sentence and remove case-sensitive"""
        return sentence.lower()
    
    def remove_accents(self, sentence):
        """Parse sentence and remove accents"""
        return unidecode.unidecode(sentence)

    def remove_ponctuation(self, sentence):
        """Parse sentence and remove ponctuation"""
        sentence_without_ponctuation = sentence
        for caracter in sentence:
            if caracter in self.ponctuation:
                sentence_without_ponctuation = sentence_without_ponctuation.replace(caracter, "")
        return sentence_without_ponctuation.strip()
    
    def remove_stop_words(self, sentence):
        """Parse location & remove stop words"""
        sentence_without_stop_words = sentence.split()
        for word in sentence.split():
            if word in self.stop_words:
                sentence_without_stop_words.remove(word)
        res = " ".join(sentence_without_stop_words)
        return res.strip()
 
    def extract_location(self, sentence):
        """Parse sentence and extract location:
        to use this method suposed that you have already used the 3 methods:
        - remove_case_sensitive
        - remove_accents
        - remove_ponctuation
        in order to proccess the sentence in input and get a valid result"""
        for formulation in self.formulation:
            formulation_without_case_sensitive = self.remove_case_sensitive(formulation)
            formulation_without_accents = self.remove_accents(formulation_without_case_sensitive)
            formulation_without_ponctuation = self.remove_ponctuation(formulation_without_accents)
            normelized_formulation = formulation_without_ponctuation
            normelized_formulation_regex = f"{normelized_formulation}.*"
            if re.search(normelized_formulation_regex, sentence):
                extract = re.search(normelized_formulation_regex, sentence)
                location_with_stop_words = extract.group().replace(normelized_formulation, "")
                location_without_stop_words = self.remove_stop_words(location_with_stop_words)
                return location_without_stop_words.strip()
