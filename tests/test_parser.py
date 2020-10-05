"""
    This module test the parser Class
"""

from src.parser import Parser


def test_check_question_mark():
    parser = Parser()
    assert parser.check_question_mark("Où est Moomin World ?") == True

def test_check_question_mark():
    parser = Parser()
    assert parser.check_question_mark("Moomin World") == False

def test_remove_case_sensitive():
    parser = Parser()
    assert parser.remove_case_sensitive("Emmène-moi à Moomin World ?") == "emmène-moi à moomin world ?"

def test_remove_accents():
    parser = Parser()
    assert parser.remove_accents("Emmène-moi à Moomin World ?") == "Emmene-moi a Moomin World ?"

def test_remove_ponctuation():
    parser = Parser()
    assert parser.remove_ponctuation("Bonjour, emmène-moi à Moomin World ?") == "Bonjour emmène-moi à Moomin World ?"

def test_extract_location():
    parser = Parser()
    sentence = "Bonjour! Emmène-moi à Moomin World ? Qu'en penses-tu ? Alors, alors qu'est-ce que tu en dis !"
    sentence_without_case_sensitive = parser.remove_case_sensitive(sentence)
    sentence_without_accents = parser.remove_accents(sentence_without_case_sensitive)
    sentence_without_ponctuation = parser.remove_ponctuation(sentence_without_accents)
    normelized_sentence = sentence_without_ponctuation
    assert parser.extract_location(normelized_sentence) == "moomin world"

def test_remove_stop_words():
    parser = Parser()
    assert parser.remove_stop_words("aux Pays des Moomins") == "Pays Moomins"

def test_process_question():
    parser = Parser()
    sentence = "Bonjour Moominpappa! Où est Moomin World ? Hein? Alors, je t'écoute !"
    assert parser.process_question(sentence) == "moomin world"