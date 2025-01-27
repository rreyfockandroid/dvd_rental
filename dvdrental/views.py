from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *
import ast

def index(request):
    langs = Language.objects.all()
    llangs = [lang.name + " " + str(lang.language_id) + "<br />" for lang in langs]
    return HttpResponse(llangs)

def film(request, id):
    try:
        film = Film.objects.get(film_id=id)
        data = serializers.serialize('python', [film])
        return JsonResponse(data, safe=False)
    except Film.DoesNotExist as e:
        return HttpResponse("Film not found", status=404)
    