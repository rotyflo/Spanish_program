from clear_screen import clear_screen
from ast import literal_eval
from csv_to_list import csv_to_list
from read_write import read_from_file
import random

def dict2set(dictionary):
	"""Make a dictionary to a set"""
	known_words_set = set()
	for key, value in dictionary.items():
		for v in value:
			known_words_set.add(v)
	return known_words_set


def translate_to_dict(word_set, word_list):
	english = []
	spanish = []
	for word in word_set:
		for lists in word_list:
			if word in lists:
				english.append(lists[4])
				spanish.append(word)
	return dict(zip(spanish,english))

def dict2list(dictionary):
	list_of_pairs = []
	for key, value in dictionary.items():
		temp = [key, value]
		list_of_pairs.append(temp)
	return list_of_pairs


def rand_pair(known_words_list, question=True, used_words=set()):
	


	done = False

	while not done:
		rand_index = random.randrange(len(known_words_list))
		rand_pair = known_words_list[rand_index]
		spanish = rand_pair[0]
		english = rand_pair[1]

		if question == True:
			if spanish not in used_words:
				used_words.add(spanish)

				done = True

				return spanish, english
			else:
				continue

		else:
			done = True

			return english



words_list = csv_to_list('100_words.csv')
known_words = read_from_file('known_words.dictionary')
known_words_set = dict2set(known_words)
known_words_translation_dict = translate_to_dict(known_words_set, words_list)
known_words_list = dict2list(known_words_translation_dict)


clear_screen()

print(rand_pair(known_words_list, False))
print(rand_pair(known_words_list))










