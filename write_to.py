def write_to(file_path, word, difficulty):
    """Write input to file path"""
    read_file = open(file_path, 'r').read()
    write_file = open(file_path, 'w')
    print(type(read_file))
    known_words = eval(read_file)

    known_words[difficulty].append(word)

    write_file.write(str(known_words))
    write_file.close()

    return