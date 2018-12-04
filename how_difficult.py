from clear_screen import clear_screen
from write_to import write_to

KNOWN_WORDS_LOCATION = 'known_words.dictionary'

def find_difficulty(word):
    """A prompt asking the difficulty of each question"""
    difficulty = 0

    while difficulty not in range(1, 6):
        try:
            difficulty = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            difficulty = int(difficulty)

            if difficulty in range(1, 6):
                clear_screen()
                write_to(KNOWN_WORDS_LOCATION, word, difficulty)

        except:
            difficulty = 0