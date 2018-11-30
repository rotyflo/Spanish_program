def write_to(file_path, word):
    """Write input to file path"""
    f = open(file_path, 'a+')
    f.write(f'{word}\n')
    f.close()
    return