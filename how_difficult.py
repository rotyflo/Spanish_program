from clear_screen import clear_screen
from read_write import read_from_file, save_to_file

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

                known_words = read_from_file(KNOWN_WORDS_LOCATION)
                
                known_words[difficulty].append(word)

                save_to_file(known_words, KNOWN_WORDS_LOCATION)

        except:
            difficulty = 0