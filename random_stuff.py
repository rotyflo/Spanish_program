import random

def rand_choice(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))
        
        rand_set.add(choices[target])

    return list(rand_set)


def rand_row(csv_file, question=True, used_words=set()):
    """Returns a random row for both a question with
       answer and random spanish words for multiple choices
       depending on if question is True"""
    done = False
    
    while not done:
        r_target = random.randrange(1, 100)
        r = 1

        for row in csv_file:
            word = row[1]
            answer = row[4]

            if r == r_target and question == True:
                if word not in used_words:
                    used_words.add(word)

                    done = True
                    
                    return word, answer
                else:
                    continue

            elif question == False:
                done = True

                return answer

            r += 1