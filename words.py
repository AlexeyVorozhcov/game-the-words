import json
import random
from unittest import result

NAMEFILE = 'russian_nouns_with_definition.json'
ENCODING = 'utf8'


def _get_dictionary(jsonFile, encoding):
    f = open(jsonFile, 'r', encoding=encoding)
    result = json.load(f)
    f.close()
    return result

def _get_random_pairKeyValue_from_dict(dict):
    return random.choice(list(dict.items()))

def _extract_definition(dict):
    return dict['definition']

def get_word_and_definition():
    dict = _get_dictionary(NAMEFILE, ENCODING)
    word, definition = _get_random_pairKeyValue_from_dict(dict)
    definition = _extract_definition(definition)
    return word, definition

if __name__=="__main__":
    word, definition = get_word_and_definition()
    print(word)
    print (definition) 


    