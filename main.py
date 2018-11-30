"""current state: itterates through questions. Responds to user input. 
   number of question and attemps available varibles work. 

   add: a way to rank them and sort by dificulty"""

from csv_to_list import csv_to_list
from clear_screen import clear_screen
from questions import question_prompt
from random_stuff import rand_row
from how_difficult import how_difficult

clear_screen()
print('Type "exit" to end program\n')

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
		correct = question_prompt(word, choices, answer)

	how_difficult(word)