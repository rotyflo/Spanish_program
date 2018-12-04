from clear_screen import clear_screen

total_answered = 0

def answer_prompt(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    response = input('\nChoose 1 - 4 and press Enter: > ')

    if response.lower() == 'exit':
        end_program()

    validity = is_it_valid(response, choices, answer)

    return validity


def is_it_valid(response, choices, answer):
    """Check if response is valid"""
    clear_screen()

    index = int(response) -1

    if index in range(4):
        response = choices[index]
        correctness = is_it_correct(answer, response)
        
        return correctness
    else:
        print('Answer not valid. Enter 1, 2, 3 or 4.\n')
    
        return False


def is_it_correct(answer, response):
    """Check if answer is correct or not"""
    global total_answered

    if response == answer:
        total_answered += 1

        print('Nice work! You got it!\n')

        return True
    else:
        print('Sorry try again\n')

        return False

def end_program():
    clear_screen()

    print(f'You got {total_answered} questions right!')
        
    exit()