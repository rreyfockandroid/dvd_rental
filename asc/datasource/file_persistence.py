import pickle
from model.film_model import *

PATH = "datasource/"
NEW_LINE_SIGN = '\n'
ENCODING = 'utf-8'

def save(filename, data: iter):
        with open(PATH + filename, 'w', encoding=ENCODING) as file:
            for d in data:
                file.write(str(d))
                file.write(NEW_LINE_SIGN)

def save_binary(filename, data):
    with open(PATH + filename, "wb") as file:
        pickle.dump(data, file,protocol=pickle.HIGHEST_PROTOCOL)


def load(filename):
     with open(PATH + filename, "r", encoding=ENCODING) as file:
        line = file.readline()
        print("LINE: ", line)

def load_binary(filename):
    with open(PATH + filename, "rb") as file:
        res = pickle.load(file)
        return res