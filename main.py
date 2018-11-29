"""current state: itterates through questions. Responds to user input. 
   number of question and attemps available varibles work. 

   add: a way to rank them and sort by dificulty"""

import csv
from clear_screen import clear_screen
from questions import question_prompt
from random_stuff import rand_row
from write_to import write_to
from difficulty import difficulty

NUMBER_OF_QUESTION = 10
answered = 0

clear_screen()
print('Type "exit" to end program\n')

while answered <= NUMBER_OF_QUESTION:
	with open('100_words.csv', 'rt', encoding='utf8') as csv_file:
		open_csv_words = csv.reader(csv_file, delimiter=',')

		choices = set()

		spanish_word, answer = rand_row(open_csv_words)
		choices.add(answer)

		while len(choices) <= 3:
			choices.add(rand_row(open_csv_words, question=False))

		ans = False
		attemps = 0

		while ans != True:
			ans = question_prompt(spanish_word, choices, answer)

		difficulty(spanish_word)
		answered += 1