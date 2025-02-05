from django.urls import path
from . import views
from rest_framework import generics
from .models import *
from .serializers import FilmSerializer, CutFilmSerializer
import logging
from django.http import JsonResponse
from dvdrental.internal.datasource.film import process

logger = logging.getLogger(__name__)

class FilmDetail(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmList(generics.ListCreateAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    def list(self, request):
        logger.debug("FilmList-list called")
        limit = self.request.query_params.get('limit', 10)
        films = self.get_queryset()[:int(limit)]
        serializer = FilmSerializer(films, many=True)
        return JsonResponse(serializer.data, safe=False)   

    def get_queryset(self):
        logger.debug("FilmList-get_queryset called")
        return super().get_queryset() 

    # def get_queryset(self):
    #     logger.debug("get_queryset called")
    #     limit = self.request.query_params.get('limit', 10)
    #     films = Film.objects.all()[:int(limit)]
    #     return films

class CutFilmList(generics.ListCreateAPIView):
    serializer_class = CutFilmSerializer

    def get_queryset(self):
        logger.debug("CutFilmList-get_queryset called")
        limit = self.request.query_params.get('limit', 10)
        films = Film.objects.order_by('-film_id').all()[:int(limit)]
        films = process(films)
        return films
    

urlpatterns = [
    path('', views.index, name="index"),
    path('languages/', views.languages, name="languages"),
    path('film/<int:id>/', views.film, name="film"),
    path('films/', CutFilmList.as_view(), name="films"),
    path('api/film/<int:pk>/', FilmDetail.as_view(), name="film-detail"),
    path('api/films/', FilmList.as_view(), name="film-list"),

]