from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *
import ast
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def languages(request):
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
    

def films(request):
    films = Film.objects.all()[:20]
    return JsonResponse(serializers.serialize('python', films), safe=False)