def read_from_file(file_path):
	read_file = open(file_path, 'r').read()
	dictionary = eval(read_file)

	return dictionary


def save_to_file(dictionary, file_path):
	write_file = open(file_path, 'w')
	
	write_file.write(str(dictionary))
	write_file.close
