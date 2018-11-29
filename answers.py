from clear_screen import clear_screen

total_answered = 0

def answer_prompt(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    response = input('\nChoose 1 - 4 and press Enter: > ')

    if response.lower() == 'exit':
        clear_screen()

        print('You got {} questions right!'.format(str(total_answered)))
        
        exit()

    validity = is_it_valid(response, choices, answer)

    return validity


def is_it_valid(response, choices, answer):
    """Check if response is valid"""
    clear_screen()

    if response in '1234' and response != '':
        response = '1234'.find(response)
        response = choices[response]
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