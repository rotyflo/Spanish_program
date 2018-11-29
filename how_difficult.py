from clear_screen import clear_screen
from write_to import write_to

KNOWN_WORDS_LOCATION = 'known_words.txt'

def how_difficult(spanish_word):
    """A prompt asking the difficulty of each question"""
    difficulty = 0

    while difficulty < 1 or difficulty > 5:
        try:
            difficulty = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            difficulty = int(difficulty)

            if difficulty == 1:
                write_to(KNOWN_WORDS_LOCATION, spanish_word)
        except:
            difficulty = 0