from clear_screen import clear_screen

def answer_prompt(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    response = input('\nChoose 1 - 4 and press Enter: > ')

    if response.lower() == 'exit':
        clear_screen()
        exit()

    validity = is_it_valid(response, choices, answer)
    return validity


def is_it_valid(response, choices, answer):
    """Check if response is valid"""
    if response in '1234' and response != '':
        clear_screen()
        
        response = '1234'.find(response)
        response = choices[response]

        correctness = is_it_correct(answer, response)
        return correctness
    else:
        clear_screen()

        print('Answer not valid. Enter 1, 2, 3 or 4.\n')
        
        return False


def is_it_correct(answer, response):
    """Check if answer is correct or not"""
    if response == answer:
        print('Nice work! You got it!\n')
        return True
    else:
        print('Sorry try again\n')
        return False