from clear_screen import clear_screen
from ast import literal_eval


def file2dict (file_path):
	"""Turns the dictionary file into a python_dict"""
	read_file = open(file_path, 'r').read()
	python_dict = literal_eval(read_file)
	return python_dict


def dict2set (dictionary):
	known_words_set = set()
	for key, value in dictionary.items():
		for v in value:
			known_words_set.add(v)
	return known_words_set

clear_screen()
print('Type "exit" to end program\n')

known_words = file2dict('known_words.dictionary')
known_words_set = dict2set(known_words)