'''

current state: itterates through questions. Responds to user input. 
number of question and attemps available varibles work. 

add: a way to rank them and sort by dificulty


eventually: merge with tkinter module


'''

import csv
import random
import os

used_words = set()

NUMBER_OF_QUESTION = 10

NUMBER_OF_ATTEMPS = 4

KNOWN_WORDS_LOCATION = '/known_words.txt'


# Write input to file path
def write_to(file_path, input_to_file):
	f = open(file_path, 'a+')
	f.write('{}\n'.format(input_to_file))
	f.close()
	return


# Clears screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	return


# A promt asking the difficulty of each question
def difficulty(spanish_word):
	done = False
	while not done:
		try:
			response = input(
				'On a scale of 1 - 5, how difficult was it?\n1 meaning you know it and 5 really hard.\n> '
			)
			if int(response) == 1:
				write_to(KNOWN_WORDS_LOCATION, spanish_word)
				done = True
				clear_screen()
				return
			else:
				done = True
				clear_screen()
				return
		except:
			pass


# Returns a random list from an orderd list
# It should take choices as a parameter in line 64 and choices in 66 should be assigned list(choices)
def rand_choice():
	rand_set = set()
	choices = [1,2,3]

	while len(rand_set) != len(choices):
		target = random.randrange(len(choices))
		rand_set.add(choices[target])

	print(list(rand_set))


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
	response = input('\nChoose 1 - 4 and press Enter: > ')

	# Check if response is a-d and not empty
	if response in '1234' and response != '':
		clear_screen()
		choice = '1234'.find(response)

		# When choice is the correct answer
		if choices[choice] == answer:
			print('Nice work! You got it!\n')
			return True
		# When choice is wrong but a valid choice
		elif response in '1234':
			print('Sorry try again\n')
			return False

	# When calling exit from promt
	elif response.lower() == 'exit':
		clear_screen()
		exit()

	# When choice is not valid
	else:
		clear_screen()
		print('Make sure you use numbers 1, 2, 3 or 4. Try again\n')
		return False


# Prints out question promt
def question_promt(spanish_word, choices, answer):
	print(
		'Whats the correct translation for: {}'.format(spanish_word.capitalize()))
	choices = rand_choice(choices)
	a = ['1', '2', '3', '4']
	x = 0

	for choice in choices:
		print('\n {}) {}'.format(a[x], choice.capitalize()))
		x += 1

	choice = answer_promt(answer, choices)
	return choice


# Main function 
def question_program(num_of_questions=100):
	global NUMBER_OF_ATTEMPS
	total_questions = num_of_questions
	answered = 0

	clear_screen()
	print('Type "exit" to end program\n')

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
			difficulty(spanish_word)
			answered += 1


# question_program(num_of_questions=NUMBER_OF_QUESTION)

