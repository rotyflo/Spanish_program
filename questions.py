from answers import answer_prompt
from random_stuff import rand_choice
from clear_screen import clear_screen

def question_prompt(spanish_word, choices, answer):
    """Prints out question prompt"""
    clear_screen()

    print('Translate: ' + spanish_word.capitalize())
    
    choices = rand_choice(choices)
    a = ['1', '2', '3', '4']
    x = 0

    for choice in choices:
        print('\n {}) {}'.format(a[x], choice.capitalize()))
        x += 1

    choice = answer_prompt(answer, choices)
    return choice