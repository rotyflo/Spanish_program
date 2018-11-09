'''

current state: itterates through questions still reapeating some. Responds to user input and only crashes sometimes... hasnt crashed in a while now.


*issue: rand_row; only repeats once but what to do when its already in used_words

*bug: sometimes multiple choices will come out mixed after being wrong...or should they come mixed and they stay in an order?


add: a timer or number of attemps per question to understand difficulty of each question 


eventually: merge with tkinter module


'''

import csv
import random

used_words = set()

NUMBER_OF_QUESTION = 10

# Still needs to be inplemented into the program
NUMBER_OF_ATTEMPS = 1


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
    r_target = random.randrange(1, 10)
    r = 1
    for row in csv_file:
        if r == r_target and question == True:
            if f'{row[1]}' not in used_words:
                used_words.add(f'{row[1]}')
                return f'{row[1]}', f'{row[4]}'
            else:
                return False
                pass
        elif question == False:
            return f'{row[4]}'
        r += 1


# Prints answer promt and returns user input as a boolean
def answer_promt(answer, choices):
    response = input('\nChoose "A" - "B" and press Enter: > ')

    if response.upper() in 'ABCD' and response.upper() != '':
        choice = 'ABCD'.find(response.upper())
        if choices[choice] == answer:
            print('\nNice work! You got it!\n')
            return True

        elif response.upper() in 'ABCD':
            print('\nSorry try again\n')
            return False

    else:
        print('\nMake sure you user character "A B C D". Try again\n')
        return False


# Prints out question promt
def question_promt(spanish_word, choices, answer):
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

            while ans != True:
                ans = question_promt(spanish_word, choices, answer)
            answered += 1


question_program(num_of_questions=NUMBER_OF_QUESTION)

