from datasource.film_ds import FilmDS
from model.film_model import FilmModel

class FilmRepository():
    __film_ds = FilmDS()

    def filmDs(self) -> FilmDS:
        return self.__film_ds

    def film(self, id) -> FilmModel:
        return self.__film_ds.film(id)
    
    def films(self) -> list[FilmModel]:
        films = self.__film_ds.films()
        # films = self.sort_by_id(films)
        films = self.sort_by(films, 'id')
        return films
    
    def sort_by(self, films: list[FilmModel], field: str):
        films.sort(key=lambda film: getattr(film, field), reverse=True)
        return films

    def sort_by_id(self, films: list[FilmModel]):
        films.sort(key=lambda film: film.id, reverse=True)
        return films
    
    def filter_by_id(self, films: list[FilmModel]):
        return [film for film in films if film.id > 3]
    
    def filter_by_rental_duration(self, films: list[FilmModel]) -> list[FilmModel]:
        return [film for film in films if film.rental_duration == 1]
    
    def filter_by_len(self, films: list[FilmModel]):
        return [film for film in films if film.length > 4]
        
