

import os
import pickle

PICKLE_FILE = 'pickle.dat'

def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass

        if __name__ == '__main__':
            main()