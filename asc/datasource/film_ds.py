from model.film_model import *
from datasource.file_persistence import *
import pickle

class FilmDS():
    __films = []

    def __init__(self):
        # self.__films = self.create_films()
        self.__films = load_binary('films.dat')

    def film(self, id: int) -> FilmModel:
        return self.__films[id]
    
    def films(self) -> list[FilmModel]:
        return self.__films
    
    def create_films(self):
        films = []
        for i in range(30):
            mod = i%4
            films.append(FilmModel(i, 'Title_' + str(i), 'Description_' + str(mod) + str(FilmDS.length(mod)), mod, FilmDS.length(mod)))
        return films
    
    @staticmethod
    def length(val):
        return val * 2
    
    def save(self):
        file = 'films'
        save_binary(file + '.dat', self.__films)
        save(file + '.txt', self.__films)

