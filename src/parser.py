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
        entities_list = []
        parsed_sentence = nlp(sentence)
        for entity in parsed_sentence.ents:
            if entity.label_ in ["LOC", "ORG", "MISC"]:  # cf Wikipedia scheme: https://spacy.io/api/annotation
                place = Place(entity.text, entity.label_)
                entities_list.append(place)

                #TODO: contacter l'API Google Map & compléter l'objet place
                #TODO: contacter l'API Wikipédia & compléter l'objet place

        return entities_list
    
    # TODO: retirer les stop words
    