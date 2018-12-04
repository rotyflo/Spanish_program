from answers import answer_prompt
from random_stuff import rand_choice
from clear_screen import clear_screen

def question_prompt(word, choices, answer):
    """Prints out question prompt"""

    print(f'Translate: {word}')
    
    choices = rand_choice(choices)
    option = 1

    for choice in choices:
        print(f'\n {option}) {choice}')
        option += 1

    choice = answer_prompt(answer, choices)
    return choice