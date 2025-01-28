from django.urls import path

from . import views
from rest_framework import generics
from .models import *
from .serializers import FilmSerializer

class FilmDetail(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmList(generics.ListCreateAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        limit = self.request.query_params.get('limit', 10)
        return Film.objects.all()[:int(limit)]

urlpatterns = [
    path('', views.index, name="index"),
    path('languages/', views.languages, name="languages"),
    path('film/<int:id>/', views.film, name="film"),
    path('api/film/<int:pk>/', FilmDetail.as_view(), name="film-detail"),
    path('api/films/', FilmList.as_view(), name="film-list"),
]