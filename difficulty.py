from clear_screen import clear_screen
from write_to import write_to

KNOWN_WORDS_LOCATION = 'known_words.txt'

def difficulty(spanish_word):
    """A prompt asking the difficulty of each question"""
    done = False
    while not done:
        try:
            response = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            if int(response) == 1:
                write_to(KNOWN_WORDS_LOCATION, spanish_word)
                done = True
                clear_screen()
                return
            else:
                done = True
                clear_screen()
                return
        except:
            pass