from repository import film_ry
from datasource import film_ds

if __name__ == '__main__':
    rep = film_ry.FilmRepository()
    film = rep.film(3)
    # print(film)

    films = rep.films()

    films = rep.filter_by_len(films)
    # films = rep.filter_by_rental_duration(films)

    # print(films)

    # for film in films:
        # print(film)


    # rep.filmDs().save()
    # films = rep.filmDs().load()
    # print(films)

    # rep.filmDs().save()

    rep.films_map()