from django.urls import path
from . import views
from rest_framework import generics
from .models import *
from .serializers import FilmSerializer
from dvdrental.internal.datasource.film import distinct
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class FilmDetail(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmList(generics.ListCreateAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    # def list(self, request):
    #     logger.debug("get_queryset called")
    #     limit = self.request.query_params.get('limit', 10)
    #     films = self.get_queryset()[:int(limit)]
    #     serializer = FilmSerializer(films, many=True)
    #     return JsonResponse(serializer.data, safe=False)    

    def get_queryset(self):
        logger.debug("get_queryset called")
        limit = self.request.query_params.get('limit', 10)
        films = Film.objects.all()[:int(limit)]
        print(distinct(films))
        return films

urlpatterns = [
    path('', views.index, name="index"),
    path('languages/', views.languages, name="languages"),
    path('film/<int:id>/', views.film, name="film"),
    path('api/film/<int:pk>/', FilmDetail.as_view(), name="film-detail"),
    path('api/films/', FilmList.as_view(), name="film-list"),
]