'''

current state: itterates through questions. Responds to user input. 
number of question and attemps available varibles work. 


eventually: merge with tkinter module


'''

import csv
import random

used_words = set()

NUMBER_OF_QUESTION = 10

NUMBER_OF_ATTEMPS = 2


# Returns a random list from an orderd list
def rand_choice(choices):
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))
        rand_set.add(choices[target])

    return list(rand_set)


# Returns a random row for both a question with answer and random spanish words for multiple choices depending on if question is True
def rand_row(csv_file, question=True):
    global used_words
    done = False
    while not done:
        r_target = random.randrange(1, 100)
        r = 1
        for row in csv_file:
            if r == r_target and question == True:
                if f'{row[1]}' not in used_words:
                    used_words.add(f'{row[1]}')
                    done = True
                    return f'{row[1]}', f'{row[4]}'
                else:
                    continue

            elif question == False:
                done = True
                return f'{row[4]}'

            r += 1


# Prints answer promt and returns user input as a boolean
def answer_promt(answer, choices):
    response = input('\nChoose "A" - "D" and press Enter: > ')

    # Check if response is a-d and not empty
    if response.upper() in 'ABCD' and response.upper() != '':
        choice = 'ABCD'.find(response.upper())

        # When choice is the correct answer
        if choices[choice] == answer:
            print('\nNice work! You got it!\n')
            return True
        # When choice is wrond but a valid choice
        elif response.upper() in 'ABCD':
            print('\nSorry try again\n')
            return False

    # When choice is not valid
    else:
        print('\nMake sure you user character "A B C D". Try again\n')
        return False


# Prints out question promt
def question_promt(spanish_word, choices, answer):
    print('=======================================')
    print('Whats the correct translation for: {}'.format(
        spanish_word.capitalize()))
    choices = rand_choice(choices)
    a = ['A', 'B', 'C', 'D']
    x = 0

    for choice in choices:
        print('\n{}.) {}'.format(a[x], choice.capitalize()))
        x += 1

    choice = answer_promt(answer, choices)
    return choice


# Main function 
def question_program(num_of_questions=100):
    global NUMBER_OF_ATTEMPS
    total_questions = num_of_questions
    answered = 0
    while answered <= total_questions:

        with open('100_words.csv', 'rt', encoding='utf8') as csv_file:
            open_csv_words = csv.reader(csv_file, delimiter=',')

            choices = set()

            spanish_word, answer = rand_row(open_csv_words)
            choices.add(answer)

            while len(choices) <= 3:
                choices.add(rand_row(open_csv_words, question=False))
            ans = False
            attemps = 0
            
            while ans != True and attemps < NUMBER_OF_ATTEMPS:
                ans = question_promt(spanish_word, choices, answer)
                attemps += 1
            answered += 1


question_program(num_of_questions=NUMBER_OF_QUESTION)

