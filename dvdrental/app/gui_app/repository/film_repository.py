import json
from repository.rest_connector import getFilm, putFilm
from model.gui_model import film_model



class FilmRepository():    
    def getField(self, film_id):
        return self._json_fields()
        
    def getFilm(self, id):
        return getFilm(id)
    
    def updateFilm(self, id, data):
        return putFilm(id, data, film_model)