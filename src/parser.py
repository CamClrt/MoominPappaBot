"""
    This module represente the parser
"""


class Parser:
    """Respresents the parser """

    def check_question_mark(self, sentence):
        """Check if the sentence is a real question"""
        if sentence.find('?') == -1:
            return False
        else:
            return True
