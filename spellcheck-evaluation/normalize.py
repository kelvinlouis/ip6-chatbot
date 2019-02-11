import re
import unicodedata
import inflect

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


def remove_punctuation(words):
    """Removes: (),.!?:; keeps: '"""
    new_words = []
    for word in words:
        new_word = re.sub('[\.\,\:\(\)\?\!\&]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def remove_all_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_numbers(words):
    """Removes all interger occurrences in list"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit() == False:
            new_words.append(word)
            
    return new_words
    

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_all_punctuation(words)
    words = replace_numbers(words)
    return words
