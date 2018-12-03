from clear_screen import clear_screen
from write_to import write_to

KNOWN_WORDS_LOCATION = 'known_words.dictionary'

def how_difficult(word):
    """A prompt asking the difficulty of each question"""
    difficulty = 0

    while difficulty < 1 or difficulty > 5:
        try:
            difficulty = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            difficulty = int(difficulty)

            if difficulty >= 1 and difficulty <= 5:
                write_to(KNOWN_WORDS_LOCATION, word, difficulty)
        except:
            if difficulty not in range(1,6):
                difficulty = 0