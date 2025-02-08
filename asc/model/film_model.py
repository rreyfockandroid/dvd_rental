from array import array
from copy import copy

class Model():
    id: int
    def __init__(self, id):
        self.id = id


class Language(Model):
    name: str

class FilmModel(Model):
    title: str
    description: str
    rental_duration: int
    length: int

    language: Language

    def __init__(self, id, title, desc, rental_duration, length):
        self.title = title
        self.description = desc
        self.rental_duration = rental_duration
        self.length = length

        super().__init__(id)

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        return str(self.id) + ' FilmModel; title: ' + self.title + ' desc: ' + self.description + ' rent_dur: ' + str(self.rental_duration) + ' len: ' + str(self.length)
    

    def __eq__(self, value):
        return self.id == value.id
    
    def __hash__(self):
        return hash(self.id)