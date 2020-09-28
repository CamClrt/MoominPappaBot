"""
    This module represente the parser
"""

from src.place import Place


class Parser:
    """Respresents the parser """

    def check_question_mark(self, sentence):
        """Check if the sentence is a real question"""
        if sentence.find('?') == -1:  # return the index of the substring or -1 
            return False
        else:
            return True

    def process_question(self, sentence): 
        """Find named entities and filter them"""
        #TODO: retirer les stop words, normaliser minuscules/majuscules, éliminer accents, isoler le lieu...
        #placeObject = Place(sentence)
        #TODO: contacter l'API Google Map & compléter l'objet place
        #TODO: contacter l'API Wikipédia & compléter l'objet place

        # if sentence contains a place > return placeObject
        # else > return None

        place_object = Place("Uluru", -25.344, 131.036)

        return place_object
        
    
    
