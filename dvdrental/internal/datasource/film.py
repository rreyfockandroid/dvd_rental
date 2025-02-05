from dvdrental.models import Film
from datetime import datetime

def process(films) -> list[Film]:
    # return sort_by_title(films)
    # return sort_by(films, 'title')
    return filter_by(films)

def distinct(films):
    return " Films:  " + str(len(films)) + str(datetime.timestamp(datetime.now()))

def sort_by(films, field) -> list[Film]:
    sorted = list(films)
    sorted.sort(reverse=False, key=lambda film: getattr(film, field))
    return sorted

def sort_by_title(films):
    films = list(films)
    films.sort(key=lambda film: film.title, reverse=True)
    return films

def filter_by(films):
    filtered = [film for film in films if film.rental_duration > 5]
    return filtered
    

