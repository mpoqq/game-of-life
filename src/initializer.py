import numpy as np


def initialize_from_file(file):
    new_file = ""
    for line in file.readlines():
        if not line.startswith("#"):
            new_file += line
    new_file.rsplit()
    x = new_file.splitlines()[1]
    y = new_file.splitlines()[0]
    new_file = new_file[new_file.find('\n') + 2:]
    new_file = new_file[new_file.find('\n'):]
    grid = np.fromstring(new_file, sep=" ")
    return np.reshape(grid, (int(x), int(y)))


def initialize_random(random_config, number_of_columns, number_of_rows):
    return np.random.choice(p=[random_config, 1 - random_config], a=2, size=(number_of_columns, number_of_rows))
