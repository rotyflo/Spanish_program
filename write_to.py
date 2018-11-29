def write_to(file_path, input_to_file):
    """Write input to file path"""
    f = open(file_path, 'a+')
    f.write('{}\n'.format(input_to_file))
    f.close()
    return