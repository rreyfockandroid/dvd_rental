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
    
    def sort_by_id_asc(self, films: list[FilmModel]):
        films.sort(key=lambda film: film.id, reverse=False)
        return films
    
    def filter_by_id(self, films: list[FilmModel]):
        return [film for film in films if film.id > 3]
    
    def filter_by_rental_duration(self, films: list[FilmModel]) -> list[FilmModel]:
        return [film for film in films if film.rental_duration == 1]
    
    def filter_by_len(self, films: list[FilmModel]):
        return [film for film in films if film.length > 4]
        
    def films_map(self) -> dict:
        f_dict = dict()
        f_set = set()
        i = 0
        for film in self.sort_by_id_asc(self.__film_ds.films()):
            if i == 5:
                break
            f_dict[film] = 'VAL_' + film.title
            f_set.add(film)
            i = i+1

        for key, item in zip(f_dict.keys(), f_dict.items()):
            print(f_dict[key], ' ', hash(f_dict[key]))
            print(key.title, " ITEM: ", item, '; KEY: ', item[0], ' VAL: ', item[1])
        
        
        for key in f_dict.keys():
            print('type: ', type(key), ' val: ', f_dict[key])

        while len(f_set) > 0:
            print("POP: ", f_set.pop())
        
        try:
            find = FilmModel(2,'title','desc', 1, 1)
            f = f_dict[find]
            print("Found key: ", f)
        except KeyError as e:
            print('Key not found ', e)