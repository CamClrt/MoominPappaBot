"""
    This module represente the parser
"""

from src.place import Place
from config import STOP_WORDS, PUNCTUATION, FORMULATION
import unidecode
import re


class Parser:
    """Respresents the parser """

    def __init__(self):
        self.stop_words = STOP_WORDS
        self.ponctuation = PUNCTUATION
        self.formulation = FORMULATION

    def check_question_mark(self, sentence):
        """Check if the sentence is a real question"""
        if sentence.find('?') == -1:  # return the index of the substring or -1 
            return False
        else:
            return True

    def process_question(self, sentence): 
        """Find named entities and filter them"""
        sentence_without_case_sensitive = self.remove_case_sensitive(sentence)
        sentence_without_accents = self.remove_accents(sentence_without_case_sensitive)
        sentence_without_ponctuation = self.remove_ponctuation(sentence_without_accents)
        normelized_sentence = sentence_without_ponctuation
        location = self.extract_location(normelized_sentence)
        location_without_stop_words = self.remove_stop_words(location)
        return location_without_stop_words

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
        return sentence_without_ponctuation
 
    def extract_location(self, sentence):
        """Parse sentence and extract location:
        used this method suposed that you have already used the 3 methods:
        - remove_case_sensitive
        - remove_accents
        - remove_ponctuation
        in order to proccess the sentence in input and get a valid result"""
        for formulation in self.formulation:
            formulation_without_case_sensitive = self.remove_case_sensitive(formulation)
            formulation_without_accents = self.remove_accents(formulation_without_case_sensitive)
            formulation_without_ponctuation = self.remove_ponctuation(formulation_without_accents)
            normelized_formulation = formulation_without_ponctuation
            normelized_formulation_regex = f"{normelized_formulation}.*?[\?]"
            if re.search(normelized_formulation_regex, sentence):
                extract = re.search(normelized_formulation_regex, sentence)
                location = extract.group().replace("?", "").replace(normelized_formulation, "")
        return location.strip()

    def remove_stop_words(self, location):
        """Parse location & remove stop words"""
        location_without_stop_words = location.split()
        for word in location.split():
            if word in self.stop_words:
                location_without_stop_words.remove(word)
        res = " ".join(location_without_stop_words)
        return res.strip()
