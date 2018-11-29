import random

used_words = set()

def rand_choice(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))
        rand_set.add(choices[target])

    return list(rand_set)


def rand_row(csv_file, question=True):
    """Returns a random row for both a question with
       answer and random spanish words for multiple choices
       depending on if question is True"""
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