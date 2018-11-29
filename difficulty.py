from clear_screen import clear_screen
from write_to import write_to

KNOWN_WORDS_LOCATION = 'known_words.txt'

def difficulty(spanish_word):
    """A prompt asking the difficulty of each question"""
    response = 0

    while response < 1 or response > 5:
        response = int(input('Rate difficulty from 1(EASY) to 5(HARD): '))
        
        if response == 1:
            write_to(KNOWN_WORDS_LOCATION, spanish_word)