import json
from model.gui_model import film_model

jsonString = """[
  {
    "model": "dvdrental.film",
    "pk": 1000,
    "fields": {
      "title": "Zorro Ark",
      "description": "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery",
      "release_year": 2006,
      "rental_duration": 3,
      "rental_rate": "4.99",
      "length": 50,
      "replacement_cost": "18.99",
      "rating": "NC-17",
      "special_features": "[\\"Trailers\\", \\"Commentaries\\", \\"Behind the Scenes\\"]",
      "last_update": "2025-02-08T18:35:05.765",
      "language": 1,
      "actor": [
        155,
        166,
        178
      ]
    }
  }
]"""

apiJsonString = """
{
    "film_id": 1000,
    "actor": [
        {
            "actor_id": 155,
            "first_name": "Ian",
            "last_name": "Tandy",
            "last_update": "2013-05-26T14:47:57.620000Z"
        },
        {
            "actor_id": 166,
            "first_name": "Nick",
            "last_name": "Degeneres",
            "last_update": "2013-05-26T14:47:57.620000Z"
        },
        {
            "actor_id": 178,
            "first_name": "Lisa",
            "last_name": "Monroe",
            "last_update": "2013-05-26T14:47:57.620000Z"
        }
    ],
    "language": "[1] - English             ",
    "title": "Zorro Ark",
    "description": "A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery",
    "release_year": 2006,
    "rental_duration": 3,
    "rental_rate": "4.99",
    "length": 50,
    "replacement_cost": "18.99",
    "rating": "NC-17",
    "special_features": [
        "Trailers",
        "Commentaries",
        "Behind the Scenes"
    ],
    "last_update": "2025-02-08T18:35:05.765570Z"
}
"""

class FilmRepository():
    def _json_fields(self):
        g = json.loads(jsonString)
        return g[0]['fields']
    
    def getField(self, film_id):
        return self._json_fields()
    
    def _json_film(self):
        g = json.loads(apiJsonString)
        return g
    
    def getFilm(self, id):
        return self._json_film()
