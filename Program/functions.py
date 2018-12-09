import os
import csv
import random

total_answered = 0
known_words_location = 'known_words.dictionary'
running = True

def clear_screen():
    """Clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def csv_to_list(csv_file):
    with open(csv_file, 'rt') as file:
        reader = csv.reader(file)
        return list(reader)


def ask_answer(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    response = input('\nChoose 1 - 4 and press Enter: > ')

    if response.lower() == 'exit':
        end_program()

    validity = check_validity(response, choices, answer)

    return validity


def check_validity(response, choices, answer):
    """Check if response is valid"""
    clear_screen()

    index = int(response) - 1

    if index in range(4):
        response = choices[index]
        correctness = check_correctness(answer, response)
        
        return correctness
    else:
        print('Answer not valid. Enter 1, 2, 3 or 4.\n')
    
        return False


def check_correctness(answer, response):
    """Check if answer is correct or not"""
    if response == answer:
        total_answered += 1

        print('Nice work! You got it!\n')

        return True
    else:
        print('Sorry try again.\n')

        return False

def end_program():
    clear_screen()

    print(f'You got {total_answered} questions right!')


def randomize_choices(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))
        
        rand_set.add(choices[target])

    return list(rand_set)


def rand_row(word_list, question=True, used_words=set()):
    """Returns a random row for both a question with
       answer and random spanish words for multiple choices
       depending on if question is True"""
    done = False
    
    while not done:
        random_row = random.randrange(100)
        row = word_list[random_row]
        word = row[1]
        answer = row[4]

        if question:
            if word not in used_words:
                used_words.add(word)

                done = True
                
                return word, answer
            else:
                continue

        else:
            done = True

            return answer


def ask_question(word, choices, answer):
    """Prints out question prompt"""
    print(f'Translate: {word}')
    
    choices = randomize_choices(choices)
    option = 1

    for choice in choices:
        print(f'\n {option}) {choice}')
        option += 1

    response = ask_answer(answer, choices)
    return response


def read_from_file(file_path):
    read_file = open(file_path, 'r').read()
    dictionary = eval(read_file)

    return dictionary


def save_to_file(dictionary, file_path):
    write_file = open(file_path, 'w')
    
    write_file.write(str(dictionary))
    write_file.close


def find_difficulty(word):
    """A prompt asking the difficulty of each question"""
    difficulty = 0

    while difficulty not in range(1, 6):
        try:
            difficulty = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            difficulty = int(difficulty)

            if difficulty in range(1, 6):
                clear_screen()

                known_words = read_from_file(known_words_location)
                
                known_words[difficulty].append(word)

                save_to_file(known_words, known_words_location)

        except:
            difficulty = 0


def multiple_choice():
    clear_screen()

    while True:
        csv_file = '100_words.csv'
        word_list = csv_to_list(csv_file)

        choices = set()

        word, answer = rand_row(word_list)
        choices.add(answer)

        while len(choices) <= 3:
            choices.add(rand_row(word_list, question=False))

        correct = False

        while not correct:
            correct = ask_question(word, choices, answer)

        find_difficulty(word)


def fill_in_blank():
    print("\nFill-in the blank mode is coming soon!")


def change_language():
    print("\nMultiple language options are coming soon!")


def other():
    print("\nOther features are coming soon!")


def select_menu_item(programs):
    list_of_programs = list(programs.values())
    selection = input('\nChoose an option from the list: ')

    try:
        selection = int(selection) - 1
        
        list_of_programs[selection]()

    except:
        pass

def make_menu(menu_items):
    clear_screen()
    menu = "\nLANGUAGE LEARNING APP\n(type 'exit' to end a program)\n"
    i = 1

    for item in menu_items:
        menu += f'\n\t({i}) {item}'
        i += 1

    return menu