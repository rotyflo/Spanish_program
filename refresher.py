from clear_screen import clear_screen
from ast import literal_eval
from csv_to_list import csv_to_list


def file2dict(file_path):
	"""Turns the dictionary file into a python_dict"""
	read_file = open(file_path, 'r').read()
	python_dict = literal_eval(read_file)
	return python_dict


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


words_list = csv_to_list('100_words.csv')
known_words = file2dict('known_words.dictionary')
known_words_set = dict2set(known_words)
known_words_translation_dict = translate_to_dict(known_words_set, words_list)
clear_screen()
print('Type "exit" to end program\n')
print(known_words_translation_dict)
